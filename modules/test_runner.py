import os
import subprocess

class TestRunner:

    def __init__(self, file_path, tests_dir, mode):
        self.file_path = file_path
        self.tests_dir = tests_dir
        self.mode = mode
        self.tests_list = []
        self.score_per_test_percent = 0
        self.per_test_case_score = 0

    def get_in_ans_pairs(self):
        files = os.listdir(self.tests_dir)
        file_pairs = {}

        for file_name in files:
            full_path = os.path.join(self.tests_dir, file_name)
            if not os.path.isfile(full_path):
                continue

            base_name, extension = os.path.splitext(file_name)
            if extension == ".in" or extension == ".ans":
                if base_name not in file_pairs:
                    file_pairs[base_name] = [None, None]

                if extension == ".in":
                    file_pairs[base_name][0] = full_path
                elif extension == ".ans":
                    file_pairs[base_name][1] = full_path

        self.tests_list = [pair for pair in file_pairs.values() if all(pair)]

    def find_per_test_case_score(self):
        test_list_len = len(self.tests_list)
        if test_list_len == 0:
            raise ValueError("No valid test cases found")
        self.score_per_test_percent = round(100 / test_list_len, 2)
        self.per_test_case_score = self.score_per_test_percent

    def read_file(self, file_path):
        with open(file_path, 'r') as file:
            return file.read()

    def test_pass(self, input_file_path, answer_file_path):
        input_content = self.read_file(input_file_path)
        expected_output = self.read_file(answer_file_path).strip()

        process = subprocess.run(
            ["python3", self.file_path,input_content],
            capture_output=True,
            text=True
        )

        output = process.stdout.strip()
        
        return output == expected_output

    def test_state(self, base_name, state):
        if self.mode == "TOTAL":
            return
        color = "\033[91m" if state == "fail" else "\033[92m"
        status = "fail" if state == "fail" else "success"
        print(f"{color}{base_name} : {status}\033[0m")

    def write_final_score(self, final_score):
        rounded_score = round(final_score)
        print("#####################################################")
        if rounded_score < 50:
            print(f"\033[91mFinal score: {rounded_score} : fail\033[0m")
        elif 50 <= rounded_score < 100:
            print(f"\033[92mFinal score: {rounded_score} : not bad\033[0m")
        elif rounded_score == 100:
            print(f"\033[92mFinal score: {rounded_score} : done, bravo bro\033[0m")
        print("#####################################################")

    def run_tests(self):
        final_score = 0
        for input_file, answer_file in self.tests_list:
            base_name, _ = os.path.splitext(os.path.basename(input_file))
            if self.test_pass(input_file, answer_file):
                final_score += self.per_test_case_score
                self.test_state(base_name, "success")
            else:
                self.test_state(base_name, "fail")

        self.write_final_score(final_score)
