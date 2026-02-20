# Exercise 1.7 Task
# Recipe Application with SQLAlchemy ORM and MySQL Database

# ====== IMPORTS ======
# Import necessary SQLAlchemy components
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import sessionmaker

# ====== DATABASE SETUP ======
# Create an engine and a session to interact with the MySQL database
engine = create_engine("mysql+pymysql://cf-python:75-Graffiti@localhost/recipes_db")
Session = sessionmaker(bind=engine)
session = Session()

# Create a base class for declarative class definitions
Base = declarative_base()

# ====== CLASS DEFINITION ======
# Define the Recipe class mapped to the recipes table
class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    # Simple string representation of the Recipe object
    def __repr__(self):
        return (f"\tRecipe ID: {self.id} | {self.name} | Difficulty: {self.difficulty}")
    
    # Detailed string representation of the Recipe object
    def __str__(self):
        return (f"Recipe Name: {self.name}\n"
                f"\tCooking Time: {self.cooking_time} minutes\n"
                f"\tIngredients: {self.ingredients}\n"
                f"\tDifficulty: {self.difficulty}\n")
    
    # Method to return ingredients as a list
    def return_ingredients_as_list(self):
        if self.ingredients is None or self.ingredients.strip() == "":
            return []
        return self.ingredients.split(', ')

    # Method to calculate the difficulty level based on cooking time and number of ingredients
    def calculate_difficulty(self):
        num_ingredients = len(self.return_ingredients_as_list())
        if self.cooking_time < 10:                   # Cooking time less than 10 minutes
            difficulty = 'Easy' if num_ingredients < 4 else 'Medium'
        else:                                        # Cooking time 10 minutes or more
            difficulty = 'Intermediate' if num_ingredients < 4 else 'Hard'
        self.difficulty = difficulty

# ====== FUNCTION DEFINITIONS ======
# Function to get a recipe name from user input (with validation)
def get_recipe_name(current_name=None):
    while True:
        name = input("Enter the recipe name: ").strip()

        # If updating and the user enters the same name, just return it
        if current_name and name == current_name:
            return name
        
        # 1. Length Validation
        if len(name) > 50 or len(name) == 0:
            print("Name must be between 1 and 50 characters.")
            continue
        # 2. Character Validation (alphanumeric + spaces)
        if not name.replace(' ', '').isalnum():
            print("Name must be alphanumeric (spaces allowed).")
            continue
        # 3. Duplicate Check
        exists = session.query(Recipe).filter(Recipe.name == name).first()
        if exists:
            print(f"A recipe named '{name}' already exists. Please choose a different name.")
            continue
            
        return name

# Function to get a cooking time from user input (with validation)
def get_cooking_time():
    while True:
        time_input = input("Enter the cooking time (in minutes): ").strip()
        # 1. Numeric Validation
        if not time_input.isnumeric():
            print("Invalid input. Please enter a number.")
            continue
        # 2. Positive Value Check    
        time = int(time_input)
        if time <= 0:
            print("Cooking time must be greater than zero.")
            continue
            
        return time

# Function to get ingredients from user input (with validation)
def get_ingredients():
    while True:
        ingredients_list = []
        n_input = input("Enter the number of ingredients: ").strip()
        
        if not n_input.isnumeric() or int(n_input) <= 0:
            print("Please enter a positive number.")
            continue
        
        for i in range(int(n_input)):
            ing = input(f"Enter ingredient {i + 1}: ").strip().lower()
            # Validation: letters and spaces only
            if ing and ing.replace(' ', '').isalpha():
                ingredients_list.append(ing)
            else:
                print("Invalid ingredient. Use letters and spaces only.")
                break # Restarts the whole ingredient process
        
        # Ensure the loop finished for all ingredients
        if len(ingredients_list) == int(n_input):
            ingredients_string = ", ".join(ingredients_list)    # Convert to a comma-separated string
            return ingredients_string

