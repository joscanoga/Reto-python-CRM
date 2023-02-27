# Generated by Django 4.1.7 on 2023-02-26 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CVE",
            fields=[
                (
                    "id",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                ("solucionado", models.BooleanField(default=False)),
                ("publicado", models.DateTimeField()),
                ("editado", models.DateTimeField()),
                ("descripcion", models.TextField(max_length=500)),
                ("severidad", models.CharField(max_length=50)),
                ("estado", models.CharField(max_length=50)),
            ],
        ),
    ]