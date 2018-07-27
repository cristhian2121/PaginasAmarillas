from django.db import models
from django.utils import timezone
from django.contrib import admin


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Ciudad(models.Model):
    id_ciudad = models.AutoField(primary_key=True)
    departamento = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'ciudad'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Empresa(models.Model):
    id_empresa = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    nit = models.IntegerField()
    id_tipo = models.ForeignKey('Tipo', models.DO_NOTHING, db_column='id_tipo')
    id_ciudad = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='id_ciudad')
    direccion = models.CharField(max_length=25)
    telefono = models.IntegerField(blank=True, null=True)
    celular = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=45)
    lema = models.CharField(max_length=200)
    mision = models.CharField(max_length=400, blank=True, null=True)
    vision = models.CharField(max_length=400, blank=True, null=True)
    nombre_ser_1 = models.CharField(max_length=100)
    ser_1 = models.CharField(max_length=400, blank=True, null=True)
    nombre_ser_2 = models.CharField(max_length=100, blank=True, null=True)
    ser_2 = models.CharField(max_length=400, blank=True, null=True)
    nombre_ser_3 = models.CharField(max_length=100, blank=True, null=True)
    ser_3 = models.CharField(max_length=400, blank=True, null=True)
    nombre_ser_4 = models.CharField(max_length=100, blank=True, null=True)
    ser_4 = models.CharField(max_length=400, blank=True, null=True)
    nombre_ser_5 = models.CharField(max_length=100, blank=True, null=True)
    ser_5 = models.CharField(max_length=400, blank=True, null=True)
    fecha_registro = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'empresa'


class Empresas(models.Model):
    id_empresas = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    nit = models.IntegerField()
    logo = models.CharField(max_length=25)
    id_tipo = models.ForeignKey('Tipo', models.DO_NOTHING, db_column='id_tipo')
    id_ciudad = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='id_ciudad')
    direccion = models.CharField(max_length=25)
    telefono = models.IntegerField(blank=True, null=True)
    celular = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=45)
    lema = models.CharField(max_length=200)
    mision = models.CharField(max_length=400, blank=True, null=True)
    vision = models.CharField(max_length=400, blank=True, null=True)
    nombre_ser_1 = models.CharField(max_length=100)
    ser_1 = models.CharField(max_length=400, blank=True, null=True)
    nombre_ser_2 = models.CharField(max_length=100, blank=True, null=True)
    ser_2 = models.CharField(max_length=400, blank=True, null=True)
    nombre_ser_3 = models.CharField(max_length=100, blank=True, null=True)
    ser_3 = models.CharField(max_length=400, blank=True, null=True)
    nombre_ser_4 = models.CharField(max_length=100, blank=True, null=True)
    ser_4 = models.CharField(max_length=400, blank=True, null=True)
    nombre_ser_5 = models.CharField(max_length=100, blank=True, null=True)
    ser_5 = models.CharField(max_length=400, blank=True, null=True)
    fecha_registro = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empresas'


class Tipo(models.Model):
    id_tipo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tipo'


class Users(models.Model):
    nombre = models.TextField()
    apellido = models.TextField()
    correo = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'users'
