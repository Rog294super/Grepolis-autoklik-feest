import requests
import os
import subprocess
import time

GITHUB_API = "https://api.github.com/repos/rog294super/Grepolis-autoklik-feest/releases/latest"  # Vervang met je eigen repo
EXE_NAME = "Autoklik.exe"

def get_local_version():
    try:
        output = subprocess.check_output([EXE_NAME, "--version"], text=True).strip()
        return output
    except Exception as e:
        print(f"❌ Kan lokale versie niet ophalen: {e}")
        return None


def get_latest_version_info():
    response = requests.get(GITHUB_API)
    data = response.json()
    tag = data["tag_name"]  # bijv: v1.15.1
    for asset in data["assets"]:
        if asset["name"] == EXE_NAME:
            return tag, asset["browser_download_url"]
    return None, None

def download_and_replace(url):
    with requests.get(url, stream=True) as r:
        with open("autoklik_new.exe", "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    if os.path.exists(EXE_NAME):
        os.remove(EXE_NAME)
    os.rename("autoklik_new.exe", EXE_NAME)

def restart():
    subprocess.Popen([EXE_NAME])
    time.sleep(1)
    exit()

# Uitvoering
tag, download_url = get_latest_version_info()
local_version = get_local_version()

if tag and local_version and tag.lstrip("v") > local_version:
    print(f"Nieuwe versie beschikbaar: {tag}")
    download_and_replace(download_url)
    restart()
else:
    print("Geen update nodig.")