from django.urls import path
from user_accounts import views

urlpatterns = [
    path('user_accounts/', views.AccountList.as_view()),
]