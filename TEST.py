import sys
from modules.test import Test


def main():

    if len(sys.argv) != 4:
        print("Incorrect command format. Correct format: python3 main.py /path/to/Code.py /path/to/Test/Dir MODE")
        sys.exit(1)

    file_path = sys.argv[1]
    tests_dir = sys.argv[2]
    mode = sys.argv[3]
    test_instance = Test(file_path, tests_dir, mode)
    test_instance.run()


if __name__ == "__main__":
    main()
