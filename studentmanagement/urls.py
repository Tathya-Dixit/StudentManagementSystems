from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from profiles import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("pages.urls"),name='home'),
    path('',include("profiles.urls"),name='profiles'),
    path('login/',views.loginPage,name='loginpage'),
    path('logout/',views.logOut,name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)