# Function to select a recipe from the database by ID
def select_recipe_from_list():
    # 1. Fetch all recipes to see if there's anything to search
    results = session.query(Recipe).all()
    if not results:
        print("No recipes found in the database.")
        return None

    # 2. Display existing recipes
    print("\nExisting recipes in the database:")
    for row in results:
        print(repr(row))

    # 3. Selection loop
    while True:
        recipe_id_input = input("\nEnter the recipe ID to select: ").strip()
        # Numeric Validation
        if not recipe_id_input.isnumeric():
            print("Invalid input. Numeric value expected.")
            continue
        # Fetch the selected recipe
        selected_recipe = session.get(Recipe, int(recipe_id_input))
        # Existence validation
        if not selected_recipe:
            print("Recipe not found. Please enter a valid recipe ID.")
            continue
        
        return selected_recipe

# Function to create and store a new recipe in the database
def create_recipe():
    name = get_recipe_name()            # Input recipe name
    cooking_time = get_cooking_time()   # Input cooking time
    ingredients = get_ingredients()     # Input ingredients

    # Insert the new recipe into the database
    # Initialize Recipe object without difficulty level
    recipe_entry = Recipe(
        name=name,
        ingredients=ingredients,
        cooking_time=cooking_time
    )
    # Calculate difficulty level using the class method
    recipe_entry.calculate_difficulty()
    # Save the new recipe to the database
    try:
        session.add(recipe_entry)
        session.commit()
        print(f"\nRecipe '{name}' added successfully!\n")
    except Exception as e:
        session.rollback()                   # Rollback in case of error
        print(f"Error occurred while adding the recipe. Changes are rolled back: {e}.")

# Function to display a list of all recipes in the database
def view_all_recipes():
    recipes_list = session.query(Recipe).all()
    # Display recipes list
    if recipes_list:
        print("\nAll recipes from the database:" + "\n" + "-"*80)
        for recipe in recipes_list:
            print(recipe)
    else:
        print("No recipes found in the database.")
        return None

# Function to search for a recipe by ingredient
def search_recipe():
    # Fetch all ingredients from the database
    results = session.query(Recipe.ingredients).filter(
        Recipe.ingredients.is_not(None), Recipe.ingredients != ''
    ).all()
    # Check if there are any recipes in the database
    if not results:
        print("No recipes with ingredients found in the database.")
        return
    
    # Build a list of all unique ingredients from the database
    all_ingredients = []         # List of all unique ingredients
    all_ingredients_set = set()  # Temporary set to track unique ingredients

    for row in results:
        if row.ingredients is None or row.ingredients.strip() == "":
            continue
        parts = row.ingredients.split(', ')
        all_ingredients_set.update(parts)           # Add not present unique ingredients to the set
    all_ingredients = sorted(all_ingredients_set)   # Convert set to a sorted list

    # Display ingredient search menu
    print("Available ingredients to search for:")
    for i, ingredient in enumerate(all_ingredients, start=1):
        print(f"{i}. {ingredient}")
    
    # Prompt user to enter ingredient numbers separated by spaces
    selection = input("Enter ingredient numbers to search for (separated by spaces): ").strip()
    if not selection:
        print("No input provided. Exiting search.")
        return
    try:
        selected_numbers = [int(num) for num in selection.split()]
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return
    
    # Validate all selected numbers
    if not all(1 <= num <= len(all_ingredients) for num in selected_numbers):
        print("One or more selected numbers are out of range. Exiting search.")
        return
    
    # Build search_ingredients set
    search_ingredients = {all_ingredients[num-1] for num in selected_numbers}
    # Build filter conditions for each selected ingredient
    conditions = []
    for ingredient in search_ingredients:
        conditions.append(Recipe.ingredients.like(f"%{ingredient}%"))   

    # Retrieve recipes containing all selected ingredients
    print(f"\nRecipes containing ingredients: {', '.join(search_ingredients)}") # Header
    print("-" * 80)
    # Matching recipes display
    results = session.query(Recipe).filter(*conditions).all()
    if results:
        for row in results:
            print(row)
    else:
        print(f"No recipes found containing {', '.join(search_ingredients)}.")

