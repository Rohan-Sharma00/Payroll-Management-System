from django.urls import include, path

from rest_framework import routers

from pay.views import AttendanceViewSet

router = routers.DefaultRouter()
router.register(r'attendance', AttendanceViewSet, basename="attendance")

urlpatterns = [
   path('', include(router.urls)),
]