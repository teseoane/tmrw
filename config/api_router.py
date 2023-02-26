from django.conf.urls import include
from django.urls import path
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

urlpatterns = [
    path('jobs/', include(('tmrw.jobs.urls', 'jobs'))),
]

app_name = 'api'
urlpatterns += router.urls
