from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DoctorViewset, AvailableTimeViewset, DesignationViewset, ReviewViewset, SpecializationViewset
router = DefaultRouter()

router.register('list', DoctorViewset)
router.register('available_time', AvailableTimeViewset)
router.register('designation', DesignationViewset)
router.register('specialization', SpecializationViewset)
router.register('reviews', ReviewViewset)

urlpatterns = [
    path('', include(router.urls)),
]