import csv
import re
import requests
from os import makedirs
from os.path import exists
from pathlib import Path

images_dir_path = "images/"

def download_image_from_url(image_url: str):
    file_name = "images/" + image_url.replace("https://storage.googleapis.com/fabmaster/media/images/", "")
    if exists(file_name):
        print(file_name + " already exists, skipping")
        return

    print("Downloading " + image_url + " to " + file_name)
    img_data = requests.get(image_url).content
    with open(file_name, 'wb') as handler:
        handler.write(img_data)

if not exists(images_dir_path):
    print(images_dir_path + " does not exist, creating it")
    makedirs(images_dir_path)

path = Path(__file__).parent / "../csvs/card.csv"
with path.open(newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t', quotechar='"')
    next(reader)

    for row in reader:
        image_urls = [re.split(" – | - ", url.strip())[0].strip() for url in row[23].split(',')]
        for image_url in image_urls:
            download_image_from_url(image_url)

