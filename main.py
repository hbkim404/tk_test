from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from pizza_recipes.pizza_recipes.spiders.recipes import RecipesSpider

from pathlib import Path

from utils.find_recipe import find_recipe

indexed_file_name = "indexed_pizza_recipes.json"
indexed_file_dir = Path(indexed_file_name)


def scrap_recipes():
    settings = get_project_settings()

    settings.set(
        "FEEDS",
        {
            "pizza_recipes.json": {
                "format": "json",
                "encoding": "utf8",
                "store_empty": False,
                "indent": 4,
                "overwrite": True,
            }
        },
    )

    process = CrawlerProcess(settings)
    process.crawl(RecipesSpider)
    process.start()


def delete_existing_indexed_recipes(file_dir: Path) -> None:
    try:
        file_dir.unlink(missing_ok=True)
        print(f"File '{file_dir}' has been deleted (if it existed).")

    except PermissionError:
        print(f"Permission denied to delete the file '{file_dir}'.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    scrap_recipes()
    delete_existing_indexed_recipes(indexed_file_dir)

    print("*" * 20)

    find_recipe("Pizza keto de pollo")
    find_recipe("Nombre inexistente")
    find_recipe("Masa de pizza de coliflor")

    print("*" * 20)
