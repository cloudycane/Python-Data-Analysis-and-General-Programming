""" OOP class where the customer can select from the class options"""


class Options():

    """--init--"""
    def __init__(self):
        print("Here are the options, please select the number: ")
        print(""" 
            Option 1 - Buy food and drinks! 
            Option 2 - Meet and greet with the cats!
            Option 3 - Give us an opinion! 
            Option 4 - Exit the application 
              """)

    def food(self):
            print("""
                        Select the menu you want: 
                        Menu 1 - Fries, Burgers, plus unlimited drinks --- Price : 10.00
                        Menu 2 - Ramen, sushi, bentos, plus unlimited drinks --- Price: 20.00
                        Menu 3 - Japanese seafoods, salads, plus unlimited drinks --- Price: 30.00


                        """)


