
import sys
import os
import subprocess


def main(arg):
    print("python main function")
    create(arg[1])


def create(query):
    """ 
        create file with supplied query
    """

    base_path = "/Users/qaiyyumhakimi/Desktop/gitpitch"
    path_exist = os.path.exists(base_path)
    print(path_exist)
    if not path_exist:
        print("path not exist ")
        os.makedirs(base_path)

    file_path = os.path.join(base_path, query + ".md")
    print(file_path)

    # Check file exist
    file_exist = os.path.isfile(file_path)
    print(file_exist)
    if not file_exist:
        try:
            f = open(file_path, "w")
            f.write("")
        except IOError:
            print("error")
        else:
            print("success")
        finally:
            f.close()
    print('file exist')
    # for i in range(10):
    # f.write("This line %d\r\n % (i+1)")

    print("done")


def open_with_vs_code():
    pass


if __name__ == "__main__":
    main(sys.argv)
