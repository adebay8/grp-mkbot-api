# Generated by Django 3.2 on 2023-04-18 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0002_alter_category_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoreNode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_cell', models.CharField(max_length=10)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('next_node', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next_store_nodes', to='stores.storenode')),
                ('previous_node', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='previous_store_nodes', to='stores.storenode')),
            ],
        ),
        migrations.AddField(
            model_name='store',
            name='node',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stores', to='stores.storenode'),
        ),
    ]
