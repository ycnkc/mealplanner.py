
print("""
                       _           _                                    
                      | |         | |                                   
  _  _  _    _   __,  | |      _  | |  __,   _  _    _  _    _   ,_     
 / |/ |/ |  |/  /  |  |/     |/ \_|/  /  |  / |/ |  / |/ |  |/  /  |    
   |  |  |_/|__/\_/|_/|__/   |__/ |__/\_/|_/  |  |_/  |  |_/|__/   |_/  
                            /|                                          
                            \|
""")
 
class Recipes:
    def __init__(self, type, name, diet):
        self.type = type
        self.name = name
        self.diet = diet


user_name = input("Welcome to your very own meal planner. What's your name? ")
print(user_name + " please answer some quick questions for me to create a special meal plan for you.")

print("How would you describe your eating habits?")
user_eating_habit = input("""Your choices are:
1. two meals a day(or IF)
2. three meals a day
3. three meals a day + a snack
(Please enter the number of your choice.)""")

