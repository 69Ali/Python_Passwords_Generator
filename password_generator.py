import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbol=['!','@','#','$','%','^','&','*','(',')','_','+']
#Now we take some inputs from user for what type of password he wants.
print("Welcome to pypassword ganerator : ")
nbr_letters=int(input("How many number of letters you want in your password? \n"))
nbr_symbol=int(input(f"How many symbols you want in password? \n"))
nbr_numbers=int(input(f"How many numbers you want in your password? \n"))
password_list = []
#using for loop 
for char in range(1, nbr_letters + 1):
 password_list.append(random.choice(letters))

for char in range(1, nbr_symbol + 1 ):
    password_list += random.choice(symbol)

for char in range(1, nbr_numbers + 1):
    password_list += random.choice(numbers)
    print(password_list) 
    random.shuffle(password_list)
    print(password_list)  
    password = "" 
for char in password_list :
    password += char
    print(f"Your password is : {password} ")