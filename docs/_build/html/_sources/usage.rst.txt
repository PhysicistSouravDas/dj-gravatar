=====
Usage
=====

Suppose the directory structure of your project is like this.
:: 

    Django_Project
    │   db.sqlite3
    │   manage.py
    │
    ├───pages
    │   │   admin.py
    │   │   apps.py
    │   │   models.py
    │   │   tests.py
    │   │   urls.py
    │   │   views.py
    │   │   __init__.py
    │   └───templates
    │       │   base.html
    │       │
    │       └───pages
    │               about.html
    │               index.html
    │
    └───Django_Project
            asgi.py
            settings.py
            urls.py
            wsgi.py
            __init__.py


In ``Django_Project/settings.py``,
.. code-block:: python

    ...

    INSTALLED_APPS = [

        ...

        'dj_gravatar'   # NOTE: underscore(_) is used instead of hyphen(-)

        ...

    ]

    ...

In the Django Template (``.html`` file) where you want to show the gravatar,
.. code-block:: html

    {% load gravatar %}
    ...

    <img src="{% gravatar_url 'email@mail.com' 200 %}" alt="profile-pic">
    ...

The above code outputs like this:
.. code-block:: html

    <img src="http://www.gravatar.com/avatar/267f3587edc9b64d8e80ee7eca8abbcb?s=200&d=" alt="profile-pic">
    <!-- OR -->
    <img src="http://www.gravatar.com/avatar/[hash]?s=200&d=" alt="profile-pic">

The argument ``s=200`` represents the size of the image (``size=200px``). Default size is 80px.

You can also use the following snippet to achieve the same as above:
.. code-block:: html

    {% load gravatar %}
    ...
    {% gravatar 'email@mail' 200 "alt='profile-pic'" %}
    ...

You can use any HTML attribute instead of ``alt``, like ``style``. But only use one optional attribute at a time, Otherwise you will get ``TemplateSyntaxError``.

If you want to use ``https://.../`` instead of the default ``http://.../``, then add the following setting in your ``settings.py`` file.
.. code-block:: python

    GRAVATAR_SECURE = True  # Default False

If any email address has no matching Gravatar image, then, a default image is shown. There are the following types of default images:

* **404:** do not load any image if none is associated with the email hash, instead return an HTTP 404 (File Not Found) response
* *mp:* (mystery-person) a simple, cartoon-style silhouetted outline of a person (does not vary by email hash)
* *identicon:* a geometric pattern based on an email hash
* *monsterid:* a generated 'monster' with different colors, faces, etc
* *wavatar:* generated faces with differing features and backgrounds
* *retro:* awesome generated, 8-bit arcade-style pixelated faces
* *robohash:* a generated robot with different colors, faces, etc
* *blank:* a transparent PNG image (border added to HTML below for demonstration purposes)

You can `see here`_ how each type of default image looks like.

To show a particular default image out of the above, add the following setting to your ``settings.py`` file.
.. code-block:: python

    GRAVATAR_DEFAULT_URL = 'identicon'  # Choose any one of the above


.. _see here: https://en.gravatar.com/site/implement/images/#default-image
  