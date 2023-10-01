from django.urls import path
from .views import UrlsListView, UrlRedirectView

urlpatterns = [
    path('urls_list/', UrlsListView.as_view()),
    path('urls_list/<int:url_id>', UrlsListView.as_view()),
    path('<str:short_url>/', UrlRedirectView.as_view())
]

