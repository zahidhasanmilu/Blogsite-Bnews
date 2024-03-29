from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('App_Login.urls')),
    path('apis/', include('apiApp.urls')),
    path('', include('App_Blog.urls'))

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

