from django.urls import path
from . import views


urlpatterns = [
    # path('', views.GitRepoListView.as_view()),
    path('repos/', views.GitRepoList.as_view()),
    path('repo/<int:pk>/', views.GitRepoDetail.as_view()),
    path('users/', views.GitRepoUsersList.as_view()),
    path('user_repos/<int:pk>/', views.GitUserRepoList.as_view()),
    path('user_url/<int:pk>/', views.GitUserURL.as_view()),
    path('stats/', views.GitStats.as_view()),
    path('stat/<int:pk>/', views.GitUserStat.as_view()),
]
