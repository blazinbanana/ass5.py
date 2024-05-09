# File Creation
def create_file():
    try:
        with open("calebsFile.txt", 'w') as file:
            file.write("Bruised ego\n")
            file.write("10032\n")
            file.write("All 500 of his men died\n")
    except IOError as e:
        print("Error occurred while creating the file:", e)
    else:
        print("File created successfully.")


#file reading and display
def readFile():
    try:
        with open("calebsFile.txt",'r') as file:
            content=file.read()
            print("Content of calebsFile.txt:")
            print(content)
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied to access the file.")
    except Exception as e:
        print("Error occurred while reading the file:",e)


#file appending
def appendTofile():
    try:
        with open("calebsFile.txt",'a') as file:
            file.write("Don't patronize me!\n")
            file.write("bonyeza *544#\n")
            file.write("sabbath is the 7th day")
    except PermissionError:
        print("Permission denied to access the file.")
    except Exception as e:
        print("Error occurred while appending the file",e)


if __name__== "__main__":
    create_file()
    readFile()
    appendTofile()
    readFile()  #read file after appending