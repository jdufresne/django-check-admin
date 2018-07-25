==================
django-check-admin
==================

django-check-admin is a Django app that adds a system check to verify that all
models have been registered with the Django admin site. This check is useful if
all models of a project should normally be registered.


Installation
============

Install the package with pip:

.. code-block::

    $ pip install django-check-admin

Add ``'checkadmin'`` to ``INSTALLED_APPS``.

.. code-block:: python

    INSTALLED_APPS = [
        ...
        'checkadmin',
    ]


Running
=======

Use the Django management command ``check``:

.. code-block::

    $ python manage.py check

If a model is not registered with the Django admin site, an error will be
emitted. For example:

.. code-block::

    The model myapp.MyModel is not registered with an admin site.

If specific models should be ignored by the check, use
``checkadmin.ignore()``::

.. code-block:: python

   import checkadmin
   from myapp.models import MyModel

   checkadmin.ignore(MyModel)

Now, even if ``MyModel`` is not registered with an admin site, an error will
not be emitted.
