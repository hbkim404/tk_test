from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from pizza_recipes.pizza_recipes.spiders.recipes import RecipesSpider

from utils.find_recipe import find_recipe


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


if __name__ == "__main__":
    scrap_recipes()

    print("*" * 20)

    recipe = find_recipe("Pizza keto de pollo")

    print(f"Recipe found: {recipe}") if recipe else print("No recipe found")
    print("*" * 20)
