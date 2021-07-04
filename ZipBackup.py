import zipfile
import datetime
import os
from pathlib import Path
import re

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
            full_path = os.path.join(root, filename)
            file_paths.append(full_path)      
    
    # returning all file paths 
    return file_paths  

def create_backup(source_location, backup_location, file_prefix, extension=""):
    """
    source_location:     absolute path to directory to back up
    backup_location:     absolute path to backup directory
    file_prefix:         short prefix to add to beginning of zip file
    extension:           (optional) keep only files of this type
    """
    
    # create path object to calculate relative path
    source_path = Path(source_location)
    
    # get all files in the input directory
    all_file_paths = get_all_file_paths(source_path)
    
    # keep only matching extensions
    extension_regex = re.compile("\." + extension)  
    matching_paths = list(filter(extension_regex.search, all_file_paths))

    # get current datetime and format as string
    current_date_time = datetime.datetime.now()
    time_stamp = '{:%Y-%m-%d_%H-%M-%S}'.format(current_date_time)

    # write timestamped zip file in remote directory with all files in relative path
    with zipfile.ZipFile(backup_location + file_prefix + time_stamp + ".zip", 'w') as zipped_file:
        for file in matching_paths:
            zipped_file.write(
                Path(file).absolute(), 
                arcname=str(Path(file).relative_to(source_path))
            )