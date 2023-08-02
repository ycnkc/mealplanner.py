import random
print("""
                       _           _                                    
                      | |         | |                                   
  _  _  _    _   __,  | |      _  | |  __,   _  _    _  _    _   ,_     
 / |/ |/ |  |/  /  |  |/     |/ \_|/  /  |  / |/ |  / |/ |  |/  /  |    
   |  |  |_/|__/\_/|_/|__/   |__/ |__/\_/|_/  |  |_/  |  |_/|__/   |_/  
                            /|                                          
                            \|
""")

with open("recipes.py") as recipes:
   from recipes import breakfast_recipes
   from recipes import main_dishes
   from recipes import snacks

   class Recipes:
    all_recipes = []
    

    def __init__(self,type, diet, recipe):
        self.type = type
        self.diet = diet 
        self.recipe = recipe 
        __class__.all_recipes.append(self)
           
    def __repr__(self):
        return "{recipe}.".format(recipe=self.recipe)
    
    def is_vegan(self):
       if self.diet == "vegan":
          return self
       
def get_random_recipe(diet, type):
   filtered_recipes = [recipe for recipe in Recipes.all_recipes if diet in recipe.diet and recipe.type == type]
   return random.choice(filtered_recipes).recipe
 

        

a1 = Recipes("breakfast", ["vegetarian", "low carb", "no diet"], breakfast_recipes.get("Cottage Cheese Pancakes"))
b1 = Recipes("breakfast", ["vegetarian", "no diet"], breakfast_recipes.get("Carrot Cake Oatmeal"))
c1 = Recipes("breakfast", ["vegetarian", "vegan", "no diet"], breakfast_recipes.get("Strawberry Cheesecake Overnight Oats"))
d1 = Recipes("breakfast", ["high protein", "low carb", "no diet"], breakfast_recipes.get("Pizza Omelet"))
e1 = Recipes("breakfast", ["vegetarian", "vegan","no diet"], breakfast_recipes.get("Apple Pie Granola"))

a2 = Recipes("main", ["high protein", "low carb","no diet"], main_dishes.get("Teriyaki Meatballs"))
b2 = Recipes("main", ["vegetarian", "vegan","no diet"], main_dishes.get("Gochujang Mac and Cheese"))
c2 = Recipes("main", ["low carb", "high protein","no diet"], main_dishes.get("Chicken Lo Mein"))
d2 = Recipes("main", ["high protein","no diet"], main_dishes.get("Chicken Fried Rice"))
e2 = Recipes("main", ["no diet"], main_dishes.get("Spaghetti Puttanesca"))
f2 = Recipes("main", ["vegan", "vegetarian", "no diet"], main_dishes.get("Microwave Baked Potato"))

a3 = Recipes("snack", ["high protein", "vegan", "no diet"], snacks.get("Peanut Butter Choc Chip Protein Balls"))
b3 = Recipes("snack", ["vegan", "vegetarian","no diet"], snacks.get("Healthy Chocolate Cupcakes"))
c3 = Recipes("snack", ["vegetarian", "vegan", "high protein"], snacks.get("Cinnamon Raisin Protein Balls"))
c4 = Recipes("snack", ["low carb", "no diet"], snacks.get("Pizza Zucchini Bites"))

user_name = input("Welcome to your meal planner. What's your name? ")
print(user_name + ", please answer some quick questions for me to create a special meal plan for you.")
print("------------------------------------------------------------------------")
print("How would you describe your eating habits?")
user_eating_habit = input("""Your choices are:
1. two meals a day(or IF)
2. three meals a day
3. three meals a day + a snack
(Please enter the number of your choice.) """)
print("------------------------------------------------------------------------")
print("Do you have a special diet?")
user_diet = input("(vegan, vegetarian, low carb, high protein, no diet) ")
print("------------------------------------------------------------------------")

meal_options = [
    ("vegan", "breakfast"),
    ("vegan", "main"),
    ("vegetarian", "breakfast"),
    ("vegetarian", "main"),
    ("low carb", "breakfast"),
    ("low carb", "main"),
    ("high protein", "breakfast"),
    ("high protein", "main"),
    ("no diet", "breakfast"),
    ("no diet", "main")
]

print("Here's your customized meal plan: \n")
if user_eating_habit == "1" and user_diet in ["vegan", "vegetarian", "low carb", "high protein", "no diet"]:
    for diet, meal_type in meal_options:
        if user_diet == diet:
            print("▸" + meal_type.upper())
            print("------------------------------------------------------------------------")
            print(get_random_recipe(diet, meal_type))
            print("------------------------------------------------------------------------")

elif user_eating_habit == "2" and user_diet in ["vegan", "vegetarian", "low carb", "high protein", "no diet"]:
    breakfast_recipe = get_random_recipe(user_diet, "breakfast")
    lunch_recipe = get_random_recipe(user_diet, "main")
    dinner_recipe = get_random_recipe(user_diet, "main")

    print("▸BREAKFAST")
    print("------------------------------------------------------------------------")
    print(breakfast_recipe)
    print("------------------------------------------------------------------------")

    print("▸LUNCH")
    print("------------------------------------------------------------------------")
    print(lunch_recipe)
    print("------------------------------------------------------------------------")

    print("▸DINNER")
    print("------------------------------------------------------------------------")
    print(dinner_recipe)
    print("------------------------------------------------------------------------")

elif user_eating_habit == "3" and user_diet in ["vegan", "vegetarian", "low carb", "high protein", "no diet"]:
    breakfast_recipe = get_random_recipe(user_diet, "breakfast")
    lunch_recipe = get_random_recipe(user_diet, "main")
    dinner_recipe = get_random_recipe(user_diet, "main")
    snack_recipe = get_random_recipe(user_diet, "snack")

    print("▸BREAKFAST")
    print("------------------------------------------------------------------------")
    print(breakfast_recipe)
    print("------------------------------------------------------------------------")

    print("▸LUNCH")
    print("------------------------------------------------------------------------")
    print(lunch_recipe)
    print("------------------------------------------------------------------------")

    print("▸DINNER")
    print("------------------------------------------------------------------------")
    print(dinner_recipe)
    print("------------------------------------------------------------------------")

    print("▸SNACK")
    print("------------------------------------------------------------------------")
    print(snack_recipe)
    print("------------------------------------------------------------------------")

else:
   print("You may have entered some unrelated info. Please try again.")
 
 

 


      






   

            

   


      
         
      

