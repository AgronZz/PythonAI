# fruits = ["apple","banana","cherry","date"] # krijojme nje list me stringje ne te  
# print(fruits)   #printojme listen te cilen e kemi ne variabel

# print("First fruit: ", fruits[0])   # printimi i elementit 0(te pare) te listes
# print("Last fruit: ", fruits[-1])   # printimi i elementit te fundit te listes

# fruits = ["apple","banana","cherry","date"] # lista me te dhenat
# fruits.append("elderberry") # bejme append me funksion
# fruits.remove("banana") # e heqim me funksion te cilen e shenojme emrin apo valuten
# print(fruits)


# fruits = ["apple","banana","cherry","date"] # lista me te dhenat
# search_fruit = input("Enter a fruit to search for: ") # japim input qe ta gjejme ne list
# if search_fruit in fruits:  # nese search_fruit(inputi i dhene) eshte tek lista fruits
#     print(f"{search_fruit} is in the list.") # ate her ajo eshte aty
# else:   # Nese jo ate her nuk eshte
#     print(f"{search_fruit} is not in the list")


# contacts = {                # krijojme nje dictionary
#     "Dea" : "123-456-789", # shenojme key dhe value 
#     "Marko" : "983-123-432",
#     "Charlie" : "124-423-547"
# }
# print(contacts) # printojme dictionaryn

# print("Dea's phone number: ", contacts["Dea"])  # printojme valuen e "Dea" 123 456 

#

# contacts = {                # krijojme nje dictionary
#     "Dea" : "123-456-789", # shenojme key dhe value 
#     "Marko" : "983-123-432",
#     "Charlie" : "124-423-547"
# }
# contacts["David"] = "223-244-546" # vendosim nje key me value ADD
# del contacts["Dea"] # e fshijme keyn e "Dea"
# print(contacts) # printojme key dhe values te dictionaryt



# contacts = {                # krijojme nje dictionary
#     "Dea" : "123-456-789", # shenojme key dhe value 
#     "Marko" : "983-123-432",
#     "Charlie" : "124-423-547"
# }
# search_name = input("Enter the name to search for: ") # japim input 

# if search_name in contacts: # e shikojme nese inputi qe e kemi dhene a eshte tek contacts
#     print(f"{search_name}'s phone number is {contacts[search_name]}")
# else:   # nese eshte printo emrin dhe valuen te keys nese jo at her else
#     print(f"{search_name} is not in the list.")


# inventory = ["milk","bread","eggs"]     # nje list me 3 items

# item = input("Enter an item to add.")   # japin input qe te bejme add
# inventory.append(item)      # e bejme append tek lista inputin item

# remove_item = input("Enter an item to remove: ")    # qe te bejme remove e japim nje input
# if remove_item in inventory:    # nese inputi te cilen e dham eshte ne inventory(lista)
#     inventory.remove(remove_item)   # ate her tek inventory me remove e fshijme remove item

# search_item = input("Enter an item search for: ")   # e bejme input ndonje search item
# if search_item in inventory:    # nese ne inventory ndodhet search_item ate her:
#     print(f"{search_item} is in stock.")    # printo qe eshte ne list(stock)
# else:
#     print(f"{search_item} is out of stock.")    # printo qe nuk eshte ne stock


# contacts = {}       # krijojme nje dictionary
# name = input("Enter the name: ")    # japim emrin e key ne input
# phone = input("Enter the phone number: ")   # japim numrin si value ne input
# contacts[name] = phone      # pastaj ketu i vendosim mbrenda contacts[name(inputi name)] 
#                             # dhe phone e lejme si value
# remove_name = input("Enter the name to remove: ") # sheno input per te fshir
# if remove_name in contacts:     # nese ekziston tek contacts inputi i dhene 
#     del contacts[remove_name]   # ate her fshij ate key me value

# search_name = input("Enter the name to search for: ")    # search_name ta gjejm ne dict
# if search_name in contacts:     # nese inputi i dhene eshte ne dictionart contacts
#     print(f"{search_name}'s phone number is {contacts[search_name]}")
# else:   # printo inputin e dhene dhe jep valuen e valuen e inputit
#     print(f"{search_name} is not in the contact list.") # nese jo ate her nuk ekziston



# list1 = ["Agron","Lebibe","Arita"]  # krijojme nje list me 3 items stringje

# search = input("Search a name to look at the list if there it is inside: ") 
# # krijojme nje input search te shohim nese a egziston ne list

# if search in list1: # e kontrollojme me if inputi(search) ne list1: ate her
#     print(f"The {search} is in the list1.") # printo se ekziston
# else:   # nese jo at her nuk egziston
#     print(f"{search} is not in the list1.")


# dict1 = {               # inicializpjme nje dictionary me key dhe valuess
#     "Agron" : 21,
#     "Lebibe" : 20,
#     "Arita" : 21
# }

# print(dict1["Agron"])       # printojme values te key's Agron
# print(dict1["Lebibe"])      # printojme values te key's Lebibes

tasks = [] # inicializojme nje list me emrin tasks
deadlines = {}  # inicializojme nje dictionary me emrin deadlines

task = input("Enter a task to add: ")   # japim input per taskun
deadline = input("Enter the deadline for that task: ")  # japim nje deadline per at task

tasks.append(task) # e bejme append tek lista taskun e dhene
deadlines[task] = deadline  # ndersa tek dict e bejme append taskun si key dhe deadline
                            # si value
remove_task = input("Enter a task to remove: ") # e japim nje input per ta fshir
if remove_task in tasks:        # nese egziston remove_task tek lista tasks
    tasks.remove(remove_task)   # ateher fshij ate task(remove_task)
    del deadlines[remove_task]  # the fshij tek deadlines ate task (remove_task)


search_task = input("Enter a task to search for: ") # search task input
if search_task in tasks:    # nese eshte ai tasku tek lista e tasks
    print(f"{search_task} is in your task list. Deadline: {deadlines[search_task]}")
else:   # printo se egziston the deadline eshte value e atij search_task(key)
    print(f"{search_task} is not on your list.")