# Generated by Django 3.2.6 on 2021-08-29 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HArcherApp', '0007_auto_20210829_1410'),
    ]

    operations = [
        migrations.RenameField(
            model_name='training',
            old_name='run_1_t_1',
            new_name='a1',
        ),
        migrations.RenameField(
            model_name='training',
            old_name='run_1_t_2',
            new_name='a2',
        ),
        migrations.RenameField(
            model_name='training',
            old_name='run_1_t_3',
            new_name='a3',
        ),
        migrations.RenameField(
            model_name='training',
            old_name='run_2_t_1',
            new_name='a4',
        ),
        migrations.RenameField(
            model_name='training',
            old_name='run_2_t_2',
            new_name='a5',
        ),
        migrations.RenameField(
            model_name='training',
            old_name='run_2_t_3',
            new_name='a6',
        ),
        migrations.RenameField(
            model_name='training',
            old_name='run_3_t_1',
            new_name='b1',
        ),
        migrations.RenameField(
            model_name='training',
            old_name='run_3_t_2',
            new_name='b2',
        ),
        migrations.RenameField(
            model_name='training',
            old_name='run_3_t_3',
            new_name='b3',
        ),
        migrations.RenameField(
            model_name='training',
            old_name='run_4_t_1',
            new_name='b4',
        ),
        migrations.RenameField(
            model_name='training',
            old_name='run_4_t_2',
            new_name='b5',
        ),
        migrations.RenameField(
            model_name='training',
            old_name='run_4_t_3',
            new_name='b6',
        ),
        migrations.RenameField(
            model_name='training',
            old_name='run_5_t_1',
            new_name='c1',
        ),
        migrations.RenameField(
            model_name='training',
            old_name='run_5_t_2',
            new_name='c2',
        ),
        migrations.RenameField(
            model_name='training',
            old_name='run_5_t_3',
            new_name='c3',
        ),
        migrations.RenameField(
            model_name='training',
            old_name='run_6_t_1',
            new_name='c4',
        ),
        migrations.RenameField(
            model_name='training',
            old_name='run_6_t_2',
            new_name='c5',
        ),
        migrations.RenameField(
            model_name='training',
            old_name='run_6_t_3',
            new_name='c6',
        ),
        migrations.RemoveField(
            model_name='training',
            name='dodatkowe',
        ),
        migrations.AddField(
            model_name='training',
            name='accuracy_b',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True),
        ),
        migrations.AddField(
            model_name='training',
            name='accuracy_f',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True),
        ),
        migrations.AddField(
            model_name='training',
            name='arrows_counted_to_no_points_b',
            field=models.PositiveSmallIntegerField(blank=True, default='0', null=True),
        ),
        migrations.AddField(
            model_name='training',
            name='arrows_counted_to_no_points_f',
            field=models.PositiveSmallIntegerField(blank=True, default='0', null=True),
        ),
        migrations.AddField(
            model_name='training',
            name='arrows_in_target',
            field=models.PositiveSmallIntegerField(blank=True, default='0', null=True),
        ),
        migrations.AddField(
            model_name='training',
            name='arrows_in_target_b',
            field=models.PositiveSmallIntegerField(blank=True, default='0', null=True),
        ),
        migrations.AddField(
            model_name='training',
            name='arrows_in_target_f',
            field=models.PositiveSmallIntegerField(blank=True, default='0', null=True),
        ),
        migrations.AddField(
            model_name='training',
            name='arrows_in_target_no_points',
            field=models.PositiveSmallIntegerField(blank=True, default='0', null=True),
        ),
        migrations.AddField(
            model_name='training',
            name='arrows_in_target_no_points_b',
            field=models.PositiveSmallIntegerField(blank=True, default='0', null=True),
        ),
        migrations.AddField(
            model_name='training',
            name='arrows_in_target_no_points_f',
            field=models.PositiveSmallIntegerField(blank=True, default='0', null=True),
        ),
        migrations.AddField(
            model_name='training',
            name='arrows_shoot',
            field=models.PositiveSmallIntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='training',
            name='arrows_shoot_b',
            field=models.PositiveSmallIntegerField(blank=True, default='0', null=True),
        ),
        migrations.AddField(
            model_name='training',
            name='arrows_shoot_f',
            field=models.PositiveSmallIntegerField(blank=True, default='0', null=True),
        ),
        migrations.AddField(
            model_name='training',
            name='average_arrow_score',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True),
        ),
        migrations.AddField(
            model_name='training',
            name='average_arrow_score_b',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True),
        ),
        migrations.AddField(
            model_name='training',
            name='average_arrow_score_f',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True),
        ),
        migrations.AddField(
            model_name='training',
            name='counted_arrows',
            field=models.PositiveSmallIntegerField(blank=True, default='0', null=True),
        ),
        migrations.AddField(
            model_name='training',
            name='counted_arrows_b',
            field=models.PositiveSmallIntegerField(blank=True, default='0', null=True),
        ),
        migrations.AddField(
            model_name='training',
            name='counted_arrows_f',
            field=models.PositiveSmallIntegerField(blank=True, default='0', null=True),
        ),
        migrations.AddField(
            model_name='training',
            name='missed_arrows',
            field=models.PositiveSmallIntegerField(blank=True, default='0', null=True),
        ),
        migrations.AddField(
            model_name='training',
            name='missed_arrows_b',
            field=models.PositiveSmallIntegerField(blank=True, default='0', null=True),
        ),
        migrations.AddField(
            model_name='training',
            name='missed_arrows_f',
            field=models.PositiveSmallIntegerField(blank=True, default='0', null=True),
        ),
        migrations.AddField(
            model_name='training',
            name='result_b',
            field=models.PositiveSmallIntegerField(blank=True, default='0', null=True),
        ),
        migrations.AddField(
            model_name='training',
            name='result_f',
            field=models.PositiveSmallIntegerField(blank=True, default='0', null=True),
        ),
        migrations.DeleteModel(
            name='Results',
        ),
    ]