# Exercise 19-1: Blog
# Add a Blog feature to the Learning Log project (or a new project).
#
# Steps:
# 1. Create a new app called 'blogs': python manage.py startapp blogs
# 2. Define a BlogPost model:
#    - title: CharField(max_length=200)
#    - text: TextField
#    - date_added: DateTimeField(auto_now_add=True)
#    - owner: ForeignKey(User, on_delete=models.CASCADE)
# 3. Only logged-in users can create posts (@login_required)
# 4. Users can only edit/delete their own posts (check post.owner != request.user)
# 5. All posts are visible to everyone on the public blog page
#    (no @login_required on the list view)
#
# TODO: Create BlogPost model and migrate
# TODO: Create views: blog_posts (public), new_post, edit_post
# TODO: Add ownership check on edit/delete views
# TODO: Create templates for listing and editing posts

# Exercise 19-3: Username on Home Page
# Display "Hello, <username>" on the home page when a user is logged in.
#
# In your base.html template:
# {% if user.is_authenticated %}
#   <p>Hello, {{ user.username }}. <a href="{% url 'logout' %}">Log out</a></p>
# {% else %}
#   <a href="{% url 'login' %}">Log in</a>
# {% endif %}
#
# TODO: Add the username greeting to base.html
