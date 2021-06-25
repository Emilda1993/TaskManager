from django.contrib import admin
from django.urls import path,include
from to_do_list import views as todolist_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', todolist_views.index, name='index'),
    path('todolist',include('to_do_list.urls')),
    path('account/',include('users_app.urls')),
    path('contact', todolist_views.contact, name='ContactUs'),
    path('about', todolist_views.about, name='AboutUs'),
]
