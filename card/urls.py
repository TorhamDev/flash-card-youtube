from django.urls import path
from card import views


urlpatterns = [
    path('create/', views.CreateFlashCardView.as_view(), name="create-flash-card"),
    path('update/<id>/', views.UpdateFlashCardView.as_view(), name="update-flash-card"),
    path('delete/<id>/', views.DeleteFlashCardView.as_view(), name="delete-flash-card"),
    path('list/<user_id>/', views.ListFlashCardsView.as_view(), name="list-flash-card"),
]
