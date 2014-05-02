
from django.views.generic import View
from django.http import HttpResponseRedirect

from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import ProjectSerializer, UserSerializer
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


class SectionListView(View):
    def get(self, request, format=None, project_id=None):
        try:
            project = Project.objects.get(id=project_id)
        except Exception as e:
            return Http404()

        sections = project.sections()

        def to_dict(section):
            name, content, children = section
            return {
                'name': name,
                'content': content,
                'children': [to_dict(child) for child in children]
            }
        jsons = json.dumps([to_dict(section) for section in sections])
        return HttpResponse(jsons)


def home(request):
    return HttpResponseRedirect('/static/app/index.html')
