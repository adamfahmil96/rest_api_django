from django.urls import path
from . import views

urlpatterns = [
    # ketika pertama kali mengakses web, langsung diarahkan ke view dengan fungsi di dalamnya
    path('', views.index, name='index'),

    # url utk register
    path('register', views.register, name='register')
]