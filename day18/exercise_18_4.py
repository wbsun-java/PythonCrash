# Exercise 18-4: Pizzeria
# Build a separate Django app called 'pizzas' inside a new project.
#
# Steps:
# 1. Create a new project: django-admin startproject pizzeria .
# 2. Create an app: python manage.py startapp pizzas
# 3. Define two models in pizzas/models.py:
#    - Pizza: name (CharField), and a many-to-many relationship with Topping
#    - Topping: name (CharField)
#    Note: use ManyToManyField on Pizza pointing to Topping
# 4. Run makemigrations + migrate
# 5. Register both models in admin.py and create a superuser
# 6. Add sample pizzas and toppings via the admin panel
# 7. Create a view that lists all pizzas with their toppings
# 8. Create a template to display the list
#
# TODO: Create models.py with Pizza and Topping
# TODO: Register models in admin.py
# TODO: Create views.py and urls.py
# TODO: Create templates to list pizzas and toppings

# Key difference from the book's model:
# ManyToManyField allows one pizza to have many toppings AND
# one topping to appear on many pizzas — e.g. "Cheese" on every pizza
