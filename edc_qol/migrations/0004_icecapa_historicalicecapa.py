# Generated by Django 4.1.7 on 2023-04-25 15:46

import uuid

import _socket
import django.db.models.deletion
import django_audit_fields.fields.hostname_modification_field
import django_audit_fields.fields.userfield
import django_audit_fields.fields.uuid_auto_field
import django_audit_fields.models.audit_model_mixin
import django_revision.revision_field
import edc_sites.models
import edc_utils.date
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("sites", "0002_alter_domain_unique"),
        ("edc_qol", "0003_auto_20220704_1841"),
    ]

    operations = [
        migrations.CreateModel(
            name="Icecapa",
            fields=[
                (
                    "revision",
                    django_revision.revision_field.RevisionField(
                        blank=True,
                        editable=False,
                        help_text="System field. Git repository tag:branch:commit.",
                        max_length=75,
                        null=True,
                        verbose_name="Revision",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
                    ),
                ),
                (
                    "modified",
                    models.DateTimeField(
                        blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
                    ),
                ),
                (
                    "user_created",
                    django_audit_fields.fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user created",
                    ),
                ),
                (
                    "user_modified",
                    django_audit_fields.fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user modified",
                    ),
                ),
                (
                    "hostname_created",
                    models.CharField(
                        blank=True,
                        default=_socket.gethostname,
                        help_text="System field. (modified on create only)",
                        max_length=60,
                    ),
                ),
                (
                    "hostname_modified",
                    django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                        blank=True,
                        help_text="System field. (modified on every save)",
                        max_length=50,
                    ),
                ),
                ("device_created", models.CharField(blank=True, max_length=10)),
                ("device_modified", models.CharField(blank=True, max_length=10)),
                (
                    "id",
                    django_audit_fields.fields.uuid_auto_field.UUIDAutoField(
                        blank=True,
                        editable=False,
                        help_text="System auto field. UUID primary key.",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("subject_identifier", models.CharField(max_length=50, unique=True)),
                (
                    "stability",
                    models.CharField(
                        choices=[
                            (
                                "4",
                                "I am able to feel settled and secure in <B>all</B> areas of my life",
                            ),
                            (
                                "3",
                                "I am able to feel settled and secure in <B>many</B> areas of my life",
                            ),
                            (
                                "2",
                                "I am able to feel settled and secure in a <B>few</B> areas of my life",
                            ),
                            (
                                "1",
                                "I am <B>unable</B> to feel settled and secure in <B>any</B> areas of my life",
                            ),
                        ],
                        max_length=5,
                        verbose_name="Feeling settled and secure",
                    ),
                ),
                (
                    "attachment",
                    models.CharField(
                        choices=[
                            ("4", "I can have <B>a lot</B> of love, friendship and support"),
                            (
                                "3",
                                "I can have <B>quite a lot</B> of love, friendship and support",
                            ),
                            ("2", "I can have <B>a little</B> love, friendship and support"),
                            (
                                "1",
                                "I <B>cannot</B> have <B>any</B> love, friendship and support",
                            ),
                        ],
                        max_length=5,
                        verbose_name="Love, friendship and support",
                    ),
                ),
                (
                    "autonomy",
                    models.CharField(
                        choices=[
                            ("4", "I am able to be <B>completely</B> independent"),
                            ("3", "I am able to be independent in <B>many</B> things"),
                            ("2", "I am able to be independent in <B>a few</B> things"),
                            ("1", "I am <B>unable</B> to be at all independent"),
                        ],
                        max_length=5,
                        verbose_name="Being independent",
                    ),
                ),
                (
                    "achievement",
                    models.CharField(
                        choices=[
                            (
                                "4",
                                "I can achieve and progress in <B>all</B> aspects of my life",
                            ),
                            (
                                "3",
                                "I can achieve and progress in <B>many</B> aspects of my life",
                            ),
                            (
                                "2",
                                "I can achieve and progress in <B>a few</B> aspects of my life",
                            ),
                            (
                                "1",
                                "I <B>cannot</B> achieve and progress in <B>any</B> aspects of my life",
                            ),
                        ],
                        max_length=5,
                        verbose_name="Achievement and progress",
                    ),
                ),
                (
                    "enjoyment",
                    models.CharField(
                        choices=[
                            ("4", "I can have a lot of enjoyment and pleasure"),
                            ("3", "I can have quite a lot of enjoyment and pleasure"),
                            ("2", "I can have a little enjoyment and pleasure"),
                            ("1", "I cannot have any enjoyment and pleasure"),
                        ],
                        max_length=5,
                        verbose_name="Enjoyment and pleasure",
                    ),
                ),
                ("report_datetime", models.DateTimeField(default=edc_utils.date.get_utcnow)),
                (
                    "site",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        to="sites.site",
                    ),
                ),
            ],
            options={
                "verbose_name": "Overall quality of life (ICECAP-A V2)",
                "verbose_name_plural": "Overall quality of life (ICECAP-A V2)",
                "ordering": ("-modified", "-created"),
                "get_latest_by": "modified",
                "abstract": False,
                "default_permissions": ("add", "change", "delete", "view", "export", "import"),
            },
            managers=[
                ("on_site", edc_sites.models.CurrentSiteManager()),
            ],
        ),
        migrations.CreateModel(
            name="HistoricalIcecapa",
            fields=[
                (
                    "revision",
                    django_revision.revision_field.RevisionField(
                        blank=True,
                        editable=False,
                        help_text="System field. Git repository tag:branch:commit.",
                        max_length=75,
                        null=True,
                        verbose_name="Revision",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
                    ),
                ),
                (
                    "modified",
                    models.DateTimeField(
                        blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
                    ),
                ),
                (
                    "user_created",
                    django_audit_fields.fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user created",
                    ),
                ),
                (
                    "user_modified",
                    django_audit_fields.fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user modified",
                    ),
                ),
                (
                    "hostname_created",
                    models.CharField(
                        blank=True,
                        default=_socket.gethostname,
                        help_text="System field. (modified on create only)",
                        max_length=60,
                    ),
                ),
                (
                    "hostname_modified",
                    django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                        blank=True,
                        help_text="System field. (modified on every save)",
                        max_length=50,
                    ),
                ),
                ("device_created", models.CharField(blank=True, max_length=10)),
                ("device_modified", models.CharField(blank=True, max_length=10)),
                (
                    "id",
                    django_audit_fields.fields.uuid_auto_field.UUIDAutoField(
                        blank=True,
                        db_index=True,
                        editable=False,
                        help_text="System auto field. UUID primary key.",
                    ),
                ),
                ("subject_identifier", models.CharField(db_index=True, max_length=50)),
                (
                    "stability",
                    models.CharField(
                        choices=[
                            (
                                "4",
                                "I am able to feel settled and secure in <B>all</B> areas of my life",
                            ),
                            (
                                "3",
                                "I am able to feel settled and secure in <B>many</B> areas of my life",
                            ),
                            (
                                "2",
                                "I am able to feel settled and secure in a <B>few</B> areas of my life",
                            ),
                            (
                                "1",
                                "I am <B>unable</B> to feel settled and secure in <B>any</B> areas of my life",
                            ),
                        ],
                        max_length=5,
                        verbose_name="Feeling settled and secure",
                    ),
                ),
                (
                    "attachment",
                    models.CharField(
                        choices=[
                            ("4", "I can have <B>a lot</B> of love, friendship and support"),
                            (
                                "3",
                                "I can have <B>quite a lot</B> of love, friendship and support",
                            ),
                            ("2", "I can have <B>a little</B> love, friendship and support"),
                            (
                                "1",
                                "I <B>cannot</B> have <B>any</B> love, friendship and support",
                            ),
                        ],
                        max_length=5,
                        verbose_name="Love, friendship and support",
                    ),
                ),
                (
                    "autonomy",
                    models.CharField(
                        choices=[
                            ("4", "I am able to be <B>completely</B> independent"),
                            ("3", "I am able to be independent in <B>many</B> things"),
                            ("2", "I am able to be independent in <B>a few</B> things"),
                            ("1", "I am <B>unable</B> to be at all independent"),
                        ],
                        max_length=5,
                        verbose_name="Being independent",
                    ),
                ),
                (
                    "achievement",
                    models.CharField(
                        choices=[
                            (
                                "4",
                                "I can achieve and progress in <B>all</B> aspects of my life",
                            ),
                            (
                                "3",
                                "I can achieve and progress in <B>many</B> aspects of my life",
                            ),
                            (
                                "2",
                                "I can achieve and progress in <B>a few</B> aspects of my life",
                            ),
                            (
                                "1",
                                "I <B>cannot</B> achieve and progress in <B>any</B> aspects of my life",
                            ),
                        ],
                        max_length=5,
                        verbose_name="Achievement and progress",
                    ),
                ),
                (
                    "enjoyment",
                    models.CharField(
                        choices=[
                            ("4", "I can have a lot of enjoyment and pleasure"),
                            ("3", "I can have quite a lot of enjoyment and pleasure"),
                            ("2", "I can have a little enjoyment and pleasure"),
                            ("1", "I cannot have any enjoyment and pleasure"),
                        ],
                        max_length=5,
                        verbose_name="Enjoyment and pleasure",
                    ),
                ),
                ("report_datetime", models.DateTimeField(default=edc_utils.date.get_utcnow)),
                (
                    "history_id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "site",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="sites.site",
                    ),
                ),
            ],
            options={
                "verbose_name": "historical Overall quality of life (ICECAP-A V2)",
                "verbose_name_plural": "historical Overall quality of life (ICECAP-A V2)",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
