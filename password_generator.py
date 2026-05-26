import random
print("Hello this ia a Password Generator Program\nin this program Computer will be generate a Random Password for User."); 


user = int(input("Choose a Length of Password: ")); 

smallletter = "abcdefghijklmnopqrstuvwxyz"; 
capitalletter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"; 
number = "0123456789"; 
specialchar = "@#$"; 

combine = smallletter + capitalletter + number + specialchar; 
password = (""); 
for i in range(user): # User jitni Length dega utni br chlega 
 computer = random.choice(combine); 
 password = password + computer; 
print("Password: " , password); 