from django.contrib import admin
from django.urls import path
from Poll.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('vote/<poll_id>', vote, name='vote'),
    path('results/<poll_id>', results, name='results'),
    path('create/', create, name='create')
]
