import pytest
from main.serializers import (
    RateSerializer,
    PriceSerializer,
    ServiceSerializer,
    WhyWeAreSerializer,
    ReasonsWhyWeAreSerializer,
    OurProjectSerializer,
    ProjectPictureSerializer,
    OurWorksVideoUrlsSerializer,
    ReviewSerializer,
    OneReviewSerializer,
    ConnectionSerializer
)
from main.models import (
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


@pytest.mark.django_db
class TestSerializers:

    def test_rate_serializer(self):
        rate = Rate.objects.create(title='Test Rate')
        serializer = RateSerializer(rate)
        assert serializer.data == {'title': 'Test Rate'}

    def test_price_serializer(self):
        rate = Rate.objects.create(title='Test Rate')
        price = Price.objects.create(
            price='100', description='Test Description', rate=rate)
        serializer = PriceSerializer(price)
        assert serializer.data == {
            'price': '100', 'description': 'Test Description', 'rate': rate.id}

    def test_service_serializer(self):
        rate = Rate.objects.create(title='Test Rate')
        service = Service.objects.create(title='Test Service', rate=rate)
        serializer = ServiceSerializer(service)
        assert serializer.data == {'title': 'Test Service', 'rate': rate.id}

    def test_why_we_are_serializer(self):
        why_we_are = WhyWeAre.objects.create(title='Why We Are')
        serializer = WhyWeAreSerializer(why_we_are)
        assert serializer.data == {'title': 'Why We Are'}

    def test_reasons_why_we_are_serializer(self):
        why_we_are = WhyWeAre.objects.create(title='Why We Are')
        reasons = ReasonsWhyWeAre.objects.create(
            text='Reason Text', picture_url='http://example.com', why_we_are=why_we_are)
        serializer = ReasonsWhyWeAreSerializer(reasons)
        assert serializer.data == {
            'text': 'Reason Text', 'picture_url': 'http://example.com', 'why_we_are': why_we_are.id}

    def test_our_project_serializer(self):
        project = OurProject.objects.create(
            title='Project', footage=100.0, price=1000)
        serializer = OurProjectSerializer(project)
        assert serializer.data == {
            'title': 'Project', 'footage': 100.0, 'price': 1000}

    def test_project_picture_serializer(self):
        project = OurProject.objects.create(
            title='Project', footage=100.0, price=1000)
        picture = ProjectPicture.objects.create(
            picture_url='http://example.com', description='Picture Description', our_project=project)
        serializer = ProjectPictureSerializer(picture)
        assert serializer.data == {'picture_url': 'http://example.com',
                                   'description': 'Picture Description', 'our_project': project.id}

    def test_our_works_video_serializer(self):
        video = OurWorksVideo.objects.create()
        serializer = OurWorksVideoUrlsSerializer(video)
        assert serializer.data == {}

    def test_review_serializer(self):
        review = Review.objects.create(title='Review Title')
        serializer = ReviewSerializer(review)
        assert serializer.data == {'title': 'Review Title'}

    def test_one_review_serializer(self):
        review = Review.objects.create(title='Review Title')
        one_review = OneReview.objects.create(name='John', surname='Doe', photo_url='http://example.com/photo.jpg',
                                              title='Review Title', text='Review Text', email='john.doe@example.com', review=review)
        serializer = OneReviewSerializer(one_review)
        assert serializer.data == {'name': 'John', 'surname': 'Doe', 'photo_url': 'http://example.com/photo.jpg',
                                   'title': 'Review Title', 'text': 'Review Text', 'email': 'john.doe@example.com', 'review': review.id}

    def test_connection_serializer(self):
        connection = Connection.objects.create(
            address='123 Main St', office_hours='9-5', phone='555-1234', email='contact@example.com')
        serializer = ConnectionSerializer(connection)
        assert serializer.data == {'address': '123 Main St', 'office_hours': '9-5',
                                   'phone': '555-1234', 'email': 'contact@example.com'}
