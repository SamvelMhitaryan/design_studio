from rest_framework import viewsets

from .models import (
    Rate,
    Price,
    Service,
    WhyWeAre,
    ReasonsWhyWeAre,
    OurProject,
    ProjectPicture,
    OurWorksVideo,
    Review,
    OneReview,
    Connection
)
from .serializers import (
    RateSerializer,
    PriceSerializer,
    ServiceSerializer,
    WhyWeAreSerializer,
    ReasonsWhyWeAreSerializer,
    OurProjectSerializer,
    ProjectPictureSerializer,
    ReviewSerializer,
    OneReviewSerializer,
    ConnectionSerializer
)


class RateViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer


class PriceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer


class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class WhyWeAreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = WhyWeAre.objects.all()
    serializer_class = WhyWeAreSerializer


class ReasonsWhyWeAreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ReasonsWhyWeAre.objects.all()
    serializer_class = ReasonsWhyWeAreSerializer


class OurProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = OurProject.objects.all()
    serializer_class = OurProjectSerializer


class ProjectPictureViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ProjectPicture.objects.all()
    serializer_class = ProjectPictureSerializer


class ReviewViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class OneReviewViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = OneReview.objects.all()
    serializer_class = OneReviewSerializer


class ConnectionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Connection.objects.all()
    serializer_class = ConnectionSerializer
