**About**

The test program for creating API server with test DB with Git repositories info (info from [get_git project](https://github.com/Sirojka/get_git)). Running with sqlite3 as DB for decrease number of containers.

**Using data structure**

    # git user model
    class GitUser(models.Model):
        name = models.CharField(max_length=256, unique=True)

    # git repository model
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

    # git commit model
    class GitRepoCommit(models.Model):
        repo_name = models.OneToOneField('GitRepo', on_delete=models.SET_NULL, null=True, related_name='last_commit')
        author = models.CharField(max_length=128)
        message = models.CharField(max_length=256, blank=True)
        datetime = models.DateTimeField()

    # git release model
    class GitRepoRelease(models.Model):
        repo_name = models.OneToOneField('GitRepo', on_delete=models.SET_NULL, null=True, related_name='last_release')
        ver = models.CharField(max_length=128)
        change_log = models.TextField(blank=True)
        datetime = models.DateTimeField()

**System requirements**

- Linux based or Windows 10+ based with WSL2 with 1Gb RAM and 10Gb free disk space
- git preinstalled
- Docker preinstalled

**Build**

Firstly we need to copy the project sources from GitHub repository to local computer, run in terminal `git clone https://github.com/Sirojka/get_git_repo_api.git`. After, go to project folder with: `cd get_git_repo_api`, and all you need is a run `./build_image.sh` file or run `sudo docker build -t "get_git_repo_api" .` command from the root folder of the project.

**Run**

Just run in terminal:
`sudo docker run -v /var/log:/var/log -v /opt:/opt -p 8000:8000 --rm get_git_repo_api:latest python manage.py runserver 0.0.0.0:8000 --noreload`

after this server will be available on local address http://127.0.0.1:8000/<endpoint> list of endpoints see below

*Endpoints description:*

    admin/ - admin panel, test login: user - admin, pass - admin
    api/v1/repos/ - list of repositories
    api/v1/repo/<repo_id>/ - info about repo_id
    api/v1/users/ - list of users
    api/v1/user_repos/<user_id>/ - list of repositories for user with user_id
    api/v1/user_url/<user_id>/ - url link for user with user_id
    api/v1/stats/ - common statistic
    api/v1/stat/<user_id>/ - statistic for user with user_id
