class Recipe:
    def __init__(self, recipe_name, ingredients, instructions):
        self.recipe_name = recipe_name
        self.ingredients = ingredients
        self.instructions = instructions

class RecipeEncoder:
    def default(self, o):
        return o.__dict__
