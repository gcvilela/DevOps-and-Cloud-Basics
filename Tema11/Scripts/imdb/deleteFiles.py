import os

def delete(file_name):
  
    pathname = os.path.join(os.getcwd(), "imdb","files",file_name)
    os.remove(pathname)

def execute():
    delete("title.basics.tsv")
    delete("title.principals.tsv")
    delete("name.basics.tsv")
    print("Deletions Finished")
