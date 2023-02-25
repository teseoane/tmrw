from django.urls import path
from rest_framework.routers import DefaultRouter

from tmrw.jobs.api.views import JobListView

router = DefaultRouter()

urlpatterns = [
    path('', JobListView.as_view(), name='jobs-list'),
]

urlpatterns += router.urls
