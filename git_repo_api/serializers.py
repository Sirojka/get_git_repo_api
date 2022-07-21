from rest_framework import serializers
from . import models


class GitRepoCommitSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('repo_name', 'author', 'message', 'datetime')
        model = models.GitRepoCommit


class GitRepoCommitLightSerializer(serializers.ModelSerializer):

    class Meta:
        exclude = ('id', 'repo_name')
        model = models.GitRepoCommit


class GitRepoReleaseSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('repo_name', 'ver', 'change_log', 'datetime')
        model = models.GitRepoRelease


class GitRepoReleaseLightSerializer(serializers.ModelSerializer):

    class Meta:
        exclude = ('id', 'repo_name')
        model = models.GitRepoRelease


class GitRepoUserNameSerializer(serializers.ModelSerializer):

    class Meta:
        # exclude = ('id',)
        fields = ('id', 'name')
        model = models.GitUser


class GitRepoSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('full_name', 'description', 'site_url')
        model = models.GitRepo


class GitRepoDetailsSerializer(serializers.ModelSerializer):
    last_commit = GitRepoCommitLightSerializer()
    last_release = GitRepoReleaseLightSerializer()
    user = GitRepoUserNameSerializer()

    class Meta:
        fields = ('full_name', 'description', 'site_url', 'stars', 'forks', 'watching', 'commits', 'releases',
                  'last_commit', 'last_release', 'user')
        model = models.GitRepo


class GitUserRepoListSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('full_name', 'stars')
        model = models.GitRepo


class GitUserURLSerializer(serializers.ModelSerializer):
    git_user_url = serializers.CharField(source='url')

    class Meta:
        fields = ('git_user_url',)
        model = models.GitUser


# No more needed
class GitStatsSerializer(serializers.ModelSerializer):
    users_count = serializers.IntegerField()
    repos_count = serializers.IntegerField()
    avg_repo_per_user = serializers.IntegerField()

    class Meta:
        fields = ('users_count', 'repos_count', 'avg_repo_per_user')
        model = models.GitRepo


# No more needed
class GitRepoStatSerializer(serializers.ModelSerializer):
    avg_stars = serializers.IntegerField()
    max_commits = serializers.IntegerField()

    class Meta:
        fields = ('avg_stars', 'max_commits', 'full_name')
        model = models.GitRepo
