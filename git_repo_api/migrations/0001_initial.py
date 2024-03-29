# Generated by Django 3.2.14 on 2022-07-18 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GitRepo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=256, unique=True)),
                ('description', models.TextField(blank=True)),
                ('site_url', models.URLField()),
                ('stars', models.IntegerField(default=0)),
                ('forks', models.IntegerField(default=0)),
                ('watching', models.IntegerField(default=0)),
                ('commits', models.IntegerField(default=0)),
                ('releases', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Repository',
                'verbose_name_plural': 'Repositories',
                'ordering': ['stars'],
            },
        ),
        migrations.CreateModel(
            name='GitUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
            ],
            options={
                'verbose_name': 'GitHub user',
                'verbose_name_plural': 'GitHub users',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='GitRepoRelease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ver', models.CharField(max_length=128)),
                ('change_log', models.TextField(blank=True)),
                ('datetime', models.DateTimeField()),
                ('repo_name', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='last_release', to='git_repo_api.gitrepo')),
            ],
            options={
                'verbose_name': 'Release',
                'verbose_name_plural': 'Releases',
                'ordering': ['datetime'],
            },
        ),
        migrations.CreateModel(
            name='GitRepoCommit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=128)),
                ('message', models.CharField(blank=True, max_length=256)),
                ('datetime', models.DateTimeField()),
                ('repo_name', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='last_commit', to='git_repo_api.gitrepo')),
            ],
            options={
                'verbose_name': 'Commit',
                'verbose_name_plural': 'Commits',
                'ordering': ['datetime'],
            },
        ),
        migrations.AddField(
            model_name='gitrepo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='git_repo_api.gituser'),
        ),
    ]
