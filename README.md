# Leads App

=====
Leads App
=====

API for listing and storing leads.

## Quick start

1. Add "leads" to your INSTALLED_APPS setting like this::

   INSTALLED_APPS = [
   ...
   'leads',
   ]

2. Include the leads URLconf in your project urls.py like this::

   path('leads/', include('leads.urls')),

3. Run `python manage.py migrate` to create the leads models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
