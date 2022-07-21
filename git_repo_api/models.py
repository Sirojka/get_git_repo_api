from django.db import models

# Create your models here.


class GitUser(models.Model):
    name = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.name

    @property
    def url(self):
        return 'https://github.com/{}'.format(self.name)

    class Meta:
        verbose_name = 'GitHub user'
        verbose_name_plural = 'GitHub users'
        ordering = ['name']


class GitRepo(models.Model):
    full_name = models.CharField(max_length=256, unique=True)
    user = models.ForeignKey('GitUser', on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    site_url = models.URLField()
    stars = models.IntegerField(default=0)
    forks = models.IntegerField(default=0)
    watching = models.IntegerField(default=0)
    commits = models.IntegerField(default=0)
    releases = models.IntegerField(default=0)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Repository'
        verbose_name_plural = 'Repositories'
        ordering = ['stars']


class GitRepoCommit(models.Model):
    repo_name = models.OneToOneField('GitRepo', on_delete=models.SET_NULL, null=True, related_name='last_commit')
    # repo_name = models.ForeignKey('GitRepo', on_delete=models.SET_NULL, null=True, related_name='last_commit')
    author = models.CharField(max_length=128)
    message = models.CharField(max_length=256, blank=True)
    datetime = models.DateTimeField()

    def __str__(self):
        return '{}'.format({'author': self.author, 'message': self.message, 'datetime': self.datetime})

    class Meta:
        verbose_name = 'Commit'
        verbose_name_plural = 'Commits'
        ordering = ['datetime']


class GitRepoRelease(models.Model):
    repo_name = models.OneToOneField('GitRepo', on_delete=models.SET_NULL, null=True, related_name='last_release')
    ver = models.CharField(max_length=128)
    change_log = models.TextField(blank=True)
    datetime = models.DateTimeField()

    def __str__(self):
        return '{}'.format({'ver': self.ver, 'change_log': self.change_log, 'datetime': self.datetime})

    class Meta:
        verbose_name = 'Release'
        verbose_name_plural = 'Releases'
        ordering = ['datetime']
