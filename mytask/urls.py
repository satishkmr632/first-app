from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import routers
from todoapp.views import TaskViewSet

router = routers.DefaultRouter()
router.register(r'task', TaskViewSet)

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'', include('todoapp.urls')),
    url(r'', include(router.urls)),
]
