#Cat Cafe

""" Japan is a cat island. And one of the restaurants there has a unique way of engagement
 where you can have chit-chats with the cats. What if we could make a python program for the
  restaurant? """

#TODO 1: PRESENTATION, WELCOMING THE CUSTOMERS

""" The characteristics of this welcome presentation are: 
    1- Greetings and the prompt ask for the customer's name.
    2- Then the customer will have a variety of options:
        a. ORDER FOOD AND BEVERAGES 
        b. MEET THE CATS
        c. STORE A TESTIMONY/RATINGS OF THE CUSTOMER'S EXPERIENCE
    3. An exit option if the customer is finished engaging with the prompt
"""

from options import Options
cats = {
        "Oreo":{
            "Breed":"Persian",
            "Weight":"8 kilograms",
            "Trait":"sleepy, tubby, lovely",
            "Furr Color": "White"
        },
        "Astro":{
            "Breed":"Persian",
            "Weight":"6 kilograms",
            "Trait":"playful, cheerful, naughty",
            "Furr Color":"Bluish Grey"
        }
}
money = 0 #income of the restaurant
opinions = []
def intro():
    name = input("Welcome to the CAT CAFE! May I have your name please?\n")
    print(f"Konichiwa! It's nice to meet you, {name} \n \n")




isOn = True
while isOn:
    intro()
    a = Options()
    optnum = int(input())

    if optnum == 1:
        a.food()
        num = int(input("Select the number of the menu: "))
        if num == 1:
            money += 10
        if num == 2:
            money += 20
        if num == 3:
            money += 30
        if num > 3:
            print("ERROR, RESTARTING")
            intro()

    if optnum == 2:
        print("Let's meet the cats! ")
        print(cats.items())

    if optnum == 3:
        print("Please give us your opinion...")
        customopi = input()
        opinions.append(customopi)
        print("Here are what other customers say about us: ")
        print(opinions)

    if optnum == 4:
        intro()

    if optnum > 4:
        print("ERROR, RESTARTING")
        intro()

    print(f"The restaurant's current income : {money} yen.")

