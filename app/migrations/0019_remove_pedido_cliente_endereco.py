# Generated by Django 4.1.7 on 2023-06-02 23:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_pedido_valor_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='cliente_endereco',
        ),
    ]
