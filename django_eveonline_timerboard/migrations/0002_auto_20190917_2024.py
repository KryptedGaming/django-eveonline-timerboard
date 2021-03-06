# Generated by Django 2.2.4 on 2019-09-17 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_eveonline_timerboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EveTimerType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('color', models.CharField(choices=[('primary', 'Blue'), ('secondary', 'Gray'), ('success', 'Green'), ('danger', 'Red'), ('warning', 'Yellow'), ('info', 'Light Blue'), ('light', 'White'), ('dark', 'Black')], max_length=32)),
            ],
        ),
        migrations.RemoveField(
            model_name='evetimer',
            name='groups',
        ),
        migrations.AddField(
            model_name='evetimer',
            name='location',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='evetimer',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='django_eveonline_timerboard.EveTimerType'),
        ),
    ]
