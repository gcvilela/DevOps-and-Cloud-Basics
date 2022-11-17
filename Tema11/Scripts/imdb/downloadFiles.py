import requests
import gzip
import shutil
import os

def download(file_name):
    file_url = r"https://datasets.imdbws.com/{}.gz".format(file_name)
    r = requests.get(file_url,stream=True)

    file = '{}.gz'.format(file_name)

    with open(file,'wb') as f:
        for chunk in r.iter_content(chunk_size=10000):
            if chunk:
                f.write(chunk)
    
    path = os.getcwd()
    src= os.path.join(path,file)
    des = os.path.join(path, "imdb","files",file)
    os.rename(src,des)

    pathname = os.path.join(path,"imdb","files",file_name)
    with gzip.open(des,"rb") as file_in:
        with open(pathname,'wb') as file_out:
            shutil.copyfileobj(file_in,file_out)

    os.remove(des)

def execute():
    download("title.basics.tsv")
    download("title.principals.tsv")
    download("name.basics.tsv")
