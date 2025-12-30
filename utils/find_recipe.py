import json

from collections import defaultdict
from pathlib import Path
from typing import Optional


def get_recipes_directory():
    # utilized in case the script is run directly from its file
    script_parent_dir = Path(__file__).resolve().parent

    project_root = script_parent_dir.parent
    recipes_dir = project_root / "pizza_recipes.json"

    return recipes_dir


def index_recipes(recipe_array: list) -> defaultdict:
    # utilizing defaultdict in case a given key doesn't exist
    index = defaultdict(list)

    for recipe in recipe_array:
        for k, v in recipe.items():
            if k == "name":
                index[v].append(recipe)

    return index


def find_recipe(name: str) -> Optional[dict]:
    try:
        with open(get_recipes_directory(), "r") as f:
            data = json.load(f)

            indexed_recipes = index_recipes(data)
            recipe = indexed_recipes[name]

            return recipe if recipe else None

    except FileNotFoundError:
        print("File not found!")

    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the file.")


if __name__ == "__main__":
    recipe = find_recipe("Pizza keto de pollo")
    recipe2 = find_recipe("Pizza no existente")

    print(recipe)
    print(recipe2)
