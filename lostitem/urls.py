from django.urls import path
from .views import LostlistView, LostDetailView, LostImageUploadView, LostUploadView, LostSearchView

app_name = 'lostitem'

urlpatterns = [
    path('', LostlistView.as_view()),
    path('<int:lostid>/', LostDetailView.as_view()),
    path('imageupload/', LostImageUploadView.as_view()),
    path('new/', LostUploadView.as_view()),
    path('search/', LostSearchView.as_view())
]