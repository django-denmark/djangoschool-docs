Excercises 1
============

These excercises follow the first lecture. Please make use of the [mailing
list](mailto:school@djangocph.dk) and the [Facebook
group](https://www.facebook.com/groups/djangocph/) if you have any questions.
Most of us are also fairly active on IRC, [#django on
Freenode](irc://irc.freenode.net:6697/django), which is better for realtime
discussions.

These excercises are meant to familiarize yourself more with the test project
we have created and some of the basic mechanics of Django. There are some more
advanced topics towards the end for those that want to skip ahead, but it will
be less beginner friendly and will rely more on the Django documentation.

We will include links to specific pages in the documentation throughout theese
exercises, so if you ever get stuck they should be the first place to look.


Recap: Django Structure
-----------------------

The structure of our django project is as follows:

	code/
		manage.py             # script to run administrative tasks
		db.sqlite3            # the database with all our data
		requirements.txt      # list of required packages (just django for now)
		djangoschool/         # the django project folder
		wall/                 # our django app "wall"
		templates/            # a place to store templates across all apps
		static_src/           # where we put static content such as CSS and JS

The `djangoschool` folder contains all our settings and the base `urls.py` that
is loaded when we start our server. The file has two important lines (5-6):

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('wall.urls')),

The first line is our admin (automatically added, from the built-in django
package `admin`) and the second tells us that any URL that matches '' (which is
everything) should check in `wall.urls`, the `urls.py` found in our `wall`
folder. Similar patterns can be added for each app we add to our project to
keep app-specific URLs seperated from the main project.

If you ever want to delete all the data for your site, simply delete
`db.sqlite3` - remember, you will have to run `python manage.py migrate` and
`python manage.py createsuperuser` again afterwards to create a new database
and admin user from scratch.


Excercise 1.1: URLs
-------------------

The wall app currently has 4 "routes" in `urls.py`:

- `/`, our frontpage (list of posts)
- `/example/`, the template example
- `/post/new/`, our form for submitting a new post
- `/post/<pk>/`, which shows a post with a specific ID

Give the frontpage a new URL and change the template example to be the new
frontpage. Test that both are working by manually entering the new URLs.

For our regular examples, the symbol `^` at the start means "the URL must start
with this" and the `$` at the end means "the URL must end with this". If both
are present, it means the URL must match completely - no more, no less.

Try removing either symbol (or both) and playing around with the URLs by typing
in extra characters. For instance, removing the `$` from `post/new/` will allow
us to type in `post/new/dalsdjadakjdajkda` and it will still show the page.

Similarly, removing the `^` from `post/new/` will allows us to type in
`adklsadkadkadksaldlakkpost/new/` and still get the right page.

*Note: The starting slash right after `127.0.0.1:8000` is not included in URL
matching.*

Change your `urls.py` back to the starting point. Then create a few posts
(using the form at `post/new/`) that have a single-word title such as "Post1",
"Wonderful" or similar.

Currently, we can see posts by looking them up by their ID - lets change it to
find them based on their title (not recommended for actual websites).

In `wall/urls.py` change line 8 to the following:

    url(r'^post/(?P<title>[a-zA-Z0-9]+)/$', views.post_detail, name='post_detail'),

The regular expression `[a-zA-Z0-9]` means "Get any letter between a and z and
A and Z and any digit between 0 and 9" (lower and upper case letters are not
considered the same). The plus (`+`) means "One or more of these". If we want
to match any type of "text" we can also use the shorthand `\w+` which matches
both letters and numbers.

You can read more about python regular expressions
[here](https://docs.python.org/2/library/re.html) (for people using python 3.x
simply select your version in the upper left corner).

*NOTE: If you have any posts with a space in their title, you may see an error
message on the front page. This is because we are trying to match 'A title with
spaces' to a regular expression that only allows letters and digits. We can fix
this by changing it to `[ a-zA-Z0-9]` (notice the space at the start)!*

If you go to `post/post1` (replace `post1` with a title of a post you made) you
will get an error as we are now sending a variable called `title` when it only
expects a variable called `pk`.

Open `wall/views.py` and change line 22-23 to the following:

	def post_detail(request, title):
    	post = Post.objects.get(title=title)

If you go to `post/<your title>` again, it should now work correctly.

However, if you go back to the frontpage with our list of posts and try
clicking a link, you will now see that it's not working (as the links are still
using IDs). We'll fix that in the next excercise.

The full documentation for URL configuration can be found
[here](https://docs.djangoproject.com/en/1.7/topics/http/urls/).

Exercise 1.2: Templates
-----------------------

Our templates is where we put in the layout and design (HTML and CSS) so we
do not have it mixed with code. We use special template tags, `{{ tag }}` and
`{% tag %}` to insert dynamic content. The first allows us to insert a variable
value, such as a post title, while the other allows us to run code-like
functions, such as loops.

Let us open up our template for our list of posts,
`templates/wall/post_list.html`. On line 11 we have the link to our post, with
the following code:

	{% url 'post_detail' post.pk %}

`url` is a function that takes the name of a URL (see line 8 in `wall/urls.py`)
that we want to insert and a number of variables to pass along, in this case
the ID of the post. If we change it to the following:

    {% url 'post_detail' post.title %}

The links on the frontpage should now work again! The `url` helper function is
a good way to refer to other pages instead of manually typing in
`post/{{ post.title}}` - if we decide to change the URL later to
`myposts/<title>` then the link will still work if you used the `url` function,
but will fail if you typed the URL in manually.

You can see a list of all the helper functions django has
[here](https://docs.djangoproject.com/en/1.7/ref/templates/builtins/). Don't
worry if you don't understand all of them, you will learn to use them gradually
as you come across new problems and challenges.
