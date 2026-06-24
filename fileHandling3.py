from datetime import datetime

#log messages with timestamps into a file
message = input("Enter a message \n")
def log_message(filename):
    with open ("log.txt", "w") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] {message}")

    with open ("log.txt", "r") as file:
        for line in file:
            print(line)

log_message("log.txt")