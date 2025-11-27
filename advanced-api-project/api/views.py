from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Task
from .serializers import TaskSerializer


class TaskDetailView(generics.RetrieveAPIView):
    """
    Returns the details of a single task.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class TaskCreateView(generics.CreateAPIView):
    """
    Creates a new task.
    Only authenticated users can create tasks.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

