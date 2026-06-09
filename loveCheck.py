# num = int(input("Enter a number: "))

# factorial = 1;

# for i in range(1, number + 1):
#     factorial = factorial * i

# print("The factorial of", number, "is", factorial)

user_name = input("Whats your name?  ")
user_partner_name = input("Whats your partner name?  ")
true_word_check = "true"
love_word_checker = "love"
grand_total = 0
grand_total_love = 0


for letter in true_word_check:
    count_true = 0

    for char in user_name:
        if letter == char:
            count_true += 1;
            
            

    for char in user_partner_name:
        if letter == char:
            count_true += 1;
    
    print(f"Letter '{letter}' appears {count_true} times in both variables combined")
    grand_total += count_true
print(f"true score is {grand_total}")

for letter in love_word_checker:
    count_love = 0

    for char in user_name:
        if letter == char:
            count_love += 1;

    for char in user_partner_name:
        if letter == char:
            count_love += 1;
    
    print(f"Letter '{letter}' appears {count_love} times in both variables combined")
    grand_total_love += count_love
print(f"love score is {grand_total_love}")

if grand_total_love < 10 and grand_total_love > 90:
    print(f" true love score is {grand_total}{grand_total_love}, you are compatible")
elif grand_total_love >= 40 and grand_total_love <= 50:
     print(f" true love score is {grand_total}{grand_total_love}, you are alright")
else:
     print(f" true love score is {grand_total}{grand_total_love}")