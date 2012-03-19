from winecellar import models, forms
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json

"""
For any serious rest api you should get some django application:
http://djangopackages.com/grids/g/api/
"""

def read_wine_data(function):
    def decorator(request, wine_id=None):
        try:
            data = json.loads(request.read())
        except:
            return HttpResponse(status=400) #BAD_REQUEST

        form = forms.Wine(data)
        if not form.is_valid():
            return HttpResponse(status=400)
        
        if wine_id:
            return function(request, wine_id, form.cleaned_data)
        else:
            return function(request, form.cleaned_data)
    return decorator

@csrf_exempt
def wines_handler(request, wine_id=None):
    if request.method == "GET":
        return get_wines(request, wine_id)

    elif request.method == "POST":
        if wine_id:
            return HttpResponse(status=400)
        return post_wines(request)

    elif request.method == "PUT":
        if not wine_id:
            return HttpResponse(status=400)
        else:
            return put_wines(request, wine_id)

    elif request.method == "DELETE":
        return delete_wines(request, wine_id)

    else:
        return HttpResponse(status=405)

@read_wine_data
def post_wines(request, POST):
    wine = models.Wine(**POST)
    wine.save()
    return get_wines(request, wine=wine)

@read_wine_data
def put_wines(request, wine_id, PUT):
    wine = get_object_or_404(models.Wine, id=wine_id)
    wine.update(PUT)
    return HttpResponse(status=200)

def delete_wines(request, wine_id):
    wine = get_object_or_404(models.Wine, id=wine_id)
    wine.delete()
    return HttpResponse(status=200)

def get_wines(request, wine_id=None, wine=None):
    out = []
    if wine_id:
        wines = models.Wine.objects.filter(id=wine_id)
    elif wine:
        wines = [wine]
    else:
        wines = models.Wine.objects.all()

    for wine in wines:
        item = {
            "id":wine.id,
            "name":wine.name,
            "year":wine.year,
            "grapes":wine.grapes,
            "country":wine.country,
            "region":wine.region,
            "description":wine.description,
            "picture": "",
        }
        if wine.picture:
            item["picture"] = wine.picture.url
        out.append(item)

    if len(out) == 1:
        output = json.dumps(out[0])
    else:
        output = json.dumps(out)

    return HttpResponse(
            output,
            content_type = 'application/json')

