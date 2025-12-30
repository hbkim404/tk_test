import scrapy
import re


class RecipesSpider(scrapy.Spider):
    name = "recipes"
    start_urls = [
        "https://recetas.elperiodico.com/Pizza-busqCate-1.html",
    ]

    def parse(self, response):
        recipes_list = response.xpath(
            '//section[@class="max_width margin-top-1 resultados hasaside"]//div[@class="resultado link"]'
        )

        for recipe in recipes_list:
            details_link = recipe.xpath("a/@href").get()

            if details_link:
                yield response.follow(details_link, callback=self.parse_recipe)

        next_page = response.xpath(
            '//div[@class="paginator"]/a[@class="next"]/@href'
        ).get()

        if next_page is not None:
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_recipe(self, recipe):
        name = recipe.xpath('//h1[@class="titulo titulo--articulo"]/text()').get()

        img_src = recipe.xpath("//img/@src").get()

        ingredients = recipe.xpath(
            '//div[@class="ingredientes "]//label/text()'
        ).getall()

        yield {
            "name": self.parse_name(name),
            "img_src": img_src,
            "ingredients": self.parse_ingredients(ingredients),
        }

    def parse_name(self, name):
        return name.replace("Receta de ", "")

    def parse_ingredients(self, ingredients):
        # replace multiple white spaces between words with only one, and linebreaks
        parsed_list = [
            re.sub(r"\s+", " ", ingredient).strip() for ingredient in ingredients
        ]

        return parsed_list
