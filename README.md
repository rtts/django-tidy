# Django-tidy

Make Django tidy up your HTML with [HTML Tidy](http://www.html-tidy.org/)!

## Installation

1. Make sure the original `tidy` command is installed (e.g., `sudo apt install tidy`)

2. Install pytidylib: `pip install pytidylib`

3. Copy the `tidy/` directory from this repository to your Django project (or anywhere else on your Python path)

4. Add the following to your `MIDDLEWARE` setting:

        MIDDLEWARE += ['tidy.middleware.TidyMiddleware']

5. Enjoy!

## Precautions

If used in production, it is advised to use some kind of [caching](https://docs.djangoproject.com/en/dev/topics/cache/) to prevent server overload.
