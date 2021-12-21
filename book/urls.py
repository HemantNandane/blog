from django.urls.conf import path
from . import views

app_name='book'
urlpatterns=[
    path('',views.home,name='home'),
    path('book/<id>',views.review,name='review'),
    path('hemant/<id>',views.hemant,name='hemant')

]