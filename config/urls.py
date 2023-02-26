from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from tmrw.views import status_view

router = routers.DefaultRouter()

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path('__status__/', status_view),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# DSF
urlpatterns += [
    # API base url
    path('api/', include('config.api_router')),
    # DRF auth token
    path('auth-token/', obtain_auth_token),
    path('api/schema/', SpectacularAPIView.as_view(), name='api-schema'),
    path(
        'api/docs/',
        SpectacularSwaggerView.as_view(url_name='api-schema'),
        name='api-docs',
    ),
]
