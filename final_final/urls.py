from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('mecze/', include('polls.urls')),
    path(r'', include('core.urls')),
    path('admin/', admin.site.urls),
]
