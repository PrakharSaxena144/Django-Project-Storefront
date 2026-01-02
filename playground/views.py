'''
It is request handler to render HTML templates and return HTTP responses for the 'playground' app.

HTTP is request-response protocol used in web development. We use views to handle incoming HTTP requests, process data (if needed), and return HTTP responses (like HTML pages, JSON data, etc.) to the client.
request -> response
'''


from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request):
    # Here we can Pull data from database using models (if needed)
    # Process data and transform it (if needed)
    # Send emails, etc.


    return render(request, 'hello.html', {'name': 'Prakhar'})  # Render the 'hello.html' template and return as HTTP response
