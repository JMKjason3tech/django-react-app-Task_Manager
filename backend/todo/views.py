from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todo

class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)