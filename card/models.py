from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import truncatechars


User = get_user_model()

class FlashCard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField()

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return truncatechars(self.question, 10)
