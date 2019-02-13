import requests, os, sys, zipfile
from datetime import datetime

ymd = sys.argv[1]
year = ymd[0:4]
date = ymd[4:8]

# JRDB会員情報
user = "18045423"
pwd = "01102743"

# 前日データ取得処理
filecode = "SED"
filename = filecode + year[2:4] + date + ".zip"
url = (
    "http://www.jrdb.com/member/datazip/"
    + filecode.title()
    + "/"
    + year
    + "/"
    + filename
)
DOWNLOAD_SAVE_DIR = "./"
response = requests.get(url, auth=(user, pwd))
saveFileName = filename
saveFilePath = os.path.join(DOWNLOAD_SAVE_DIR, saveFileName)
with open(saveFilePath, "wb") as saveFile:
    saveFile.write(response.content)

# 解凍処理
with zipfile.ZipFile(filename) as existing_zip:
    existing_zip.extractall("./")

# 払戻データ取得処理
filecode = "HJC"
filename = filecode + year[2:4] + date + ".zip"
url = (
    "http://www.jrdb.com/member/datazip/"
    + filecode.title()
    + "/"
    + year
    + "/"
    + filename
)
DOWNLOAD_SAVE_DIR = "./"
response = requests.get(url, auth=(user, pwd))
saveFileName = filename
saveFilePath = os.path.join(DOWNLOAD_SAVE_DIR, saveFileName)

with open(saveFilePath, "wb") as saveFile:
    saveFile.write(response.content)

# 解凍処理
with zipfile.ZipFile(filename) as existing_zip:
    existing_zip.extractall("./")
