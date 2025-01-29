from django.urls import path
from . import views

urlpatterns = [
    path('recipients/', views.RecipientList.as_view()),
    path('recipients/<int:pk>/', views.RecipientDetail.as_view()),
    path('recipients/<uuid:unique_code>/', views.SharedRecipientDetail.as_view()),
]