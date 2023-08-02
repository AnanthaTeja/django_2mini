# Django mini project
## Using django made a small login page
To run locally, you can either:

- Install and run from a virtual environment
- Run with docker compose (see below)

Install and run locally from a virtual environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Create a `Python 3.8+ virtualenv and activate it <https://docs.python.org/3/library/venv.html>`_

#. Install dependencies::

    python3 -m pip install -r requirements/dev.txt
    npm install

   Alternatively, use the make task::

    make install

#. Make a directory to store the project's data (``MEDIA_ROOT``, ``DOC_BUILDS_ROOT``,
   etc.). We'll use ``~/.djangoproject`` for example purposes. Create a sub-directory
   named ``conf`` inside that directory::

    mkdir -p ~/.djangoproject/conf

   Create a ``secrets.json`` file in the ``conf`` directory, containing something
   like::

    {
      "secret_key": "xyz",
      "superfeedr_creds": ["any@email.com", "some_string"],
      "db_host": "localhost",
      "db_password": "secret",
      "trac_db_host": "localhost",
      "trac_db_password": "secret"
    }

#. Add ``export DJANGOPROJECT_DATA_DIR=~/.djangoproject`` (without the backticks)
   to your ``~/.bashrc`` (or ``~/.zshrc`` if you're using zsh, ``~/.bash_profile`` if
   you're on macOS and using bash) file and then run ``source ~/.bashrc`` (or
   ``source ~/.zshrc``, or ``source ~/.bash_profile``) to load the changes.

#. Create databases::

    createuser -d djangoproject --superuser
    createdb -O djangoproject djangoproject
    createuser -d code.djangoproject --superuser
    createdb -O code.djangoproject code.djangoproject

#. Setting up database access

   If you are using the default postgres configuration, chances are you will
   have to give a password for the newly created users to be able to
   use them for Django::

     psql
     ALTER USER djangoproject WITH PASSWORD 'secret';
     ALTER USER "code.djangoproject" WITH PASSWORD 'secret';
     \d

   (Use the same passwords as the ones you've used in your ``secrets.json`` file)

#. Create tables::

    psql -d code.djangoproject < tracdb/trac.sql

    python -m manage migrate

#. Create a superuser::

    python -m manage createsuperuser

#. Populate the www and docs hostnames in the django.contrib.sites app::

    python -m manage loaddata dev_sites

#. Compile the CSS (only the source SCSS files are stored in the repository)::

    make compile-scss

#. Finally, run the server::

    make run

   This runs both the main site ("www") as well as the
   docs and dashboard site in the same process.
   Open http://www.djangoproject.localhost:8000/,
   http://docs.djangoproject.localhost:8000/,
   or
Then in the root directory (next to the ``manage.py`` file) run::

  
