from django.shortcuts import render
from products.models import *
from django.shortcuts import render, get_object_or_404  # render page, return data or 404 page
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm


def product(request, product_id):
    username = auth.get_user(request).username
    context = {"username": username}
    product = Product.objects.get(id=product_id)


    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    print(request.session.session_key)


    return render(request, 'products/product.html', locals())