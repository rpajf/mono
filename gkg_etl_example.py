import requests
import pandas as pd
import zipfile
import io
import os

# Step 1: Get the latest GKG file URL
def get_latest_gkg_url():
    lastupdate_url = "http://data.gdeltproject.org/gdeltv2/lastupdate-translation.txt"
    resp = requests.get(lastupdate_url)
    if resp.status_code == 200:
        # Split the first line and get the last part (the URL)
        return resp.text.strip().split('\n')[0].split()[-1]
    else:
        raise Exception("Failed to fetch latest GKG file URL.")

latest_gkg_url = get_latest_gkg_url()

# Step 2: Download the latest GKG file
response = requests.get(latest_gkg_url)
if response.status_code == 200:
    with zipfile.ZipFile(io.BytesIO(response.content)) as z:
        csv_filename = z.namelist()[0]
        z.extract(csv_filename)
else:
    raise Exception("Failed to download GKG file.")

# Step 3: Load the CSV into a DataFrame
# GKG files are tab-delimited and have no header by default
colnames = [
    "GKGRECORDID", "DATE", "SourceCollectionIdentifier", "SourceCommonName", "DocumentIdentifier",
    "Counts", "V2Counts", "Themes", "V2Themes", "Locations", "V2Locations", "Persons", "V2Persons",
    "Organizations", "V2Organizations", "V2Tone", "Dates", "GCAM", "SharingImage", "RelatedImages",
    "SocialImageEmbeds", "SocialVideoEmbeds", "Quotations", "AllNames", "Amounts", "TranslationInfo",
    "Extras"
]
df = pd.read_csv(csv_filename, sep='\t', names=colnames, dtype=str, low_memory=False)

# Step 4: Filter for a specific keyword in the 'Themes' column (e.g., 'CLIMATE_CHANGE')
keyword = "CLIMATE_CHANGE"
filtered_df = df[df["Themes"].str.contains(keyword, na=False)]

# Step 5: Further filter for US and Brazil domains using 'SourceCommonName'
def is_us_or_br_domain(domain):
    if pd.isna(domain):
        return False
    domain = domain.lower()
    return domain.endswith('.br') or domain.endswith('.us') or domain.endswith('.com') or domain.endswith('.org') or domain.endswith('.gov') or domain.endswith('.edu')


filtered_df = filtered_df[filtered_df["SourceCommonName"].apply(lambda d: (isinstance(d, str) and (d.endswith('.br') or d.endswith('.us') or d.endswith('.com') or d.endswith('.org') or d.endswith('.gov') or d.endswith('.edu'))))]

# Optional: If you want to be more strict, you can use a list of known US and Brazil domains.

# Step 6: Save the filtered results to a CSV
output_csv = "filtered_gkg_climate_change_us_br.csv"
filtered_df.to_csv(output_csv, index=False)

print(f"Filtered {len(filtered_df)} records with keyword '{keyword}' from US and Brazil domains. Saved to {output_csv}.")

# Optional: Clean up extracted CSV file
os.remove(csv_filename) 