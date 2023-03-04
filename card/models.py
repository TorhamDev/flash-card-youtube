from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class FlashCard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField()

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return f"{self.question[0:10]}..."

