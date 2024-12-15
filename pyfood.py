import tkinter as tk
from tkinter import messagebox
import random

recipes = {
    'Dinner': {
        'Chicken Alfredo': {
            'ingredients': ['Chicken breast', 'Fettuccine pasta', 'Alfredo sauce', 'Parmesan cheese', 'Garlic', 'Butter'],
            'steps': [
                'Cook pasta according to package instructions.',
                'Grill chicken and slice it.',
                'Sauté garlic in butter, then add Alfredo sauce.',
                'Combine pasta, chicken, and sauce, and top with Parmesan.'
            ]
        },
        'Vegetarian Chili': {
            'ingredients': ['Kidney beans', 'Black beans', 'Tomatoes', 'Bell peppers', 'Onions', 'Garlic', 'Chili powder', 'Cumin', 'Olive oil'],
            'steps': [
                'Sauté chopped vegetables in olive oil.',
                'Add beans, tomatoes, chili powder, and cumin.',
                'Simmer for 30 minutes and serve with cornbread or rice.'
            ]
        },
        'Pork Stir-Fry': {
            'ingredients': ['Pork tenderloin', 'Bell peppers', 'Onions', 'Soy sauce', 'Sesame oil', 'Garlic', 'Ginger', 'Green onions'],
            'steps': [
                'Slice pork and stir-fry with vegetables.',
                'Add soy sauce, sesame oil, garlic, and ginger.',
                'Serve with steamed rice and garnish with green onions.'
            ]
        },
        'Lasagna': {
            'ingredients': ['Ground beef', 'Tomato sauce', 'Ricotta cheese', 'Mozzarella cheese', 'Lasagna noodles', 'Garlic', 'Onion'],
            'steps': [
                'Brown beef with garlic and onion.',
                'Layer noodles, sauce, ricotta, and mozzarella in a baking dish.',
                'Bake until golden and bubbly.'
            ]
        },
        'Fish Tacos': {
            'ingredients': ['White fish fillets', 'Taco seasoning', 'Tortillas', 'Cabbage', 'Salsa', 'Lime', 'Avocado'],
            'steps': [
                'Season and cook fish fillets.',
                'Prepare toppings: shredded cabbage, salsa, and sliced avocado.',
                'Assemble tacos with fish and toppings, serve with lime wedges.'
            ]
        }
    },
    'Breakfast': {
        'Avocado Toast': {
            'ingredients': ['2 slices of bread', '1 avocado', 'Lemon juice', 'Salt', 'Pepper', 'Chili flakes'],
            'steps': [
                'Toast the bread.',
                'Mash avocado with lemon juice, salt, and pepper.',
                'Spread on toast, sprinkle with chili flakes.'
            ]
        },
        'Chia Pudding': {
            'ingredients': ['Chia seeds', 'Almond milk', 'Honey', 'Vanilla extract', 'Fruit for topping'],
            'steps': [
                'Mix chia seeds with almond milk and honey.',
                'Refrigerate overnight.',
                'Top with fresh fruit in the morning.'
            ]
        },
        'Bagel with Cream Cheese and Smoked Salmon': {
            'ingredients': ['Bagel', 'Cream cheese', 'Smoked salmon', 'Capers', 'Red onion', 'Dill'],
            'steps': [
                'Toast the bagel.',
                'Spread cream cheese on both halves.',
                'Top with smoked salmon, capers, red onion, and dill.'
            ]
        },
        'Muesli': {
            'ingredients': ['Rolled oats', 'Yogurt', 'Almond milk', 'Dried fruit', 'Nuts', 'Honey'],
            'steps': [
                'Combine oats, yogurt, and almond milk.',
                'Let sit overnight in the fridge.',
                'Top with dried fruit and nuts in the morning.'
            ]
        },
        'Breakfast Burrito': {
            'ingredients': ['Scrambled eggs', 'Tortillas', 'Cheese', 'Sausage or bacon', 'Avocado', 'Salsa'],
            'steps': [
                'Cook scrambled eggs.',
                'Cook sausage or bacon.',
                'Assemble burrito with eggs, meat, cheese, avocado, and salsa.'
            ]
        }
    },
    'Dessert': {
        'Tiramisu': {
            'ingredients': ['Ladyfingers', 'Mascarpone cheese', 'Coffee', 'Cocoa powder', 'Eggs', 'Sugar', 'Heavy cream'],
            'steps': [
                'Dip ladyfingers in coffee and layer them in a dish.',
                'Mix mascarpone with eggs, sugar, and cream.',
                'Layer the mascarpone mixture over the ladyfingers, chill, and dust with cocoa powder.'
            ]
        },
        'Fruit Salad': {
            'ingredients': ['Mixed fruits (berries, melons, apples, etc.)', 'Honey', 'Mint'],
            'steps': [
                'Chop fruit into bite-sized pieces.',
                'Toss with honey and chopped mint.'
            ]
        },
        'Lemon Meringue Pie': {
            'ingredients': ['Pie crust', 'Lemons', 'Sugar', 'Eggs', 'Cornstarch', 'Butter', 'Cream of tartar'],
            'steps': [
                'Prepare lemon filling with lemon juice, sugar, eggs, and cornstarch.',
                'Pour into pie crust and bake.',
                'Top with meringue made from whipped egg whites and bake until golden.'
            ]
        },
        'Chocolate Mousse': {
            'ingredients': ['Dark chocolate', 'Heavy cream', 'Sugar', 'Vanilla extract', 'Eggs'],
            'steps': [
                'Melt chocolate and let it cool.',
                'Whip heavy cream with sugar and vanilla.',
                'Fold whipped cream into the chocolate mixture and chill until set.'
            ]
        },
        'Peach Cobbler': {
            'ingredients': ['Fresh peaches', 'Sugar', 'Butter', 'Flour', 'Baking powder', 'Milk'],
            'steps': [
                'Toss peaches with sugar and place in a baking dish.',
                'Mix flour, milk, and baking powder to create a batter.',
                'Pour batter over peaches and bake until golden.'
            ]
        }
    },
    'Drinks': {
        'Cucumber Mint Water': {
            'ingredients': ['Cucumber', 'Mint leaves', 'Water', 'Ice'],
            'steps': [
                'Slice cucumber and add to water with mint leaves.',
                'Serve with ice.'
            ]
        },
        'Green Smoothie': {
            'ingredients': ['Spinach', 'Banana', 'Almond milk', 'Chia seeds', 'Honey'],
            'steps': [
                'Blend spinach, banana, almond milk, chia seeds, and honey until smooth.'
            ]
        },
        'Iced Coffee': {
            'ingredients': ['Brewed coffee', 'Ice', 'Milk', 'Sugar', 'Vanilla extract'],
            'steps': [
                'Brew coffee and chill it.',
                'Pour over ice, add milk, sugar, and vanilla.'
            ]
        },
        'Hot Apple Cider': {
            'ingredients': ['Apple juice', 'Cinnamon sticks', 'Cloves', 'Orange zest'],
            'steps': [
                'Heat apple juice with cinnamon sticks, cloves, and orange zest.',
                'Simmer for 10 minutes and serve warm.'
            ]
        },
        'Pina Colada': {
            'ingredients': ['Pineapple juice', 'Coconut milk', 'Rum', 'Ice'],
            'steps': [
                'Blend pineapple juice, coconut milk, rum, and ice until smooth.'
            ]
        }
    },
    'Lunch': {
        'Grilled Chicken Caesar Wrap': {
            'ingredients': ['Grilled chicken', 'Caesar dressing', 'Lettuce', 'Parmesan cheese', 'Tortilla'],
            'steps': [
                'Grill chicken and slice.',
                'Toss chicken with Caesar dressing and lettuce.',
                'Wrap in tortilla with parmesan cheese.'
            ]
        },
        'Falafel Pita': {
            'ingredients': ['Falafel', 'Pita bread', 'Hummus', 'Cucumber', 'Tomato', 'Lettuce'],
            'steps': [
                'Prepare falafel or use premade.',
                'Fill pita with falafel, cucumber, tomato, lettuce, and hummus.'
            ]
        },
        'Chicken Caesar Salad': {
            'ingredients': ['Grilled chicken', 'Romaine lettuce', 'Caesar dressing', 'Croutons', 'Parmesan'],
            'steps': [
                'Grill chicken and slice.',
                'Toss with romaine lettuce, Caesar dressing, croutons, and parmesan.'
            ]
        },
        'Quinoa Salad': {
            'ingredients': ['Quinoa', 'Cucumber', 'Tomatoes', 'Feta cheese', 'Olive oil', 'Lemon juice'],
            'steps': [
                'Cook quinoa and cool.',
                'Mix with diced cucumber, tomatoes, feta, olive oil, and lemon juice.'
            ]
        },
        'Grilled Veggie Wrap': {
            'ingredients': ['Zucchini', 'Bell peppers', 'Mushrooms', 'Spinach', 'Hummus', 'Tortilla'],
            'steps': [
                'Grill vegetables.',
                'Spread hummus on a tortilla and add grilled veggies and spinach.'
            ]
        }
    }
}

