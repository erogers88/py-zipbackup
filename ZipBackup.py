import zipfile
import datetime
import os
import argparse

def get_all_file_paths(directory):
    # initializing empty file paths list 
    file_paths = [] 
  
    # crawling through directory and subdirectories 
    for root, directories, files in os.walk(directory): 
        for filename in files: 
            # join the two strings in order to form the full filepath. 
            full_path = os.path.join(root, filename) 
            file_paths.append(full_path) 
  
    # returning all file paths 
    return file_paths  

def create_backup(local_save_directory, remote_save_directory, file_prefix):

    # get all files in the input directory
    all_file_paths = get_all_file_paths(local_save_directory)

    # get current datetime and format as string
    current_date_time = datetime.datetime.now()
    time_stamp = '{:%Y-%m-%d_%H-%M-%S}'.format(current_date_time)

    # write timestamped zip file in remote directory with all files
    with zipfile.ZipFile(remote_save_directory + file_prefix + time_stamp + ".zip", 'w') as zip:
        for file in all_file_paths:
            zip.write(file)