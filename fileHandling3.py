copying content of a file to the other
def copy_file(filename):
    with open ("sample.txt", "r") as firstFile, open ("second.txt", "a") as secondFile:
        secondFile.write(firstFile.read())

copy_file("sample.txt")

