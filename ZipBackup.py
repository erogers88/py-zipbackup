import zipfile
import datetime
import os
from pathlib import Path

"""
create_backup method can be used to back up an entire directory.
"""


def get_all_file_paths(directory):
    # initializing empty file paths list 
    file_paths = [] 
  
    # crawling through directory and subdirectories 
    for root, directories, files in os.walk(directory): 
        for filename in files: 
            # join the two strings in order to form the full filepath. 
            full_path = Path(os.path.join(root, filename))
            file_paths.append(full_path)      
    
    # returning all file paths 
    return file_paths  

def create_backup(source_location, backup_location, file_prefix):
    """
    source_location:     absolute path to directory to back up
    backup_location:     absolute path to backup directory
    file_prefix:         short prefix to add to beginning of zip file
    """

    # create path object to calculate relative path
    source_path = Path(source_location)
    
    # get all files in the input directory
    all_file_paths = get_all_file_paths(source_path)

    # get current datetime and format as string
    current_date_time = datetime.datetime.now()
    time_stamp = '{:%Y-%m-%d_%H-%M-%S}'.format(current_date_time)

    # write timestamped zip file in remote directory with all files in relative path
    with zipfile.ZipFile(backup_location + file_prefix + time_stamp + ".zip", 'w') as zipped_file:
        for file in all_file_paths:
            zipped_file.write(
                file.absolute(), 
                arcname=str(file.relative_to(source_path))
            )