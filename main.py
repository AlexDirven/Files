__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

import os
from zipfile import ZipFile

#Part 1
#clean_cache: takes no arguments and creates an empty folder named cache in the current
#directory. If it already exists, it deletes everything in the cache folder.
def clean_cache():
    if os.path.exists('cache'):
        for filename in os.listdir('cache'):
            os.remove('cache/'+filename)
    else:
        os.mkdir('cache')

#Part 2
#cache_zip: takes a zip file path (str) and a cache dir path (str) as arguments,
#in that order. The function then unpacks the indicated zip file into a clean cache folder.
#You can test this with data.zip file.
        
def cache_zip(zip_file_path, cache_dir_path):
    with ZipFile(zip_file_path) as clean_cache:
         clean_cache.extractall(cache_dir_path)

#Part 3
#cached_files: takes no arguments and returns a list of all the files in the cache.
#The file paths should be specified in absolute terms. Search the web for what this means!
#No folders should be included in the list. You do not have to account for files
#within folders within the cache directory.         
         
def cached_files():
    files = []
    for filename in os.listdir('cache'):
        if os.path.isfile('cache/'+filename):
            files.append(os.path.abspath('cache/'+filename))
    return files

#Part 4
#find_password: takes the list of file paths from cached_files as an argument.
#This function should read the text in each one to see if the password is in there.
#Surely there should be a word in there to incidicate the presence of the password?
#Once found, find_password should return this password string.


def find_password(cache_files):
    for file in cache_files:
        with open(file) as file_path:
            content = file_path.read()
            lines = content.splitlines()
            for line in lines:
                if line.find('password') != -1:
                    password = line.replace('password: ', '')
    return password