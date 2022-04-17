""" import os 
def clear_console():
    

cookie_in_jar = 0
while cookie_in_jar < 100 :
 added_cookies = input("How many cookies to add in the jar ? ")
 clear_console()
 total = int(cookie_in_jar) + int(added_cookies)
 if total < 100:
    cookie_in_jar = int(cookie_in_jar) + int(added_cookies)
    print( "Hi, there are " + str(cookie_in_jar) + " cookies in the jar" )
 else:
    print("you try to put to many cookies, jar can contain only one hundred")
    break

"""
import random
import os 
goal = random.randint(0,50)
total=0 
print("Ton bocal peut contenir",goal, " cookies")
while total< goal:
 number_user= int(input("Tu veux ajouter combien de cookies ?"))
 for ajout in range (number_user):
        total += 1 
 os.system('clear')
 print("Ton bocal peut contenir",goal, " cookies")
 print("il y a ",total," cookies dedans")
print("trop de cookies, ca deborde")


 







