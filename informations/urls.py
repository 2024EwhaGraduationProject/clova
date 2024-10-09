from django.urls import path
from .views import PointShopView, PointShopDetailView, NoticeView, NoticeDetailView, LostMylistView

app_name = 'informations'

urlpatterns = [
    path('notice/', NoticeView.as_view()),
    path('notice/<int:noticeid>/', NoticeDetailView.as_view()),

    path('pointshop/', PointShopView.as_view()),
    path('pointshop/<int:stuffid>/', PointShopDetailView.as_view()),

    path('mylostitem/', LostMylistView.as_view())
]