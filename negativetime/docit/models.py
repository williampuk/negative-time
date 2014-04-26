import os
from base64 import b32encode

from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

import gitapi

User = get_user_model()


class Project(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=100)

    def path(self):
        enconded_username = b32encode(self.user.username.encode('utf8')).decode('utf8')
        enconded_name = b32encode(self.name.encode('utf8')).decode('utf8')
        return os.path.join(settings.DOCIT_PROJECT_DIR, enconded_username, enconded_name)

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


class Section(models.Model):
    project = models.ForeignKey(Project)
    name = models.CharField(max_length=100)

    def __str__(self):
        return 'Section[id={}, project={}, name={}]'.format(self.id, self.project, self.name)