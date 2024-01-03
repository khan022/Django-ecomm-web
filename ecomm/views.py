from django.shortcuts import render
from item.models import *

# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold = False)[0:6]
    categories = Category.objects.all()

    return render(request, 'ecomm/index.html', {
        'categories' : categories,
        'items' : items,
    })

def contact(request):
    return render(request, 'ecomm/contact.html')