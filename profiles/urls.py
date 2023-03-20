from django.urls import path
from .views import ProfileListView, ProfileDetailView

urlpatterns = [
    path('', ProfileListView.as_view(), name='profile-list'),
    path('<username>/', ProfileDetailView.as_view(), name='profile-detail'),
]