def search_recipes_by_ingredient(ingredient):
    found = False
    result = ""
    for category, recipes_list in recipes.items():
        for recipe, details in recipes_list.items():
            if ingredient.lower() in [i.lower() for i in details['ingredients']]:
                result += f"\nRecipe: {recipe} (Category: {category})\n"
                result += "Ingredients: " + ", ".join(details['ingredients']) + "\n"
                result += "Steps:\n"
                for i, step in enumerate(details['steps'], 1):
                    result += f"{i}. {step}\n"
                result += "\n"
                found = True
    if not found:
        result = f"No recipes found with {ingredient}."
    return result

def random_recipe():
    category = random.choice(list(recipes.keys()))
    recipe = random.choice(list(recipes[category].keys()))
    details = recipes[category][recipe]
    
    result = f"\nRandom Recipe: {recipe} (Category: {category})\n"
    result += "Ingredients: " + ", ".join(details['ingredients']) + "\n"
    result += "Steps:\n"
    for i, step in enumerate(details['steps'], 1):
        result += f"{i}. {step}\n"
    
    return result

def display_recipes(category):
    if category in recipes:
        result = f"\n{category} Recipes:\n"
        for recipe, details in recipes[category].items():
            result += f"\n{recipe}:\n"
            result += "Ingredients: " + ", ".join(details['ingredients']) + "\n"
            result += "Steps:\n"
            for i, step in enumerate(details['steps'], 1):
                result += f"{i}. {step}\n"
        return result
    else:
        return "Category not found!"

