import sys
import os


class Test:

    def __init__(self,file_path,tests_dir,mode):
        self.file_path = file_path
        self.tests_dir = tests_dir
        self.mode = mode
        self.testsList = []
        self.scorePerFilePercent = 0

    def file_exist(self):
        if not os.path.isfile(self.file_path):
            print("file path is not valid")
            sys.exit(1)

        print("filereturn result path is valid")

    def is_file_path(self,file_absul_path):

        if not os.path.isfile(file_absul_path):
            return True
        return False

    def is_valid_test_dir(self):

        for file_name in os.listdir(self.tests_dir):

            if not is_file_path(os.path.join(self.tests_dir,file_name)):
                print(f"there is a directory in path you specify named ( {file_name} ) but i think must all be .in or .ans files")
                continue

            if not (file_name.endswith(".ans") or file_name.endswith(".in")):
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

            if not is_file_path(os.path.join(self.tests_dir,file_name)):
                print(f"there is a directory in path you specify named ( {file_name} ) but i think must all be .in or .ans files")
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



    #     # second find that each of the files checking have what score for sum them and the reult be 100 percent
    #     # third read the input file and answer file and run the code and see the output of the code and see is the output same as the .ans file or not
    #     # do this with all the files in the array
    #     # this time that must check the if the mode is DEBUG or TOTAL 
    #     #       TOTAL : give just a percent that is reslt of calculate all the files
    #     #       DEBUG : give one by one of the files ok with green and red with no in this format 
    #     #       for ok : green [ test name : ok ]
    #     #   for not ok : red [test name : not ok]


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

main()
