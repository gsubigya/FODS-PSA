'''
defining a Dish class and a Cookbook class to 
manage a collection of recipes using oop.
'''

class Dish:
    def __init__(self, dish_id, dish_name, ingredients, instructions):
        self.dish_id = dish_id
        self.dish_name = dish_name
        self.ingredients = ingredients
        self.instructions = instructions

    def display_dish(self):
        print(f"\nID: {self.dish_id} | Name: {self.dish_name}")
        print(f"Ingredients: {self.ingredients}")
        print(f"Instructions: {self.instructions}")

class Cookbook:
    def __init__(self):
        self.dishes = []

    def add_dish(self, dish):
        self.dishes.append(dish)
        print(f"Dish '{dish.dish_name}' kept to the cookbook.")

    def show_all_dishes(self):
        if not self.dishes:
            print("The cookbook is empty.")
        else:
            print("\n--- My Recipes ---")
            for dish in self.dishes:
                dish.display_dish()

#executing
if __name__ == "__main__":
    my_cookbook = Cookbook()
    
    # Adding a sample
    d1 = Dish(101, "Selroti", "Flour, Sugar, Oil/Ghee", "Make smooth flour batter, mix sugar, water, oil to meet consistency, deep fry in oil until golden brown.")
    my_cookbook.add_dish(d1)
    
    my_cookbook.show_all_dishes()