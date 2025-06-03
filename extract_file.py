import zipfile
import json

zip_path = "/Users/raphaelportela/Downloads/allen-ai.zip"

with zipfile.ZipFile(zip_path, "r") as zip_ref:
    # Get the first JSON file in the archive
    file_list = [f for f in zip_ref.namelist() if f.endswith('.json')]
    first_file = file_list[0]
    print(f"Reading: {first_file}")
    with zip_ref.open(first_file) as f:
        data = json.load(f)
        # Print the top-level keys and a sample of the data
        print("Top-level keys:", data.keys())
        for key in data:
            print(f"{key}: {type(data[key])}")
        # Optionally, print a pretty sample of the JSON
        print(json.dumps(data, indent=2)[:2000])  # Print first 2000 char