def show_gui():

    root = tk.Tk()
    root.title("PyFood")

    root.iconbitmap('icon.png')

    def on_search_by_ingredient():
        ingredient = ingredient_entry.get()
        result = search_recipes_by_ingredient(ingredient)
        result_label.config(text=result)

    def on_random_recipe():
        result = random_recipe()
        result_label.config(text=result)

    def on_display_category():
        category = category_entry.get().capitalize()
        result = display_recipes(category)
        result_label.config(text=result)

    title_label = tk.Label(root, text="Welcome to PyFood!", font=("Arial", 16))
    title_label.pack(pady=10)

    ingredient_label = tk.Label(root, text="Enter an Ingredient to Search:")
    ingredient_label.pack()
    ingredient_entry = tk.Entry(root, width=30)
    ingredient_entry.pack(pady=5)
    search_button = tk.Button(root, text="Search Recipes", command=on_search_by_ingredient)
    search_button.pack(pady=5)

    category_label = tk.Label(root, text="Enter a Category (Dinner, Breakfast, Dessert, Drinks, Lunch):")
    category_label.pack()
    category_entry = tk.Entry(root, width=30)
    category_entry.pack(pady=5)
    category_button = tk.Button(root, text="Show Recipes", command=on_display_category)
    category_button.pack(pady=5)

    random_recipe_button = tk.Button(root, text="Get Random Recipe", command=on_random_recipe)
    random_recipe_button.pack(pady=10)

    result_label = tk.Label(root, text="", justify="left", font=("Arial", 10), padx=10, pady=10)
    result_label.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    show_gui()
      