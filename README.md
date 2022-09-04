# ZipBackup

This library implements a function that can be used to create a backup of a specified folder,
with the option of only keeping certain file extensions if desired.

```python
def create_backup(source_location, backup_location, file_prefix, extension=""):
    """
    source_location:  absolute path to directory to back up
    backup_location:  absolute path to backup directory
    file_prefix:        short prefix to add to beginning of zip file
    extension:        (optional) keep only files of this type
    """
```

