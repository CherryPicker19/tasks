class Ingredient:
    def __init__(self, name: str, volume: int, measure: str):
        self.name = name
        self.volume = volume
        self.measure = measure

    def __str__(self):
        return f"{self.name}: {self.volume}, {self.measure}"

class Recipe:
    def __init__(self):
        self.ingredients = []

    def __len__(self):
        return len(self.ingredients)

    def __str__(self):
        ing1 = []
        for i in self.ingredients:
            ing1.append(i.__str__())
        return str(ing1)

    def add_ingredient(self, ing: Ingredient):
        self.ingredients.append(ing)

    def remove_ingredient(self, ing: Ingredient):
        self.ingredients.remove(ing)

    def get_ingredients(self):
        return tuple(self.ingredients)



recipe = Recipe()
recipe.add_ingredient(Ingredient("Salt", 1, "tea_spoon"))
recipe.add_ingredient(Ingredient("Salt", 1, "tea_spoon"))
recipe.add_ingredient(Ingredient("Salt", 1, "tea_spoon"))
print(recipe)
a = Ingredient("Sugar", 10, "tea_spoon")
print(a)