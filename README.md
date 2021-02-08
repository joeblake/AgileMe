# AgileMe

Welcome to AgileMe!

AgileMe is a full stack personal organization app, built using Python 3, Django, and Bootstrap.

You can check it out in action at http://35.212.12.127/

The Django server works like this:
It receives an http request. It matchs the path in the request with the paths defined in urls.py, and send the request to the appropriate view.
The view is your chance to do something on the backend with the data in the request. You can do whatever you like with python here, and usually end by rendering a context and a template.
The template is an HTML template written using Django's template language, and the context is data you supply to be rendered by the template. 
Django uses your template and the data to produce a page of browser-ready HTML, CSS and JS.

If you are looking to check out the code most of the action is happening in a couple places:

boards/urls.py
agileme/urls.py
boards/views.py
boards/templates/boards/login.html
boards/templates/boards/index.html
boards/templates/boards/scrum.html


Plans for the future:

Further flesh out Scrum page with urgency metrics

Configure HTTPS

