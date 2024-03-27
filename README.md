# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone https://github.com/CokeProgrammers/django-Newsblog.py.git

Now change directory to:

    $ cd django-Newsblog.py
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip3 install -r requirements/local.txt
    
Then simply apply the migrations:

    $ python manage.py makemigrations    
    $ python manage.py migrate

If above migrate command not working, run this command :

    $ python manage.py migrate --run-syncdb 

You can now run the development server:

    $ python manage.py runserver
