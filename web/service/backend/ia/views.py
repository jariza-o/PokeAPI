from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .ia import IA


class Gemini_Respond(APIView):
    def get(self, request, prompt: str):
        try:
            if not prompt:
                return Response({"error": "Prompt is missing"}, status=status.HTTP_400_BAD_REQUEST)

            ia_instance = IA(prompt)
            result = ia_instance.Gemini_IA()

            return Response({"Return": result}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

""" 
class Gemini_Respond(APIView):
    APIView:
        Manage the HTTP request from the API and return the response.

    Args:
        APIView:
            Class from Django Rest Framework used for create views for HTTP request.

    Return:
        The response is all work correctly, or a Error Messages if fail.
    def get(self, request, prompt: str):

        try:
            if not prompt:
                return Response({"error": "prompt fail"}, status=status.HTTP_404_NOT_FOUND)

            result = IA.Gemini_IA(prompt)
            ia_instance = IA(prompt)
            result = ia_instance.Gemini_IA()

            return Response({"Return": result}, status=status.HTTP_200_OK)
        except:
            return Response({"error"}, status=status.HTTP_404_NOT_FOUND) """