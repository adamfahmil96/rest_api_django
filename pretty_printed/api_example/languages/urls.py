from django.urls import path, include
from . import views
from rest_framework import routers

# router digunakan untuk menghandle route URL awal ketika user akan mengakses API
router = routers.DefaultRouter()
# daftarkan view ke router supaya tampil
router.register('languages', views.LanguageView)
router.register('paradigms', views.ParadigmView)
router.register('programmers', views.ProgrammerView)

urlpatterns = [
    path('', include(router.urls))
]