from fastapi import FastAPI
from urllib.parse import unquote
import requests
import re

app = FastAPI()

def download_torrent(dl_url):
    file_path = "/downloads/"
    url = unquote(dl_url)
    payload = {}
    headers = {}
    print(url)
    response = requests.request("GET", url, headers=headers, data=payload)
    if "Content-Disposition" in response.headers:
        content_disposition = response.headers["Content-Disposition"]
        filename = (re.findall('filename=(.+)', content_disposition)[0]).replace('"', "")
        print(f"Filename: {filename}")
    else:
        filename = ''
        print("Content-Disposition header not found.")
    if response.status_code == 200:
        with open(file_path+filename, "wb") as file:
            file.write(response.content)
        print(f"File downloaded successfully to {file_path}")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")

@app.get("/")
async def read_item(url: str = 200):
    download_torrent(url)