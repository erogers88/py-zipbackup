import zipfile
import datetime
import os

LocalSaveDirectory = "C:\\Users\\erik\\Documents\\My Games\\Grim Dawn\\save\\"
RemoteSaveDirectory = "\\\\RogersShare\\Public\\VideoGames\\Windows_PC\\SaveGames\\Grim_Dawn\\"
FilePrefix = "GD_Backup_"

def get_all_file_paths(directory): 
  
    # initializing empty file paths list 
    FilePaths = [] 
  
    # crawling through directory and subdirectories 
    for root, directories, files in os.walk(directory): 
        for filename in files: 
            # join the two strings in order to form the full filepath. 
            Fullpath = os.path.join(root, filename) 
            FilePaths.append(Fullpath) 
  
    # returning all file paths 
    return FilePaths  

def main():

    # get all grim dawn save files
    GrimDawnSaveFiles = get_all_file_paths(LocalSaveDirectory)

    # get current datetime and format as string
    CurrentDateTime = datetime.datetime.now()
    TimeStamp = '{:%Y-%m-%d_%H-%M-%S}'.format(CurrentDateTime)

    # write timestamped zip file in remote directory with all grim dawn save files
    with zipfile.ZipFile(RemoteSaveDirectory + FilePrefix + TimeStamp + ".zip", 'w') as zip:
        for file in GrimDawnSaveFiles:
            zip.write(file)

if __name__ == "__main__": 
    main() 