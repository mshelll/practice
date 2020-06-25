# Refactor code: Not timed (good to get it back within 24 hours) 
# Aim for production quality ‘best-practice/clean’ code.
# Please explain/show how you would test.
#
# The requirements of the code is to update the build number in
# two different files.

import os
import re
import unittest
import shutil


class TestFileUpdate(unittest.TestCase):

    def setUp(self):
        self.working_dir = os.path.join(os.getcwd(), "SourcePath", "develop", "global", "src")
        os.makedirs(self.working_dir, exist_ok=True)
        os.environ["SourcePath"] = os.path.join(os.getcwd(), "SourcePath")
        os.environ["BuildNum"] = "7"

    def tearDown(self):
        del os.environ["BuildNum"]
        del os.environ['SourcePath']
        shutil.rmtree(os.path.join(os.getcwd(), "SourcePath"), ignore_errors=True)

    def test_updateSConstruct(self):
        input_content = """
                        config.version = Version( 
                            major=15,
                            minor=0,
                            point=6,
                            patch=0
                        )
                        """
        file_name = os.path.join(self.working_dir, "SConstruct")
        with open(file_name, 'w') as fout:
            fout.write(input_content)
        updateSconstruct()
        with open(file_name, 'r') as fin:
            assert "point={}".format(os.environ["BuildNum"]) in fin.read()

    def test_updateVersion(self):
        input_content = """
                        ADLMSDK_VERSION_POINT=6
                        """
        file_name = os.path.join(self.working_dir, "VERSION")
        with open(file_name, 'w') as fout:
            fout.write(input_content)
        updateVersion()
        with open(file_name, 'r') as fin:
            assert "ADLMSDK_VERSION_POINT={}".format(os.environ["BuildNum"]) in fin.read()

def updateFile(parent_dir, file_name, field_name, field_value):
    """
      utility file to update field in a file with BuildNum
      The routine will create a temp file write the updated contents
      Then replace the original file with the new temp file retaining original name
      Input:
      parent_dir : working directory of file
      file_name  : file to be updated
      field_name : fileld to be updated in File
      field_value : value to be substituted
    """
    file1 = os.path.join(parent_dir, file_name)
    file2 = os.path.join(parent_dir, "temp")
    match_pattern = "{}\=[\d]+".format(field_name)
    substitute = "{}={}".format(field_name, field_value)

    os.chmod(file1, 775)

    with open(file1, 'r') as fin, open(file2, 'w') as fout:
        for line in fin:
            pattern = re.sub(match_pattern, substitute, line)
            fout.write(pattern)

    os.remove(file1)
    os.rename(file2, file1)

#SCONSTRUCT file interesting line
# config.version = Version( 
#     major=15,
#     minor=0,
#     point=6,
#     patch=0
# )
def updateSconstruct():
    updateFile(parent_dir=os.path.join(os.environ["SourcePath"],"develop","global","src"),
               file_name="SConstruct",
               field_name="point",
               field_value=os.environ['BuildNum'])

# # VERSION file interesting line
# ADLMSDK_VERSION_POINT=6
def updateVersion():
    updateFile(parent_dir=os.path.join(os.environ["SourcePath"],"develop","global","src"),
               file_name="VERSION",
               field_name="ADLMSDK_VERSION_POINT",
               field_value=os.environ['BuildNum'])


def main():
    # updateSconstruct()
    # updateVersion()
    unittest.main()



main()