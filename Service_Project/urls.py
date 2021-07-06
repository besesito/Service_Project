from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.views import generic
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', generic.TemplateView.as_view(template_name='base.html'), name='home'),
    path('admin/', admin.site.urls),
    path('klienci/', include('customers.urls')),
    path('uslugi/', include('services.urls')),
    #API
    path('api/', include('api.urls')),
    #LOGIN
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
