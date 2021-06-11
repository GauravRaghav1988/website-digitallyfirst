
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "DigitallyFirst Admin Page"
admin.site.site_title = "DigitallyFirst Admin Portal"
admin.site.index_title = "Welcome to DigitallyFirst Website Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('about/', include('about.urls')),
    path('login/', include ('login.urls')),

    path('blog/', include('blog.urls')),
    path('weather/', include('weather.urls')),
]
