from django.urls import path
from cafe_app import views
from django.conf.urls.static import static
from cafe import settings

urlpatterns = [
   
    path('about', views.about),
    path('contact', views.contact),
    path('edit/<rid>', views.edit),
    path('addition/<x1>/<x2>', views.addition),
    path('myview',views.SimpleView.as_view()),
    path('hello', views.hello),
    path('home', views.home),
    path('menu', views.menu),
    path('gallery', views.gallery),
    path('about', views.about),
    path('contact', views.contact),
    path('register',views.register),
    path('login',views.user_login),
    path('logout',views.user_logout),
    path('book_table', views.book_table)
    
    
    
]


