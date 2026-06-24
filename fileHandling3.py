copying content of a file to the other
def copy_file(filename):
    with open ("sample.txt", "r") as firstFile, open ("second.txt", "a") as secondFile:
        secondFile.write(firstFile.read())

copy_file("sample.txt")

#counting number of occurence of a specific word in a text file
specWord = input("enter a word: \n")
def count_word(filename):
    with open ("sample.txt", "r") as file:
        lines = file.readlines()
        word_count = 0
        for line in lines:
            words = line.split()

            for word in words:
                if word == specWord:
                    word_count += 1
    print(f"'{specWord}' appears {word_count} times.")      
        
count_word("sample.txt")