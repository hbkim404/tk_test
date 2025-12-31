import json
import functools

from pathlib import Path
from collections import defaultdict

original_file_name = "pizza_recipes.json"
indexed_file_name = "indexed_pizza_recipes.json"


def safe_file_open(func):
    @functools.wraps(func)
    def wrapper(file_path, mode, *args, **kwargs):
        try:
            with open(file_path, mode) as f:
                return func(f, *args, **kwargs)

        except FileNotFoundError:
            print("File not found!")

        except TypeError:
            print("Error: Failed to encode JSON to the file")

        except json.JSONDecodeError:
            print("Error: Failed to decode JSON from the file.")

        except Exception:
            print("Recipe not found.")

    return wrapper


@safe_file_open
def retrieve_recipes(f):
    data = json.load(f)
    indexed_recipes = index_recipes(data)

    return indexed_recipes


@safe_file_open
def generate_indexed_recipes(f, data: defaultdict):
    json.dump(data, f, ensure_ascii=False, indent=4)


@safe_file_open
def retrieve_indexed_recipe(f, name: str):
    data = json.load(f)
    recipe = data[name]

    return recipe if recipe else "Recipe not found"


def locate_indexed_file(file_dir: Path) -> bool:
    file_path = Path(file_dir)
    return True if file_path.is_file() else False


def get_file_directory(file_name: str):
    # utilized in case the script is run directly from its file
    script_parent_dir = Path(__file__).resolve().parent

    project_root = script_parent_dir.parent
    file_dir = project_root / file_name

    return file_dir


def index_recipes(recipe_array: list) -> defaultdict:
    index = defaultdict(list)

    for recipe in recipe_array:
        for k, v in recipe.items():
            if k == "name":
                index[v].append(recipe)

    return index


def find_recipe(recipe_name: str):
    original_file_dir = get_file_directory(original_file_name)
    indexed_file_dir = get_file_directory(indexed_file_name)

    original_file_exists = locate_indexed_file(original_file_dir)
    indexed_file_exists = locate_indexed_file(indexed_file_dir)

    recipe = None

    print("Retrieving recipe...")

    if indexed_file_exists:
        recipe = retrieve_indexed_recipe(indexed_file_dir, mode="r", name=recipe_name)
    elif original_file_exists:
        data = retrieve_recipes(original_file_dir, mode="r")

        if type(data) is defaultdict:
            generate_indexed_recipes(indexed_file_dir, mode="w", data=data)
            recipe = retrieve_indexed_recipe(
                indexed_file_dir, mode="r", name=recipe_name
            )
    else:
        print("No recipe files found.")

    if recipe:
        print(f"Recipe found: {recipe}")


if __name__ == "__main__":
    find_recipe("Pizza keto de pollo")
    find_recipe("Nombre inexistente")
    find_recipe("Masa de pizza de coliflor")
