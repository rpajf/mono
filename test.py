import kagglehub
import zipfile
import json
from collections import Counter, defaultdict
import os
from etl import ETLProcessor

# Download the latest version of the dataset
# path = kagglehub.dataset_download("allen-institute-for-ai/CORD-19-research-challenge")


# Path to the zip file
zip_path = "/Users/raphaelportela/Downloads/allen-ai.zip"
target_file = "document_parses/pmc_json/PMC9146536.xml.json"

def is_text_file(filename):
    # Check for common text file extensions
    return filename.endswith(('.json', '.txt', '.csv', '.readme'))

with zipfile.ZipFile(zip_path, "r") as zip_ref:
    file_list = zip_ref.namelist()
    print(f"Total files in zip: {len(file_list)}\n")

    # Count by file extension
    ext_counter = Counter()
    # Count by top-level directory
    dir_counter = Counter()
    # Count by second-level directory (if present)
    second_level_counter = Counter()

    for f in file_list:
        # Extension
        ext = os.path.splitext(f)[1]
        ext_counter[ext] += 1

        # Top-level directory
        parts = f.split('/')
        if len(parts) > 1:
            dir_counter[parts[0]] += 1
        else:
            dir_counter['(root)'] += 1

        # Second-level directory
        if len(parts) > 2:
            second_level_counter[parts[1]] += 1

    print("File count by extension:")
    for ext, count in ext_counter.items():
        print(f"  {ext or '(no extension)'}: {count}")

    print("\nFile count by top-level directory:")
    for d, count in dir_counter.items():
        print(f"  {d}: {count}")

    print("\nFile count by second-level directory (if present):")
    for d, count in second_level_counter.items():
        print(f"  {d}: {count}")

    # Count total size of all .json files
    json_total_size = 0
    for f in file_list:
        if f.endswith('.json'):
            info = zip_ref.getinfo(f)
            json_total_size += info.file_size
    print(f"\nTotal size of all .json files: {json_total_size / (1024 * 1024):.2f} MB")

    # Find the first text file
    text_file = next((f for f in file_list if is_text_file(f)), None)

    # if text_file:
    #     print(f"\nPrinting content of: {text_file}\n")
    #     with zip_ref.open(text_file) as f:
    #         content = f.read().decode("utf-8")
    #         print(content)
    # else:
    #     print("No text file found in the zip archive.")

    if target_file in zip_ref.namelist():
        print(f"\nPrinting content of: {target_file}\n")
        with zip_ref.open(target_file) as f:
            content = f.read().decode("utf-8")
            # print(content)
    else:
        print(f"{target_file} not found in the zip archive.")

if __name__ == "__main__":
    # Get all .json article files from the zip
    article_files = [f for f in file_list if f.endswith('.json')]
    etl = ETLProcessor(article_files)
    etl.run()

# def run(self):
#     print("ETL process started. This is a placeholder for your ETL logic.")
#     mid = len(self.articles) // 2
#     category_1 = self.articles[:mid]
#     category_2 = self.articles[mid:]
#     print(f"Category 1: {len(category_1)} articles")
#     print(f"Category 2: {len(category_2)} articles")
