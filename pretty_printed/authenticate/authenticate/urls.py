from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # url admin
    path('admin/', admin.site.urls),

    # ketika pertama kali mengakses app langsung diarahkan ke url ini
    path('', include('user_example.urls')),

    # url untuk user management, langsung import dari package
    # pattern yang tersedia: login, logout, password_change, reset, dll... 
    # sesuaikan dengan pola file/folder utk html
    path('accounts/', include('django.contrib.auth.urls'))

]