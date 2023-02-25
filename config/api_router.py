from django.conf import settings
from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()


urlpatterns = [
    path('jobs/', include(('tmrw.jobs.urls', 'jobs'))),
]

app_name = 'api'
urlpatterns += router.urls
