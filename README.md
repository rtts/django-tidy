# Django-tidy

Make Django automatically tidy up all your generated HTML with [HTML
Tidy](http://www.html-tidy.org/)!

## Installation

First, make sure the `tidy` command is available (e.g., `sudo apt
install tidy`). Then, install Django-tidy with `pip`:

    $ pip install django-tidy

Finally, add the the following to your `MIDDLEWARE` setting:

    MIDDLEWARE += ['tidy.middleware.TidyMiddleware']

## Precautions

If used in production, it is advised to use some kind of
[caching](https://docs.djangoproject.com/en/stable/topics/cache/) to
prevent server overload.
