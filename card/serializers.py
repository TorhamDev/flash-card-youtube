from rest_framework.serializers import ModelSerializer
from card.models import FlashCard


class ListCreateFlashCardSerializer(ModelSerializer):

    class Meta:
        model = FlashCard
        fields = "__all__"


class UpdateFlashCardSerializer(ModelSerializer):

    class Meta:
        model = FlashCard
        fields = ("question", "answer")
