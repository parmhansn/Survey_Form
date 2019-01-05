from django.shortcuts import render, HttpResponse, redirect
from django import forms


def index(request):
    return render(request, 'myapp/index.html')

def register(request):
    if 'count' not in request.session:
        request.session['count'] = 1
    else:
        request.session['count'] += 1
    
    # for key in request.session.keys():
    #     print(key, request.session(key))


    request.session['formdata'] = request.POST
    return redirect("/result")

    # formdata is just a key words you're giving it. 

def result(request):
    return render(request, 'myapp/result.html')
