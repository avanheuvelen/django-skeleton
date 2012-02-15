Django skeleton
===================
This is a work in progress.

This is a Django skeleton that fits my needs. 

Current Features
-----------

* [Django](http://www.djangoproject.com) 1.3.1
* Admin enabled.
* local_settings.py and default_settings.py.
* pip requirements files
* Django Debug toolbar ready to use
* [HTML 5 Boilerplate](http://h5bp.com) implemented
* [1140px grid](http://cssgrid.net/) implemented.

Usage
-----------

Copy the project somewhere and:

1. Make a new virtualenv and activate it.
2. pip install -r requirements.txt requirements_more.txt (More is optional)
3. Copy local_settings.py.template to local_settings.py
4. Generate a new SECRET_KEY
5. Rename project to the project name.
6. (Optional) Set ip of debugger in INTERNAL_IPS and uncomment debug toolbar config in local_settings
7. Set up database and syncdb
