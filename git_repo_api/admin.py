from django.contrib import admin
from . models import GitRepo, GitRepoCommit, GitRepoRelease, GitUser

# Register your models here.

admin.site.register(GitUser)
admin.site.register(GitRepo)
admin.site.register(GitRepoCommit)
admin.site.register(GitRepoRelease)
