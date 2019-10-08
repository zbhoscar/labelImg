import sys

def main():
    print(sys.argv)
    # print(len(sys.argv) >= 5)
    # print(sys.argv[4] is not 'False', ''': %s is not "False" ''' % sys.argv[4])
    print(True if len(sys.argv) >= 5 and sys.argv[4] != 'False' else False)


if __name__ == '__main__':
    main()