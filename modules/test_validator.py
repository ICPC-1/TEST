import os

class TestValidator:

    def __init__(self, file_path, tests_dir, mode):
        self.file_path = file_path
        self.tests_dir = tests_dir
        self.mode = mode

    def validate(self):
        self._validate_mode()
        self._validate_file()
        self._validate_directory()
        self._validate_test_files()

    def _validate_file(self):
        if not os.path.isfile(self.file_path):
            raise FileNotFoundError("File path is not valid")
        print("File path is valid")

    def _validate_directory(self):
        if not os.path.isdir(self.tests_dir):
            raise NotADirectoryError("Test directory path is not valid")
        print("Test directory path is valid")

    def _validate_mode(self):
        if self.mode not in ["TOTAL", "DEBUG"]:
            raise ValueError("Mode is not correct. Use 'TOTAL' or 'DEBUG'")
        print("The mode is valid")

    def _validate_test_files(self):
        for file_name in os.listdir(self.tests_dir):
            full_path = os.path.join(self.tests_dir, file_name)
            if not os.path.isfile(full_path):
                print(f"There is a directory in the specified path named ({file_name}). All should be files.")
                continue

            if not (file_name.endswith('.ans') or file_name.endswith('.in')):
                raise ValueError("In the test case directory, there is at least one file with an invalid format")
        print("All files in the test directory have valid formats")
