from django.contrib.auth import authenticate, logout
from django.views.generic import View
from django.http import HttpResponse

from rest_framework.generics import ListCreateAPIView
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