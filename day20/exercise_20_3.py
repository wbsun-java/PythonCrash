# Exercise 20-3: Stylize Learning Log
# Apply Bootstrap styling to improve the look of the Learning Log app.
#
# Steps:
# 1. Install django-bootstrap5: pip install django-bootstrap5
#    Add 'django_bootstrap5' to INSTALLED_APPS in settings.py
# 2. Update base.html:
#    - Load django_bootstrap5 at the top
#    - Add {% bootstrap_css %} and {% bootstrap_javascript %}
#    - Add a Bootstrap navbar with links to Home, Topics, Login/Logout
#    - Wrap page content in a container div
# 3. Update the login and register templates to use {% bootstrap_form form %}
# 4. Style the topics list using Bootstrap's list-group component:
#    <ul class="list-group"> ... <li class="list-group-item"> ... </li> </ul>
# 5. Add a jumbotron (or hero section) to the index page:
#    <div class="p-5 mb-4 bg-light rounded-3">
#      <h1>Track your learning.</h1>
#    </div>
#
# TODO: Update base.html with navbar and Bootstrap includes
# TODO: Restyle forms with {% bootstrap_form %}
# TODO: Restyle topic list and individual entry pages

# Exercise 20-2: Add Topics from Home Page
# Add a link on the home page (index.html) that goes directly to the new topic form.
#
# In index.html, add:
# <a href="{% url 'learning_logs:new_topic' %}">Add a new topic</a>
#
# TODO: Add the link to index.html
