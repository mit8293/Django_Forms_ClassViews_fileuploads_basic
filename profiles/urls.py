from django.urls import path

# This static has to be done on main project urls not app specific Urls
# For images folder to expose to the host
# from django.conf.urls.static import static
# from django.conf import settings

from . import views

urlpatterns = [
    path("", views.CreateProfileView.as_view()),
    path("list", views.ProfilesListView.as_view()),
]  # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Here Media Url is we want to show outside world on this URL
# Root is path where is this stored in our physical system.
