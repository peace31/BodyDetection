from django.urls import path
from api.views import UserInputView


urlpatterns = [
    path('user-inputs/', UserInputView.as_view(), name='user-input'),
]
