from django.contrib.auth.models import User
import pytest
from main.models import (
    Rate,
    Price,
    Service,
    WhyWeAre,
    ReasonsWhyWeAre,
    OurProject,
    ProjectPicture,
    OurWorksVideo,
    OurWorksVideoDetail,
    Review,
    OneReview,
    Connection
)


@pytest.fixture
def rate(db):
    return Rate.objects.create(
        title="Test Rate"
    )


@pytest.fixture
def price(db, rate):
    return Price.objects.create(
        price="100", 
        description="Test Description", 
        rate=rate
    )


@pytest.fixture
def service(db, rate):
    return Service.objects.create(
        title="Test Service", 
        rate=rate
    )


@pytest.fixture
def why_we_are(db):
    return WhyWeAre.objects.create(
        title="Test Why We Are"
    )


@pytest.fixture
def reasons_why_we_are(db, why_we_are):
    return ReasonsWhyWeAre.objects.create(
        text="Test Reason", 
        picture_url="http://example.com/pic.jpg", 
        why_we_are=why_we_are
    )


@pytest.fixture
def our_project(db):
    return OurProject.objects.create(
        title="Test Project", 
        footage=100.5, price=200000
    )


@pytest.fixture
def project_picture(db, our_project):
    return ProjectPicture.objects.create(
        picture_url="http://example.com/pic.jpg", 
        description="Test Description", 
        our_project=our_project
    )


@pytest.fixture
def our_works_video(db):
    return OurWorksVideo.objects.create()


@pytest.fixture
def our_works_video_detail(db, our_works_video):
    return OurWorksVideoDetail.objects.create(
        url="http://example.com/video.mp4", 
        our_works_video=our_works_video
    )


@pytest.fixture
def review(db):
    return Review.objects.create(
        title="Test Review"
    )


@pytest.fixture
def one_review(db, review):
    return OneReview.objects.create(
        name="John", surname="Doe", 
        photo_url="http://example.com/photo.jpg",
        title="Great Service", 
        text="Testimonial text", 
        email="john.doe@example.com",
        review=review
    )


@pytest.fixture
def connection(db):
    return Connection.objects.create(
        address="123 Test St.", 
        office_hours="9-5", 
        phone="1234567890", 
        email="contact@example.com"
    )


@pytest.fixture
def bitch(db):
    return User.objects.create(
        username='Gandon'
    )
