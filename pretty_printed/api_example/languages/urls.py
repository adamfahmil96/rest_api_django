from django.urls import path, include
from . import views
from rest_framework import routers

# router digunakan untuk menghandle route URL awal ketika user akan mengakses API
router = routers.DefaultRouter()
# yang awalnya router diarahkan ke default tampilan, namun kita akan mengganti router tersebut dengan tampilan view dari Language (REST API kita)
router.register('languages', views.LanguageView)

urlpatterns = [
    path('', include(router.urls))
]