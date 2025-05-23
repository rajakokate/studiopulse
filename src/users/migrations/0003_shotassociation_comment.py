# Generated by Django 5.2 on 2025-05-04 10:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_client_department_project_user_projectcomment_shot'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShotAssociation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('version', models.FloatField(default=1.0)),
                ('assignedFrom', models.TextField(blank=True, null=True)),
                ('assignedDate', models.TextField(blank=True, null=True)),
                ('dueDate', models.TextField(blank=True, null=True)),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.department')),
                ('shot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.shot')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'unique_together': {('version', 'shot', 'user', 'dept')},
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('commentId', models.AutoField(primary_key=True, serialize=False)),
                ('version', models.FloatField()),
                ('comment', models.TextField()),
                ('shot_association', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.shotassociation')),
            ],
        ),
    ]
