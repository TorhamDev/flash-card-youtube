
from django.urls import path
from card import views

urlpatterns = [
    path('create/', views.CreateFlashCardView.as_view(), name="create-falsh-card"),
    path('update/<id>/', views.UpdateFlashCardView.as_view(), name="update-falsh-card"),
    path('delete/<id>/', views.DeleteFlashCardView.as_view(), name="delete-falsh-card"),
    path('list/<user_id>/', views.ListFlashCardsView.as_view(), name="list-falsh-card"),
]
