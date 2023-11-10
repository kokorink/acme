# Generated by Django 3.2.16 on 2023-11-10 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birthday', '0005_congratulation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=20, verbose_name='Тег')),
            ],
        ),
        migrations.AlterModelOptions(
            name='congratulation',
            options={'ordering': ('-created_at',)},
        ),
        migrations.AddField(
            model_name='birthday',
            name='tags',
            field=models.ManyToManyField(blank=True, help_text='Удерживайте Ctrl для выбора нескольких вариантов', to='birthday.Tag', verbose_name='Теги'),
        ),
    ]
