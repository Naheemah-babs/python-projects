def count_words_lines(filename):
    try:
        with open (filename, "r") as file:
            lines = file.readlines()
            line_count = len(lines)
            word_count = sum(len(line.split()) for line in lines)

            print(f"lines number: {line_count}")
            print(f"words number: {word_count}")
    except FileNotFoundError:
        print(f"File {filename} not found")

count_words_lines("sample.txt")