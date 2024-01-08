# Generated by Django 4.2.6 on 2024-01-01 05:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature_image', models.ImageField(upload_to='Images')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=50)),
                ('date', models.DateField(auto_now_add=True)),
                ('content', models.TextField()),
                ('slug', models.SlugField(blank=True, max_length=500, null=True, unique=True)),
                ('status', models.CharField(choices=[('0', 'Draft'), ('1', 'Publish')], max_length=100)),
                ('section', models.CharField(choices=[('Popular', 'Popular'), ('Recent', 'Recent'), ('Editors_Pick', 'Editors_Pick'), ('Trending', 'Trending'), ('Inspiration', 'Inspiration'), ('Latest Posts', 'Latest Posts')], max_length=200)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.category')),
            ],
        ),
    ]
