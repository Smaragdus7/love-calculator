# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
names = name1+name2
names = names.upper()

count_true = names.count("T")
count_true += names.count("R")
count_true += names.count("U")
count_true += names.count("E")
count_love = names.count("L")
count_love += names.count("O")
count_love += names.count("V")
count_love += names.count("E")

count = str(count_true)+str(count_love)
count = int(count)

if count <10 or count >90:
    print(f"Your score is {count}, you go together like coke and mentos.")
elif count >=40 and count <=50:
    print(f"Your score is {count}, you are alright together.")
else:
    print(f"Your score is {count}.")

