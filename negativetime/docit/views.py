import json
import os

from django.contrib.auth import authenticate, logout
from django.views.generic import View
from django.http import HttpResponse, Http404


from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .serializers import ProjectSerializer
from .models import Project
from .forms import LoginForm


class LoginView(View):
    def post(self, request, format=None):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user and user.is_active:
                return HttpResponse(status=status.HTTP_200_OK)
        return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(View):
    def get(self, request, format=None):
        logout(request)
        return HttpResponse(status=status.HTTP_200_OK)


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


