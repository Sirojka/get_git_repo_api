import json

from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.mixins import ListModelMixin
from .models import GitRepo, GitRepoCommit, GitRepoRelease, GitUser
from rest_framework.response import Response

from django.views.generic import ListView
from django.db.models import Prefetch, Count, Sum, Max, Avg
from .serializers import (GitRepoSerializer, GitRepoDetailsSerializer, GitRepoCommitSerializer,
                          GitRepoReleaseSerializer, GitRepoUserNameSerializer, GitUserRepoListSerializer,
                          GitUserURLSerializer, GitStatsSerializer, GitRepoStatSerializer)
# Create your views here.


class GitRepoListView(ListView):
    model = GitRepo
    template_name = 'gitrepo_list.html'


class GitRepoList(generics.ListAPIView):
    queryset = GitRepo.objects.all()
    serializer_class = GitRepoSerializer


class GitRepoDetail(generics.RetrieveAPIView):
    queryset = GitRepo.objects.all()
    serializer_class = GitRepoDetailsSerializer


class GitRepoUsersList(generics.ListAPIView):
    queryset = GitUser.objects.all()
    serializer_class = GitRepoUserNameSerializer


class GitUserRepoList(generics.ListAPIView):

    def get_queryset(self):
        return GitRepo.objects.filter(user_id=self.kwargs.get('pk'))

    serializer_class = GitUserRepoListSerializer


class GitUserURL(generics.RetrieveAPIView):
    queryset = GitUser.objects.all()
    serializer_class = GitUserURLSerializer


class GitStats(generics.GenericAPIView, ListModelMixin):
    queryset = GitRepo.objects.all()

    def get(self, request):
        users_count = GitUser.objects.all().count()
        repos_count = GitRepo.objects.all().count()
        avg_repo_per_user = int(repos_count/users_count)

        return Response({'users_count': users_count,
                         'repos_count': repos_count,
                         'average_repo_per_user': avg_repo_per_user})

    serializer_class = GitStatsSerializer


class GitUserStat(generics.GenericAPIView, ListModelMixin):

    def get(self, request, pk):
        max_commits = GitRepo.objects.filter(user_id=pk).aggregate(max_commits=Max('commits'))['max_commits']
        avg_stars = int(GitRepo.objects.filter(user_id=pk).aggregate(avg_stars=Avg('stars'))['avg_stars'])
        max_commits_repo = GitRepo.objects.filter(user_id=pk, commits=max_commits).values('full_name', 'commits')
        return Response({'user_id': pk, 'max_commits': max_commits, 'avg_stars': avg_stars,
                         'max_commits_repo': max_commits_repo})

    serializer_class = GitRepoStatSerializer
