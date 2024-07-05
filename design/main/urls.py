from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import (
    RateViewSet,
    PriceViewSet,
    ServiceViewSet,
    WhyWeAreViewSet,
    ReasonsWhyWeAreViewSet,
    OurProjectViewSet,
    ProjectPictureViewSet,
    OurWorksVideoUrlsViewSet,
    ReviewViewSet,
    OneReviewViewSet,
    ConnectionViewSet
)

router = DefaultRouter()
router.register(r'rates', RateViewSet)
router.register(r'prices', PriceViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'whyweare', WhyWeAreViewSet)
router.register(r'reasonswhyweare', ReasonsWhyWeAreViewSet)
router.register(r'ourprojects', OurProjectViewSet)
router.register(r'projectpictures', ProjectPictureViewSet)
router.register(r'ourworksvideos', OurWorksVideoUrlsViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'onereviews', OneReviewViewSet)
router.register(r'connections', ConnectionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
