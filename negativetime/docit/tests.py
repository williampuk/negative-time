from os import path

from django.test import TestCase
from django.contrib.auth import get_user_model

from model_mommy import mommy, generators


from .models import Project
from .models import Section


User = get_user_model()


class ProjectTest(TestCase):

    def test_create_project(self):
        user = mommy.make(User)
        name = generators.gen_string(10)
        project = Project(user=user, name=name)
        project.save()

        project_path = project.path()
        self.assertTrue(path.isdir(project_path), '{} does not exists'.format(project_path))

    def test_search_children(self):
        project = mommy.make(Project)
        section1 = Section("abc", "", [])
        section2 = Section("def", "", [])
        section3 = Section("ghi", "", [])
        input_list = {(1,2,3): section1, (1,2,2): section2, (1,1,1): section3}
        result = project.get_children(input_list, (1,2))
        assert len(result)==2
        assert result[1] is section1
        assert result[0] is section2

    def test_build_tree(self):
        project = mommy.make(Project)
        input = ["1_hello", "1.1_hello", "1.1.1_hello", "1.1.2_helllo", "1.2_byebye", "2_sad", "2.1_sadasad", "2.2_sad_sad"]

        result = project.build_tree(input, project.path())
        assert len(result) == "hello"
