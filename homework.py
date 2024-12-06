# print("Hello, Ai World!") # Ketu me komanden print e printon kodin



# age = 20        # inicializojm variable age me vler 20

# name = "Alice"  # inicializojm variable me emrin name 

# print("Name: ", name)    # e printojme ne output emrin Name: me variablen
# print("Age: ", age)     #e printojm age me variablen te cilen e kemi dhene


# x = 10  # e inicializojme  variablen x me vlere 10
# y = 5   # inicializojme variablen y me vlere 5

# sum = x + y # i mbledhim me variablen x dhe y dhe i vejme store te variabla e re sum

# print("Sum: ", sum) # e printojme variablen te cilen e kemi bere sum


# name = input("Enter your name: ")   # marim input me variablen name te cilen e japim me tastier
# print("Hello ", name)      # e printojme variablen name te cilen e kemi shtyp


# number = int(input("Enter a number: ")) # marim nje variabel me input integjer
# if number > 0:                          # nese variabla me numer eshte me e madhe 
#     print("The number is positive.")    # 0 ather printo this number is positive
                                       

# number = int(input("Enter a number: ")) # variable me int me input
# if number > 0:  # if statement, nese variabla number me e madhe se 0
#     print("The number is positive.")    # ather printo eshte pozitive
# else:                               # nese jo(else) printo jo pozitive
#     print("The number is not positive.")


# number = int(input("Enter a number: "))     # variable te cilen e konvertojme ne int me input
# if number > 0:     # if statement, nese numri me i madh se 0
#     print("Number is positive.")    # printo pozitiv
# elif number == 0:       # elif statement nese numri i barabart me zero
#     print("The number is zero.")    # printo numri i barabart me zero
# else:       # nese asnjera nga keto nuk permbushet printo
#     print("Number is negative.")    # numri eshte negative


# for i in range(1,6):   # for i in range, for cikel te cilen printon nga 1 deri 5
#     print(i)    #printo i te cilen kapercen ne cikel 

# number = -1     # variablen e inicializojme me numrin -1

# while number <= 0:  # nese numri eshte me e madhe ose e barabart me zero
#     number = int(input("Enter a positive number: "))  # permbushet cikli
# print("Thank you.") # nese jo ate her deri sa te printohet numer pozitiv ose 0
#                     # do te jet ne cikel

# numbers = [1,2,3,4,5]   # array te cilen kemi numrat 1,2,3,4,5

# for number in numbers:  # for cikel, per number ne numbers(inside)
#     print(number)   # printo number


# ai_terms = ["Machine learning","Neural Networks","Data","Model"]
# # nje array me stringje
# for term in ai_terms:   # for cikel te cilet per term ne ai_terms
#     print(term)         # printo termet


# ai_terms = []   # krijojme nje array te zbrazur
# for i in range(3):  # for cikel deri ne rangje 3 her (3 cikle)
#     term = input("Enter an AI term: ")  # bejme input me variable term
#     ai_terms.append(term)       # me funksionin append ne arrayn bejme termet append

# print("Ai terms: ",ai_terms)    # printojme arrayn e mbushur 3 her me append


# with open("data.txt", "r") as file: # with open hapim data.txt filen me "r" read
#     data = file.read()              # si file, dhe e bejme read me funksion

# print(data)         # me variablen te cilen e kemi bo store e bejme print


# with open("data.txt", "r") as file:     # e hapim filen data.txt ne read si file
#     data = file.read()          # e lexojme me funksionin dhe e bejme store ne data

# words = data.split()  # e bejme split fjalt ne nje variable tjt te quajtur words
# print("Number of words: ", len(words)) # pastaj me funksionin len(length) i numerojme


# with open("data.txt", "r") as file: # hapim filen data.txt si read file
#     data = file.read()  # e lexojme me funksionin read ne nje variable tjt

# count = data.count("AI")    # e bejme count mbrenda shkronjen "AI" sa her ne eshte paraqit
# print("The word 'AI' appears", count , "times.")    # e printojme counterin.


# def greet(name):        # bejme funksion me parameter name
#     print("Hello,", name,"!") # e perdorim parametrin qe e kemi vendos te funksioni

# greet("Agron")  # e therrasim funksionin me parametrin "Agron"


# def square(num):    # bejme funksion me parameter
#     return num * num    # parametrin e dhene e bejme * me veten e vet dy her

# result = square(5)      # e therrasim funksionin dhe e inicializojme vleren
#                         # ne variabel tjt
# print("Square: ", result)   # variablen tjt e therasim te cilen e kemi rezultatin


# import math     # importojme librarin math te cilen e ka pythoni

# print("Square root of 25 is: ", math.sqrt(25))  # e perdromi funksionin e libraris
#                                                 # square root me numrin 25
# import numpy as np  # e importojme librarin numpy me shkurtesen as np

# array = np.array([1,2,3,4,5])   # e therrasim librarin me funksionin e tij per array
# print("Numpy Array: ", array)   # e bejme print
# print("Array multiplied by 2: ", array * 2) # e bejme print duke u shumezuar me 2


# import random   # importojme librarin random

# decision = random.choice(["Yes","No"]) # bejme nje random chocice te na gjeneron
#                                         # fjalit Yes apo No njeren prej tyre.
# print("AI decision is: ",decision," (Yes/No)")  # variablen te cilen e kemi bere store e printojmeS


import random as rn  # importojme librarin random

decision = rn.choice(["Yes","No","Maybe"]) # japim 3 choices
print("AI decision: ", decision)        # e printojme rezultatin e dhene nga random




