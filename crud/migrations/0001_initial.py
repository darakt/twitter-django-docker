# Generated by Django 3.2.9 on 2021-12-02 18:35

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('profil_img_url', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('followers_count', models.PositiveIntegerField(default=0)),
                ('follow', models.ManyToManyField(related_name='_crud_user_follow_+', to='crud.User')),
                ('tweets', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to='crud.tweet')),
            ],
        ),
        migrations.AddField(
            model_name='tweet',
            name='mention',
            field=models.ManyToManyField(related_name='mentioned_in', to='crud.User'),
        ),
    ]