from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import ProjectSerializer
from .models import Project


class ProjectListCreateView(ListCreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated,)

    def pre_save(self, obj):
        obj.user = self.request.user

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)