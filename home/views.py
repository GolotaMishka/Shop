from django.shortcuts import render
from .forms import SubscriberForm
from products.models import *
from django.shortcuts import render, get_object_or_404  # render page, return data or 404 page
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm





def home(request):
    username = auth.get_user(request).username
    context = {"username": username}
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_phones = products_images.filter(product__category__id=2)
    products_images_laptops = products_images.filter(product__category__id=3)
    products_images_tablets = products_images.filter(product__category__id=1)
    return render(request, 'landing/home.html', locals())
