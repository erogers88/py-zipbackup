import os  # mkdir, path, listdir
import shutil  # rmtree
import unittest  # TestCase
import zipfile  # ZipFile
from pathlib import Path  # Path
import zbu


class TestCopyThreeSets(unittest.TestCase):

    def cleandir(self):
        source_path = os.path.dirname(__file__) + "/source/"
        target_path = os.path.dirname(__file__) + "/target/"
        # check and delete temp folders if they exist
        if (os.path.exists(Path(source_path))):
            shutil.rmtree(source_path)
        if (os.path.exists(Path(target_path))):
            shutil.rmtree(target_path)

    def setUp(self):
        self.cleandir()

    def tearDown(self):
        self.cleandir()

    def test_create_and_copy_three_sets(self):
        source_path = os.path.dirname(__file__) + "/source/"
        target_path = os.path.dirname(__file__) + "/target/"

        # create test folders
        os.mkdir(source_path)
        os.mkdir(target_path)

        # create test files to archive
        open(source_path + "bb-01.bb", 'a').close()
        open(source_path + "bb-02.bb", 'a').close()
        open(source_path + "tt-01.tt", 'a').close()
        open(source_path + "tt-02.tt", 'a').close()
        open(source_path + "tt-03.tt", 'a').close()
        open(source_path + "zz-01.zz", 'a').close()

        # create backup zips for three extensions
        prefix = "bb"
        extension = "bb"
        zbu.create_backup(source_path, target_path, prefix, extension)

        prefix = "tt"
        extension = "tt"
        zbu.create_backup(source_path, target_path, prefix, extension)

        prefix = "zz"
        extension = "zz"
        zbu.create_backup(source_path, target_path, prefix, extension)

        # get count of all archived files
        bb_count = 0
        tt_count = 0
        zz_count = 0
        target_dir_list = os.listdir(target_path)
        for target_dir_list_item in target_dir_list:
            zip_backup = zipfile.ZipFile(target_path + target_dir_list_item, 'r')
            for file_name in zip_backup.namelist():
                file_extension = file_name[file_name.find('.')+1:]
                if (file_extension == "bb"):
                    bb_count += 1
                if (file_extension == "tt"):
                    tt_count += 1
                if (file_extension == "zz"):
                    zz_count += 1

        self.assertEqual(len(target_dir_list), 3)
        self.assertEqual(bb_count, 2)
        self.assertEqual(tt_count, 3)
        self.assertEqual(zz_count, 1)


if (__name__ == "__main__"):
    unittest.main()
