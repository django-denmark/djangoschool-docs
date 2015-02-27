Excercises 2
============

These excercises follow the second lecture. Please make use of the [mailing
list](mailto:school@djangocph.dk) and the [Facebook
group](https://www.facebook.com/groups/djangocph/) if you have any questions.
Most of us are also fairly active on IRC, (#djangocph on
Freenode)[irc://irc.freenode.net:6697/djangocph], which is better for realtime
discussions.

These excercises are meant to familiarize yourself more with the test project
we have created and some of the basic mechanics of Django. There are some more
advanced topics towards the end for those that want to skip ahead, but it will
be less beginner friendly and will rely more on the Django documentation.

We will include links to specific pages in the documentation throughout theese
exercises, so if you ever get stuck they should be the first place to look.

The excercises are meant to be completed in order (we are referring to changes
we make as we go along) and you will most likely see errors if you skip ahead.

Recap: Django installation
--------------------------

Go back and take a look at the [Django installation
instructions](http://tutorial.djangogirls.org/en/django_installation/README.html).
If you were on Linux or MacOS, following the guide closely you would have done
something like the following (no need to repeat this now unless you want to make
a fresh installation):

```
  $ mkdir djangogirls
  $ cd djangogirls
  $ python3 -m venv myvenv
  $ source myvenv/bin/activate
  (myvenv) $ pip install django
    Downloading/unpacking django
    Downloading Django-1.7.4-py2.py3-none-any.whl (7.4MB): 7.4MB downloaded
    Installing collected packages: django
    Successfully installed django
    Cleaning up...
  (myvenv) $
```

If you used another directory than __djangogirls__ and/or another environment
name than __myenv__, then make a note of them because you will need them later.

Exercise 2.1: Upgrading Django
------------------------------

If you installed Django before or at the last lesson, then the latest release
number was 1.7.4. Since then version 1.7.5 has been released.
To use the environment again, we need to activate it:

```
  $ cd djangogirls
  $ source myvenv/bin/activate
```

__WARNING:__ Always be careful about upgrading. Read the release notes before
continuing. Minor versions should usually be the same (1.7.4 -> 1.7.5), major
versions may be incompatible (1.7.x -> 1.8.x).

To upgrade:

```
  (myenv) $ pip install django --upgrade
  Downloading/unpacking django from https://pypi.python.org/packages/py2.py3/D/Django/Django-1.7.5-py2.py3-none-any.whl#md5=d6b529414f3093c848a69996979a1bea
  Downloading Django-1.7.5-py2.py3-none-any.whl (7.4MB): 7.4MB downloaded
  Installing collected packages: django
  Found existing installation: Django 1.7.4
    Uninstalling Django:
      Successfully uninstalled Django
    Successfully installed django
  Cleaning up...
  (myvenv) $
```

Exercise 2.2: Installing extra packages
---------------------------------------

Django itself has limited functionality built in. However, there's a very large
number of free and opensource packages available. Some of those can be found on
either [pypi](http_//pypi.python.org) and [Django Packages](https://www.djangopackages.com/).
Quality of those modules vary.

In this exercise we install a package called Django Debug Toolbar. Django Debug
Toolbar is a configurable set of panels that display various debug information
about the current request/response and when clicked, display more details about
the panel's content
[documentation](https://www.djangopackages.com/)
[source](https://github.com/django-debug-toolbar/django-debug-toolbar)
[screenshot](http://is.gd/WRXgtb)

First make sure you're in the right directory and have your virtual environment
active (See previous exercise).

```
    (myvenv) $ pip install django-debug-toolbar
    Downloading/unpacking django-debug-toolbar
    Downloading django_debug_toolbar-1.2.2-py2.py3-none-any.whl (202kB): 202kB downloaded
    Requirement already satisfied (use --upgrade to upgrade): django>=1.4.2 in      ./myvenv/lib/python3.4/site-packages (from           django-debug-toolbar)
    Downloading/unpacking sqlparse (from django-debug-toolbar)
    Downloading sqlparse-0.1.14.tar.gz (55kB): 55kB downloaded
    Running setup.py (path:/Users/mt/priv/djangogirls/myvenv/build/sqlparse/setup.py) egg_info for package sqlparse

    Installing collected packages: django-debug-toolbar, sqlparse
      Running setup.py install for sqlparse
      Fixing build/lib/sqlparse/__init__.py build/lib/sqlparse/exceptions.py build/lib/sqlparse/filters.py  build/lib/sqlparse/formatter.py build/lib/sqlparse/functions.py build/lib/sqlparse/keywords.py build/lib/sqlparse/lexer.py build/lib/sqlparse/pipeline.py build/lib/sqlparse/sql.py build/lib/sqlparse/tokens.py build/lib/sqlparse/utils.py build/lib/sqlparse/engine/__init__.py build/lib/sqlparse/engine/filter.py build/lib/sqlparse/engine/grouping.py
    Skipping implicit fixer: buffer
    Skipping implicit fixer: idioms
    Skipping implicit fixer: set_literal
    Skipping implicit fixer: ws_comma
    Fixing build/lib/sqlparse/__init__.py build/lib/sqlparse/exceptions.py build/lib/sqlparse/filters.py build/lib/sqlparse/formatter.py build/lib/sqlparse/functions.py build/lib/sqlparse/keywords.py build/lib/sqlparse/lexer.py build/lib/sqlparse/pipeline.py build/lib/sqlparse/sql.py build/lib/sqlparse/tokens.py build/lib/sqlparse/utils.py build/lib/sqlparse/engine/__init__.py build/lib/sqlparse/engine/filter.py build/lib/sqlparse/engine/grouping.py
    Skipping implicit fixer: buffer
    Skipping implicit fixer: idioms
    Skipping implicit fixer: set_literal
    Skipping implicit fixer: ws_comma
    changing mode of build/scripts-3.4/sqlformat from 644 to 755

    changing mode of /Users/mt/priv/djangogirls/myvenv/bin/sqlformat to 755
    Successfully installed django-debug-toolbar sqlparse
    Cleaning up...
    (myvenv) $
```

As you can see, the above looks similar to the installation of Django. If you
look at the line: __Installing collected packages: django-debug-toolbar, sqlparse__
This is pip automatically resolving a dependency on the package called
sqlparse.
Installing the package is not quite enough. You also need to enable it in the
configuration file. Open the file __djangoschool/settings.py__ in your favorite
editor and find the modules __INSTALLED_APPS_ section:

```python
  INSTALLED_APPS = (
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
      'wall',
  )
```

Add a line for the debug toolbar:

```python
  INSTALLED_APPS = (
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
      __'debug_toolbar',__
      'wall',
  )
```

Save the file and now you're ready to test it:

```
  (myenv) $ python manage.py runserver
  Performing system checks...

  System check identified no issues (0 silenced).
  February 26, 2015 - 21:14:23
  Django version 1.7.5, using settings 'djangoschool.settings'
  Starting development server at http://127.0.0.1:8000/
  Quit the server with CONTROL-C.
```

Now point your browser at http://127.0.0.1:8000/ and verify that the toolbar is
visible.

As an addition to this exercise, install __django-extensions__ and run:

```
  (myenv) $ python manage.py
```

To verify that the number of options has grown. Take a look in the
[documentation](http://django-extensions.readthedocs.org/) for more details and
any extra extensions you may need to install for some of the options.

Exercise 2.3: Using Django Debug Toolbar
----------------------------------------

**add some content**
