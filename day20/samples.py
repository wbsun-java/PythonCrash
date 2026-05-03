# Chapter 20 — Styling and Deploying an App
# Uses Bootstrap for styling and Platform.sh (or Railway) for deployment.
# Install: pip install django-bootstrap5

# --- Add Bootstrap to the project ---
# # settings.py — add to INSTALLED_APPS:
# 'django_bootstrap5',
#
# # base.html — load Bootstrap:
# {% load django_bootstrap5 %}
# {% bootstrap_css %}
# {% bootstrap_javascript %}
#
# # Wrap content in Bootstrap's container:
# <div class="container">
#   <nav class="navbar navbar-expand-md navbar-light bg-light mb-4 border">
#     <div class="container-fluid">
#       <a class="navbar-brand" href="{% url 'learning_logs:index' %}">Learning Log</a>
#     </div>
#   </nav>
#   <div class="p-3 mb-3 bg-white border rounded">
#     {% block content %}{% endblock content %}
#   </div>
# </div>

# --- Bootstrap form styling ---
# {% load django_bootstrap5 %}
# <form action="" method='post'>
#   {% csrf_token %}
#   {% bootstrap_form form %}            # renders form with Bootstrap styling
#   {% bootstrap_button button_type="submit" content="Submit" %}
# </form>

# --- Prepare for deployment ---
# # settings.py production settings:
# DEBUG = False
# ALLOWED_HOSTS = ['your-app-name.up.railway.app', 'localhost']
# SECRET_KEY = os.environ.get('SECRET_KEY')   # read from environment variable
#
# # Never hardcode secrets in settings.py — use environment variables
# import os
# SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'dev-only-default')

# --- Static files ---
# # settings.py:
# STATIC_ROOT = BASE_DIR / 'staticfiles'
#
# # Run before deploying:
# python manage.py collectstatic      # gathers all static files into staticfiles/

# --- requirements.txt ---
# pip freeze > requirements.txt       # capture all dependencies for the server
#
# # Minimum requirements for Django + Bootstrap + deployment:
# django>=4.2
# django-bootstrap5
# gunicorn                            # production web server (replaces manage.py runserver)
# whitenoise                          # serves static files in production

# --- gunicorn (production server) ---
# # Instead of: python manage.py runserver
# # Production uses: gunicorn ll_project.wsgi
# #
# # settings.py — add whitenoise for static files:
# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'whitenoise.middleware.WhiteNoiseMiddleware',  # add after SecurityMiddleware
#     ...
# ]

# --- Key ideas ---
# 1. DEBUG = False in production — it exposes your code and settings when True
# 2. SECRET_KEY must come from an env variable — never commit it to git
# 3. collectstatic gathers all CSS/JS/images into one folder the server can serve
# 4. gunicorn replaces manage.py runserver for production — it's faster and safer
# 5. whitenoise lets Django serve its own static files without a separate nginx server

print("Chapter 20: See the comments above for Bootstrap styling and deployment prep.")
print("Install: pip install django-bootstrap5 gunicorn whitenoise")
