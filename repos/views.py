from django.shortcuts import render
import uuid
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import clone_repository
from .models import Repo


class RepoCreateView(APIView):   #creates an API endpoint handler.

    def post(self, request):   #post is a method name that DRF uses to map HTTP POST requests to your code
        url = request.data.get("url")  #request.data contains the data sent by the client.

        if not url:
            return Response(
                {"error": "URL is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        repo = Repo.objects.create(url=url)  #saves the repository information in database.

        try:
            clone_repository(url, "/tmp/test_repo")

            repo.status = "done"
            repo.save()

        except Exception:
            repo.status = "failed"
            repo.save()

        return Response(
            {
                "id": repo.id,
                "url": repo.url,
                "status": repo.status
            },
            status=status.HTTP_201_CREATED
        )