# Function to update an existing recipe in the database
def update_recipe():
    # Prompt user to select a recipe to update
    recipe_to_edit = select_recipe_from_list()
    # If no recipe selected, exit the function
    if not recipe_to_edit:
        return

    # Prompt user for columns to update
    print(f'''Which columns would you like to update?
    You can update one or several columns:
        (1) Name: {recipe_to_edit.name}
        (2) Ingredients: {recipe_to_edit.ingredients}
        (3) Cooking time: {recipe_to_edit.cooking_time}
    Difficulty will be recalculated automatically after any change.''')
    while True:
        columns_input = input("Selection (example: 1,3): ").strip()
        columns_to_update = [col.strip() for col in columns_input.split(',') if col.strip()]
        if not columns_to_update:
            print("Input cannot be empty. Please enter 1, 2, or 3, separated by commas.")
            continue
        if not set(columns_to_update).issubset({'1', '2', '3'}):
            print("Only 1, 2, or 3 are allowed. Please try again.")
            continue
        if len(set(columns_to_update)) != len(columns_to_update):
            print("Duplicate columns are not allowed. Please try again.")
            continue
        break

    # Update local variables based on choice with input validation
    if '1' in columns_to_update:
        # Pass the current name so the helper function knows it's okay to reuse it
        recipe_to_edit.name = get_recipe_name(recipe_to_edit.name)
    if '2' in columns_to_update:
        recipe_to_edit.ingredients = get_ingredients()
    if '3' in columns_to_update:
        recipe_to_edit.cooking_time = get_cooking_time()

    # Automatically recalculate difficulty using the class method
    # This ensures the difficulty column stays in sync with changes
    recipe_to_edit.calculate_difficulty()

# SQLAlchemy tracks these changes. Calling commit sends the UPDATE SQL.
    try:
        session.commit()
        print(f"Recipe ID '{recipe_to_edit.id}' updated successfully!")
    except Exception as e:
        session.rollback()
        print(f"Error occurred while updating the recipe. Changes were not saved: {e}")

# Function to delete a recipe from the database
def delete_recipe():
    # Prompt user to select a recipe to delete
    recipe_to_delete = select_recipe_from_list()
    # If no recipe selected, exit the function
    if not recipe_to_delete:
        return

    # Confirm deletion
    confirmation = input(f"Are you sure you want to delete the recipe '{recipe_to_delete.name}'? (yes/no): ").strip().lower()
    if confirmation != 'yes':
        print("Deletion cancelled.")
        return
    
    # Delete the recipe
    deleted_id = recipe_to_delete.id    # Store ID for confirmation message
    session.delete(recipe_to_delete)
    # Commit the deletion to the database
    try:
        session.commit()
        print(f"Recipe ID '{deleted_id}' deleted successfully!")
    except Exception as e:
        session.rollback()
        print(f"Error occurred while deleting the recipe. Changes were not saved: {e}")

# ====== MAIN LOGIC ======

# Create or map the recipes table in the database
Base.metadata.create_all(engine)

# Count existing recipes in the recipes table
existing_count = session.query(Recipe).count()
print("\nWelcome to the Recipe Management Application!")
print(f"MySQL database connected. There are {existing_count} recipes in the existing table.\n")

# Display main menu and handle user choices
choice = ''
try:
    while choice != 'quit':
        print("\nMain Menu:\n" + "="*60)
        print('''Choose an operation:
        1. Create a new recipe
        2. View all recipes      
        3. Search for recipes by ingredients
        4. Edit an existing recipe
        5. Delete a recipe''')
        print("Type 'quit' to exit the application")
        print("="*60)
        choice = input("Your choice: ").strip().lower()

        if choice == '1':
            create_recipe()
        elif choice == '2':
            view_all_recipes()
        elif choice == '3':
            search_recipe()
        elif choice == '4':
            update_recipe()
        elif choice == '5':
            delete_recipe()
        elif choice == 'quit':
            # Close the session and engine before exiting
            session.close()
            engine.dispose()
            print("\nDatabase connection closed. \nExiting the program. Goodbye!")
        else:
            print("Plese enter a number from the menu or type 'quit'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    # Cleanup before exiting
    session.close()
    engine.dispose()