from django.urls import path
from . import views

urlpatterns = [
    # To call class based view views.ReviewView.as_view()
    path("", views.review, name="review"),
    path("thank-you/", views.ThankYouView.as_view(), name="thank-you"),
    path("reviews/", views.ReviewsListView.as_view(), name="reviews"),
    path("reviews/<int:id>", views.SingleReviewView.as_view())
]
