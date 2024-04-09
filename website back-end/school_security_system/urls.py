from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import home_page

urlpatterns = [
    path('', home_page, name='home'),
    path('dashboard/', include('dashboard.urls')),
    path('registering/', include('registering.urls')),
    path('accounts/', include('accounts.urls')),
    path('reporting/', include('reporting.urls')),
    path('live_attendance/', include('live_attendance.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)