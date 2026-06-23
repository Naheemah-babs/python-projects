#writing and reading list of items

#write files
def write_files(filename, items):
    with open(filename, "w") as file:
        for item in items:
            file.write(item + "\n")

#read files

def read_files(filename):
    try:
        with open(filename, "r") as file:
            items = file.readlines()
            for item in items:
                print(item.strip())

    except FileNotFoundError:
        print(f" {filename} not found")

pronouns = ["he", "she", "him"]
write_files("pronoun.txt", pronouns)
read_files("pronoun.txt")
