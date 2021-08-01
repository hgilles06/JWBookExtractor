from jwbookextractor import SaveSrc
import json
import pandas as pd
from tqdm import tqdm

with open("parameters.json", encoding="utf-8") as file:
    parameters = json.load(file)

book_urls = pd.read_csv("book_urls.csv")

source_file = parameters["source_file"]
save_dir = parameters["save_dir"]

for i in tqdm(range(book_urls.shape[0])):
    
    source_url = book_urls.source_url.iloc[i]
    
    SaveSrc(source_url, source_file, save_dir)


