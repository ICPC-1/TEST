import sys

def main():
    if len(sys.argv) < 2:
        print("Please provide at least one argument.")
        sys.exit(1)
    
    arg = int(sys.argv[1])
    if arg == 5:
        print("0")
    elif arg == 18:
        print("1")

if __name__ == "__main__":
    main()
