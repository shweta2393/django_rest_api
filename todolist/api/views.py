from rest_framework import generics
from .serializers import TodoSerializer
from .models import TodoApi


class TodoList(generics.ListCreateAPIView):
    queryset = TodoApi.objects.all()
    serializer_class = TodoSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoApi.objects.all()
    serializer_class = TodoSerializer