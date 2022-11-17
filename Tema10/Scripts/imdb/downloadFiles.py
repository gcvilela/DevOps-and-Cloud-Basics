import requests
import gzip
import shutil
import os

def download(file_name):
    file_url = "https://datasets.imdbws.com/{}.gz".format(file_name)
    r = requests.get(file_url,stream=True)

    with open(r'{}.gz'.format(file_name),'wb') as file:
        for chunk in r.iter_content(chunk_size=10000):
            if chunk:
                file.write(chunk)
    
    path = os.getcwd()
    src= r'{}/{}.gz'.format(path,file_name)
    pathname = os.path.join(os.getcwd(), "imdb","files")
    des= r'{}/{}.gz'.format(pathname,file_name)
    os.rename(src,des)

    
    with gzip.open(r'{}/{}.gz'.format(pathname,file_name),"rb") as file_in:
        with open(r'{}/{}'.format(pathname,file_name),'wb') as file_out:
            shutil.copyfileobj(file_in,file_out)
      
    os.remove(r'{}/{}.gz'.format(pathname,file_name))


  

def execute():
    download("title.basics.tsv")
    download("title.principals.tsv")
    download("name.basics.tsv")
    print("Download Finished")
