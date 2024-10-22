from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .ia import IA

class Gemini_Respond(APIView):
    """
    APIView:
        Manage the HTTP request from the API and return the response.

    Args:
        APIView:
            Class from Django Rest Framework used for create views for HTTP request.

    Return:
        The response is all work correctly, or a Error Messages if fail.
    """
    def get(self, request, prompt: str):

        try:
            if not prompt:
                return Response({"error": "prompt fail"}, status=status.HTTP_404_NOT_FOUND)

            result = IA.Gemini_IA(prompt)
            return Response({"Return": result}, status=status.HTTP_200_OK)
        except:
            return Response({"error"}, status=status.HTTP_404_NOT_FOUND)