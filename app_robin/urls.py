from django.conf.urls import url, include
from views import *

urlpatterns = [
    url(r'^$', indexView, name='index'),
    url(r'^accounts/profile/$', productsView, name='profile'),
]
