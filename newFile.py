# weather = input("Enyer the weather (sunny,rainy,snowy): ")  
# # japim variabel me input me 3 zgjedhje.
# if weather == "sunny":  # if statement, nese eshte variabla sunny
#     print("AI Suggestion: It's sunny, go for a walk!")  # ate her printo kete
# elif weather == "rainy":    # nese jo elif, rainy ate her printo kete
#     print("AI Suggestion: It's rainy, stay indoors and read a book")
# elif weather == "snowy":    # nese as rainy a eshte snowy?
#     print("AI Suggestion: It's snowy, build a snowman!")    # printo kete
# else:   # nese nuk eshte as njera pergjigje printo kete te funden else
#     print("AI Suggestion: I don't know this weather condition.")


# for i in range(1,6): # for cikel nga numri 1 deri ne numer 5 pasi nuk shkon te 6ta
#     print(f"AI Count: Person {i} has entered the store.") 
#     # e printon me f" " gje qe na lejon te perdorim brenda variabla me kllapa gjarperore

# age = -1    # inicializojme age = -1
# while age < 0:  # nese age eshte me madhe se 0 ateher mbaro cikelin
#     age = int(input("Please enter a valid age (positive number): "))
#     # nese jo ateher derisa te jep numer pozitiv mos dil nga cikli!

# print(f"AI: Thank you! Your age is {age}") # e printojme brenda ne print var


# time_of_day = input("What time of day is it (morning, afternoon, evening)? ")
# temperature = int(input("What's the temperature? "))
# hungry = input("Are you hunry (yes/no)? ")
# # japim 3 inpute 2 nga to normal 1 me integjer(pateter numer)
# # i krahasojme me if, dhe me operator and qe do te thot patjeter te jen te sakta
# if time_of_day == "morning" and temperature > 20 and hungry == "yes":
#     print("AI Suggestion: Make breakfast and eat it outside!")
# elif time_of_day == "afternoon" and hungry == "no":
#     print("AI SUggestion: It's a good time to work or relax.")
# else:
#     print("AI Suggestion: No specific advice for this situation.")


# number = int(input("Write a number to check if its odd or even: ")) 
# # input me integjer patjeter ku bejme if else qe ta gjenerojme cift apo tek
# if number % 2 == 0: # nese variabla nuk ka mbetje 
#     print(f"The {number} is even number.")  # ateher eshte cift
# else:
#     print(f"The {number} is odd number.")   # nese ka mbetje at her eshte tek

print("With While loop: ") # printimi me while loop per te gjeneruar nga 1 - 10

number = 0 # inicializojme variablen number me 0

while number < 11:  # perderisa variabla te arrin numrin me e madhe se 11 mos te ndalon
    print(number)   # e printojme numrin sa her qe bon ciklet
    number += 1     # e risim per 1 gjdo her per gjdo cikel qe kalon

print("With For loop:") # me for loop

for i in range(1,11):   # for cikel nga 1 deri tek 11 qe nuk mbrin 11 
    print(i)