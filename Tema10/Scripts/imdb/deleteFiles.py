import os

def delete(file_name):
  
    pathname = os.path.join(os.getcwd(), "imdb","files")  
    os.remove(r'{}/{}'.format(pathname,file_name))

def execute():
    delete("title.basics.tsv")
    delete("title.principals.tsv")
    delete("name.basics.tsv")
    print("Deletions Finished")
