import os
from base64 import b32encode, b32decode
from collections import namedtuple, defaultdict

from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

import gitapi

User = get_user_model()
Section = namedtuple('Section', ['name', 'content', 'children'])


class Project(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=100)

    def path(self):
        enconded_username = b32encode(self.user.username.encode('utf8')).decode('utf8')
        enconded_name = b32encode(self.name.encode('utf8')).decode('utf8')
        return os.path.join(settings.DOCIT_PROJECT_DIR, enconded_username, enconded_name)

    def sections(self):
        path = self.path()
        repo = gitapi.Repo(path)
        if repo.git_branches():
            lstree = repo.git_command('ls-tree', '--name-only', '-r', 'HEAD').strip()
            files = sorted(lstree.split('\n'))
            return self.build_tree(files, path)
        else:
            return []

    def build_tree(self, filenames, path):
        dict = {}
        max_depth = 0

        for filename in filenames:
            split_pos = filename.find('_')
            order = filename[:split_pos].split('.')
            dict[filename] = order
            if len(order) > max_depth:
                max_depth = len(order)

        tree = [None]*max_depth
        for i in range(max_depth,0,-1):
            tree[i-1]={}
            current_depth_files = [(filename,dict[filename]) for filename in dict if len(dict[filename]) == i]
            for file in current_depth_files:
                with open(os.path.join(path, file[0])) as f:
                    content = f.read()
                if i == max_depth:
                    section = Section(file[0], content, [])
                    tree[i-1][tuple(file[1])] = section
                else:
                    children = self.getChildren(tree[i], tuple(file[1]))
                    section = Section(file[0], content, children)
                    tree[i-1][tuple(file[1])] = section

        sorted_list = sorted(tree[0].items(), key=lambda item: item[0])
        final_fking_result = [value for key, value in sorted_list]
        return final_fking_result

    def get_children(self, list, order):
        sorted_list = sorted(list.items(), key=lambda item: item[0])
        return [value for key, value in sorted_list if key[:len(order)] == order and len(key)==len(order)+1]

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        is_new = self.pk is None
        if is_new:
            path = self.path()
            os.makedirs(path, exist_ok=True)
            repo = gitapi.Repo(path)
            repo.git_init()

        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return 'Project[id={}, user={}, name={}]'.format(self.id, self.user, self.name)

