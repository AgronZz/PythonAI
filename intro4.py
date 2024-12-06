# def greet():            # Krijojme funksion pa parameter
#     print("Hello, Welcome to AI CLASS!")    # nje print ne funksion

# greet() # therrasim funksionin

# def greet(name):    # krijojme funksion me parameter
#     print(f"Hello, {name}! Welcome to AI class.")   # parametrin e funksionit e shtijm ne print

# greet("Agron")  # e thirim funksionin me parametrin AGron


# def add_numbers(a,b):   # krijojme funksion me dy parametra
#     return a + b    # dy parametrat i mbledhim dhe i kthejm return

# result = add_numbers(5,3)   # i japim ne nje variabel result
# print(result)   # e bejme print resultatin


# def check_weather(weather): # funksion me parametrin weather te cilen e japim si input
#     if weather == "rainy":  # nese eshte rainy at her
#         return "Take an umbrella."  # ben return se te duhet ombrell
#     else:   # nese nuk eshte rainy at her kthe no need 
#         return "No need for an umbrella."
    
# current_weather = input("What's the weather like? ").lower()    # inputin e bejme me lower
# print(check_weather(current_weather))   # ket input e japim si parameter te funksionit
#                                         # the e therrasim

def decide_activity(time_of_day, weather):  # funksion me dy parametra
    if time_of_day == "morning" and weather == "sunny": # perdorim and operator
        return "Go for a walk."                         # sepse and duhet dyja te sakta
    elif time_of_day == "morning" and weather == "rainy":   # dyjat te plotsojne kushtin
        return "Read a book."
    elif time_of_day == "afternoon" and weather == "sunny":
        return "Play outside."
    elif time_of_day == "afternoon" and weather == "rainy":
        return "Watch a movie"
    else:
        return "No activity suggestion available."
    

time_of_day = input("What time of day is it? (morning or afternoon)")
weather = input("Whats the weather? rainy or sunny ")
print(decide_activity(time_of_day,weather)) # bejme dy inpute the dyjat i japim si parametra
