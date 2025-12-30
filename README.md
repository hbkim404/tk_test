# Pizza Recipes

This project allows the user to scrap pizza recipe information from this [recipes site]("https://recetas.elperiodico.com/Pizza-busqCate-1.html") and work on the results.

Unfinished solution for provided problem during the interview.

---

## 🚀 Features

- Generates a `JSON` file with a list of pizza recipes scraped from a speficic static site using `Scrapy`.

- Allows the user to retrieve the information of a recipe given its name. Note that the name as to be written directly into the fuction `find_recipe` in `main.py`.

## 📦 Installation

### Using pip

```bash
# Clone the repository
git clone https://github.com/hbkim404/toku_test.git
# Navigate into the directory
cd project-name

# Install directly from pyproject.toml
pip install .
```

### Using Poetry

```bash
# Clone the repository
git clone https://github.com/hbkim404/toku_test.git
# Navigate into the directory
cd project-name

# Install dependencies
poetry install
```

### Using Hatch

```bash
# Clone the repository
git clone https://github.com/hbkim404/toku_test.git
# Navigate into the directory
cd project-name

# Install dependencies
hatch env create
```
