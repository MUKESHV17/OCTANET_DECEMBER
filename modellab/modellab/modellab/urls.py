from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include  # Add include import here
from store import views
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='home'),
    path('admin/', admin.site.urls),  # Admin panel route
    path('', include('store.urls')),  # Your app routes
   

   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
