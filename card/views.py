from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, get_list_or_404
from card.models import FlashCard
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from card.serializers import (
    ListCreateFlashCardSerializer,
    UpdateFlashCardSerializer,
)


class CreateFlashCardView(APIView):

    permission_classes=(IsAuthenticated,)

    def post(self, request):

        serializer = ListCreateFlashCardSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UpdateFlashCardView(APIView):
    
    permission_classes=(IsAuthenticated,)

    def put(self, request, id):

        flash_card = get_object_or_404(FlashCard, id=id)

        serializer = UpdateFlashCardSerializer(
            data=request.data, instance=flash_card)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


class DeleteFlashCardView(APIView):
    
    permission_classes=(IsAuthenticated,)

    def delete(self, request, id):
        flash_card = get_object_or_404(FlashCard, id=id)
        flash_card.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class ListFlashCardsView(APIView):
    
    permission_classes=(IsAuthenticated,)
    
    def get(self, request, user_id):

        all_user_flash_cards = get_list_or_404(FlashCard, user__id=user_id)

        serializer = ListCreateFlashCardSerializer(all_user_flash_cards, many=True)

        return Response(serializer.data)
