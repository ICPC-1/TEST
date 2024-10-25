from modules.test_validator import TestValidator
from modules.test_runner import TestRunner


class Test:

    def __init__(self, file_path, tests_dir, mode):
        self.file_path = file_path
        self.tests_dir = tests_dir
        self.mode = mode

    def run(self):
        validator = TestValidator(self.file_path, self.tests_dir, self.mode)
        validator.validate()

        runner = TestRunner(self.file_path, self.tests_dir, self.mode)
        runner.get_in_ans_pairs()
        runner.find_per_test_case_score()
        runner.run_tests()
