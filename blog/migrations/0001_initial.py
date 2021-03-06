# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-06-10 14:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_da_consulta', models.CharField(blank=True, max_length=300, null=True)),
                ('data_da_consulta', models.DateTimeField(blank=True, null=True)),
                ('plano_de_saude', models.CharField(blank=True, choices=[('N', 'Nao'), ('S', 'Sim')], max_length=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Especialidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('salario', models.IntegerField(blank=True, null=True)),
                ('descricao', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('cpf', models.CharField(blank=True, max_length=11, null=True)),
                ('data_de_nascimento', models.DateField(blank=True, null=True)),
                ('cidade', models.CharField(blank=True, max_length=30, null=True)),
                ('estado', models.CharField(blank=True, choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapa'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceara'), ('DF', 'Distrito Federal'), ('ES', 'Espirito Santo'), ('GO', 'Goias'), ('MA', 'Maranhao'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Para'), ('PB', 'Paraiba'), ('PR', 'Parana'), ('PE', 'Pernambuco'), ('PI', 'Piaui'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondonia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'Sao Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], max_length=2, null=True)),
                ('cep', models.CharField(blank=True, max_length=8, null=True)),
                ('email', models.EmailField(blank=True, max_length=30, null=True)),
                ('crm', models.CharField(blank=True, max_length=6, null=True)),
                ('uf', models.CharField(choices=[('AC', 'AC'), ('AL', 'AL'), ('AP', 'AP'), ('AM', 'AM'), ('BA', 'BA'), ('CE', 'CE'), ('DF', 'DF'), ('ES', 'ES'), ('GO', 'GO'), ('MA', 'MA'), ('MT', 'MT'), ('MS', 'MS'), ('MG', 'MG'), ('PA', 'PA'), ('PB', 'PB'), ('PR', 'PR'), ('PE', 'PE'), ('PI', 'PI'), ('RJ', 'RJ'), ('RN', 'RN'), ('RS', 'RS'), ('RO', 'RO'), ('RR', 'RR'), ('SC', 'SC'), ('SP', 'SP'), ('SE', 'SE'), ('TO', 'TO')], max_length=2)),
                ('sexo', models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1, null=True)),
                ('especialidade', models.ManyToManyField(to='blog.Especialidade')),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
                ('cpf', models.CharField(blank=True, max_length=11, null=True)),
                ('data_de_nascimento', models.DateField(blank=True, null=True)),
                ('cidade', models.CharField(blank=True, max_length=30, null=True)),
                ('estado', models.CharField(blank=True, choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapa'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceara'), ('DF', 'Distrito Federal'), ('ES', 'Espirito Santo'), ('GO', 'Goias'), ('MA', 'Maranhao'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Para'), ('PB', 'Paraiba'), ('PR', 'Parana'), ('PE', 'Pernambuco'), ('PI', 'Piaui'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondonia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'Sao Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], max_length=2, null=True)),
                ('cep', models.CharField(blank=True, max_length=8, null=True)),
                ('email', models.EmailField(blank=True, max_length=30, null=True)),
                ('sexo', models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='consulta',
            name='medico',
            field=models.ManyToManyField(to='blog.Medico'),
        ),
        migrations.AddField(
            model_name='consulta',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Paciente'),
        ),
    ]
