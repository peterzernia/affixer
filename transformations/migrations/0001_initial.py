# Generated by Django 2.2 on 2019-04-03 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lexical_categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adjectives', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lexical_categories.Adjective')),
                ('adverbs', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lexical_categories.Adverb')),
                ('nouns', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lexical_categories.Noun')),
                ('verbs', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lexical_categories.Verb')),
            ],
        ),
    ]
