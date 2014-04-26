from os import path

from django.test import TestCase
from django.contrib.auth import get_user_model

from model_mommy import mommy, generators
import testfixtures


from .models import Project, Section


User = get_user_model()


class ProjectTest(TestCase):

    def test_create_project(self):
        user = mommy.make(User)
        name = generators.gen_string(10)
        project = Project(user=user, name=name)
        project.save()

        project_path = project.path()
        self.assertTrue(path.isdir(project_path), '{} does not exists'.format(project_path))

