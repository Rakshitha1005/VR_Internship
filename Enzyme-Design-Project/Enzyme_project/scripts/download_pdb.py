import os
import requests

pdb_id = "1CI8"
data_folder = "../data"
os.makedirs(data_folder, exist_ok=True)
output_path = os.path.join(data_folder, "predicted_structure.pdb")

url = f"https://files.rcsb.org/download/{pdb_id}.pdb"
headers = {"User-Agent": "Mozilla/5.0"}

try:
    response = requests.get(url, headers=headers, timeout=30)  # 30 sec timeout
    response.raise_for_status()
    with open(output_path, "wb") as f:
        f.write(response.content)
    print(f"✅ Downloaded {pdb_id}.pdb successfully.")
except requests.exceptions.RequestException as e:
    print(f"❌ Failed to download: {e}")
