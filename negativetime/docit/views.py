from django.contrib.auth import authenticate, logout
from django.views.generic import View
from django.http import HttpResponse

from rest_framework.generics import ListCreateAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .serializers import ProjectSerializer, UserSerializer
from .models import Project
from .forms import LoginForm


class LoginView(View):
    def post(self, request, format=None):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.username, password=form.password)
            if user.is_active:
                serializer = UserSerializer(user)
                return Response(serializer.data)
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