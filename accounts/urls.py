from django.urls import path
from .views import LoginView, SignupView, SignupCodeView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('signup/', SignupView.as_view()),
    path('signupCode/', SignupCodeView.as_view())
]