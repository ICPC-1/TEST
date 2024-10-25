import sys
import os


class Test:

    def __init__(self,file_path,tests_dir,mode):
        self.file_path = file_path
        self.tests_dir = tests_dir
        self.mode = mode
        self.testsList = []
        self.scorePerTestPercent = 0
        self.per_testCase_score = 0

    def file_exist(self):
        if not os.path.isfile(self.file_path):
            print("file path is not valid")
            sys.exit(1)

        print("file path is valid")

    def is_file(self,file_absul_path):

        if os.path.isfile(file_absul_path):
            return True
        return False

    def is_valid_test_dir(self):

        for file_name in os.listdir(self.tests_dir):

            if not self.is_file(os.path.join(self.tests_dir,file_name)):
                print(f"there is a directory in path you specify named ( {file_name} ) but i think must all be .in or .ans files")
                continue

            if not (file_name.endswith('.ans') or file_name.endswith('.in')):
                print("in the test case directory you specifiy there is at list a file with invalid format please check the path and return to the run the TEST file")
                sys.exit(1)

        print("all the files format in test case folder have valid format")

    def dir_exist(self):
        if not os.path.isdir(self.tests_dir):
            print("test dir is not valid")
            sys.exit(1)
        print("test dir path is valid")

    def is_valid_test_mode(self):
        if self.mode not in ["TOTAL","DEBUG"]:
            print("mode is not correct")
            sys.exit(1)
        print("the mode is valid")


    def validate_arguments(self):
        self.is_valid_test_mode()
        self.file_exist()
        self.dir_exist()
        self.is_valid_test_dir()
    
    def get_in_ans_pairs(self):

        files = os.listdir(self.tests_dir)

        file_pairs = {}
        
        for file_name in files:

            if not self.is_file(os.path.join(self.tests_dir,file_name)):
                continue

            base_name, extension = os.path.splitext(file_name)
            
            if extension == ".in" or extension == ".ans":
                if base_name not in file_pairs:
                    file_pairs[base_name] = [None, None]
                
                if extension == ".in":
                    file_pairs[base_name][0] = file_name
                elif extension == ".ans":
                    file_pairs[base_name][1] = file_name
        
        result = [pair for pair in file_pairs.values() if all(pair)]
        self.testsList = result

    def find_per_testCase_score(self):
        testListLen=len(self.testsList)
        self.scorePerTestPercent=round(100/testListLen,2)

    def readFile(self,file_path):

        file = open(file_path,'r')
        try:
            content = file.read()
        finally:
            file.close()
        return content
        
    def testPass(self,inputFilePath,ansewrFilePath)
        input = readFile(inputFilePath)
        answer = readFile(ansewrFilePath)
        process = subprocess.run(["python3",self.file_path,input], capture_ouput = True, text = True)
        ouput = process.stdout.strip()
        if output ==  input :
            return True
        return False 

    def test_state(self, file_name,state):
        if self.mode == "TOTAL":
            return
        base_name, extension = os.path.splitext(file_name)

        if state == "fail":
            print(f"\033[91m{base_name} : fail\033[0m")
        else:
            print(f"\033[92m{base_name} : success\033[0m")

    def write_final_score(self,final_score):
        print("#####################################################")
        if final_score < 50:
            print(f"\033[91m final score: {final_score} : fail\033[0m")
        if final_score >= 50 and final_score != 100 :
            print(f"\033[92mfinal score: {base_name} : not bad\033[0m")
        if final_score == 100:
            print(f"\033[92mfinal score: {base_name} : done bravo bro\033[0m")
        print("#####################################################")

    def test(self):
        final_score = 0
        for test in self.testsList:
            if testPass(test[0],[test[1]]):
                final_score += self.per_testCase_score
                test_state(test[0],"success")
            else:
                test_state(test[0],"fail")
                
        write_final_score(final_score)



    @classmethod
    def createClass(cls):
        if len(sys.argv) != 4:
           print("structure of the command for run the code is not correct right format is like this : python3 TEST.py /path/to/the/Code.py /path/to/the/Test/Dir MODE")
           sys.exit(1)
        file_path = sys.argv[1]
        test_folder_path = sys.argv[2]
        mode = sys.argv[3]

        return cls(file_path,test_folder_path,mode)

def main():
    test = Test.createClass() 
    test.validate_arguments()
    test.get_in_ans_pairs()
    test.find_per_testCase_score()
    test.test()

main()
