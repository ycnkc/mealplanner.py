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
 

        

a1 = Recipes("breakfast", ["vegetarian", "low carb"], breakfast_recipes.get("Cottage Cheese Pancakes"))
b1 = Recipes("breakfast", ["vegetarian"], breakfast_recipes.get("Carrot Cake Oatmeal"))
c1 = Recipes("breakfast", ["vegetarian", "vegan"], breakfast_recipes.get("Strawberry Cheesecake Overnight Oats"))
d1 = Recipes("breakfast", ["high protein", "low carb"], breakfast_recipes.get("Pizza Omelet"))
e1 = Recipes("breakfast", ["vegetarian", "vegan"], breakfast_recipes.get("Apple Pie Granola"))

a2 = Recipes("main", ["high protein", "low carb"], main_dishes.get("Teriyaki Meatballs"))
b2 = Recipes("main", ["vegetarian", "vegan"], main_dishes.get("Gochujang Mac and Cheese"))
c2 = Recipes("main", ["low carb", "high protein"], main_dishes.get("Chicken Lo Mein"))
d2 = Recipes("main", ["high protein"], main_dishes.get("Chicken Fried Rice"))
e2 = Recipes("main", ["vegan"], main_dishes.get("Spaghetti Puttanesca"))

a3 = Recipes("snack", ["high protein", "vegan"], snacks.get("Peanut Butter Choc Chip Protein Balls"))


user_name = input("Welcome to your meal planner. What's your name? ")
print(user_name + " please answer some quick questions for me to create a special meal plan for you.")
print("---------------------------------------------------")
print("How would you describe your eating habits?")
user_eating_habit = input("""Your choices are:
1. two meals a day(or IF)
2. three meals a day
3. three meals a day + a snack
(Please enter the number of your choice.) """)
print("---------------------------------------------------")
print("Do you have a special diet?")
user_diet = input("(vegan, vegetarian, low carb, high protein, no diet) ")
print("---------------------------------------------------")

if user_eating_habit == "1" and user_diet == "vegan":
    print("▸BREAKFAST")
    print("---------------------------------------------------")
    random_vegan_breakfast = get_random_recipe("vegan", "breakfast")
    print(random_vegan_breakfast)
    print("---------------------------------------------------")
    print("▸DINNER")
    print("---------------------------------------------------")
    random_vegan_main = get_random_recipe("vegan", "main")
    print(random_vegan_main)


 
 

 


      






   

            

   


      
         
      

