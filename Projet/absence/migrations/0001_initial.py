# Generated by Django 4.0.2 on 2022-03-05 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Annee_scolaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annee_scolaire', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Matiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Personne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=80)),
                ('prenom', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Eleve',
            fields=[
                ('personne_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='absence.personne')),
                ('statut', models.CharField(choices=[('Chef', 'Chef de classe'), ('Autre', 'Autre')], default='autre', max_length=30)),
            ],
            bases=('absence.personne',),
        ),
        migrations.CreateModel(
            name='service_secretariat',
            fields=[
                ('personne_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='absence.personne')),
                ('login', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
            bases=('absence.personne',),
        ),
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=80)),
                ('annee_scolaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='absence.annee_scolaire')),
            ],
        ),
        migrations.CreateModel(
            name='Professeur',
            fields=[
                ('personne_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='absence.personne')),
                ('classe', models.ManyToManyField(to='absence.Classe')),
            ],
            bases=('absence.personne',),
        ),
        migrations.CreateModel(
            name='Presence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('presence', models.CharField(choices=[('P', 'present'), ('A', 'absent')], max_length=1, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('heures_cours', models.CharField(choices=[('8H-10H', '8H-10H'), ('10H15-12H15', '10H15-12H15'), ('13H30-15H30', '13H30-15H30'), ('15H30-17H30', '15H30-17H30'), ('17H30-19H30', '17H30-19H30')], default='8H-10H', max_length=30)),
                ('Matiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='absence.matiere')),
                ('eleve', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='absence.eleve')),
            ],
        ),
        migrations.AddField(
            model_name='matiere',
            name='eleve',
            field=models.ManyToManyField(through='absence.Presence', to='absence.Eleve'),
        ),
        migrations.AddField(
            model_name='eleve',
            name='classe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='absence.classe'),
        ),
    ]
