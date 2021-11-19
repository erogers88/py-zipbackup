import ZipBackup

source = "C:\\temp\\source\\"
target = "C:\\temp\\target\\"
prefix = "test_prefix"
extension = "vdf"

ZipBackup.create_backup(source, target, prefix, extension)