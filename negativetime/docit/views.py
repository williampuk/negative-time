from django.http import HttpResponse, Http404, HttpResponseRedirect

from rest_framework.generics import (ListCreateAPIView, RetrieveAPIView,
                                     ListAPIView)
from rest_framework.permissions import IsAuthenticated

from .serializers import ProjectSerializer, UserSerializer, SectionSerializer
from .models import Project


class UserRetrieveView(RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        return self.request.user


class ProjectListCreateView(ListCreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated,)

    def pre_save(self, obj):
        obj.user = self.request.user

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)


class SectionListView(ListAPIView):
    serializer_class = SectionSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        project_id = int(self.kwargs['pk'])
        project = Project.objects.get(id=project_id)
        sections = project.sections()
        return sections


def home(request):
    return HttpResponseRedirect('/static/app/index.html')
