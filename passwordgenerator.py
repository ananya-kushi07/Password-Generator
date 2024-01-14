# usage ascii art
import random
logo='''                                           _                                    _             
                                          | |                                  | |            
 _ __   __ _ ___ _____      _____  _ __ __| |    __ _  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
| '_ \ / _` / __/ __\ \ /\ / / _ \| '__/ _` |   / _` |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
| |_) | (_| \__ \__ \\ V  V / (_) | | | (_| |  | (_| |  __/ | | |  __/ | | (_| | || (_) | |   
| .__/ \__,_|___/___/ \_/\_/ \___/|_|  \__,_|   \__, |\___|_| |_|\___|_|  \__,_|\__\___/|_|   
| |                                              __/ |                                        
|_|                                             |___/                                   '''

print(logo)

length=int(input("what should be the length of your password? :"))
alpha_list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
num_list=['0','1','2','3','4','5','6','7','8','9']
spl_list=['@','%','!','^','&','*','$','#']
letter=int(input("How many letters you need? :"))
number=int(input("How many numbers you need? :"))
splchar=int(input("How many special characters you need? :"))

#numberss=random.randint(1,40)
password_list=[]

for i in range(1,number+1):     # inside for loop give printing variable
    password_list.append(random.choice(num_list))     #give list name

for i in range(1,letter + 1):
    password_list.append(random.choice(alpha_list))

for i in range(1,splchar + 1):
    password_list.append(random.choice(spl_list))

random.shuffle(password_list)
result=""

for i in password_list:
    result+=i

print(f"Your password is {result} :")