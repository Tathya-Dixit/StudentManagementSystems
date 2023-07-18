from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from profiles import views
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("pages.urls"),name='home'),
    path('',include("profiles.urls"),name='profiles'),
    path('login/',views.loginPage,name='loginpage'),
    path('logout/',views.logOut,name='logout'),
    
    path('reset_password/',
    PasswordResetView.as_view(template_name="password_reset.html"),
    name = "reset_password"),

    path('reset_password_sent/',
    PasswordResetDoneView.as_view(template_name = "password_reset_sent.html"),
    name = "password_reset_done"),

    path('reset/<uidb64>/<token>',
    PasswordResetConfirmView.as_view(template_name = "password_reset_confirm.html"),
    name = "password_reset_confirm"),

    path('reset_password_complete/',
    PasswordResetCompleteView.as_view(template_name = "password_reset_done.html"),
    name = "password_reset_complete"),
    


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)