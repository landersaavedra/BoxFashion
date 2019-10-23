# -*- coding: utf-8 -*-
from django.db.models import Sum
from django.db import models
from django.utils.translation import ugettext as _
from WebBoxFashion.apps.security.models import Login_Customer, Login_Partner
from django.contrib.auth.models import User
import datetime
from django.utils import timezone

"""
Modelo De Clientes
"""
class Quiz_Master(models.Model):
    sname = models.CharField(max_length=500)
    ncod_quiz = models.IntegerField(verbose_name=None)
    scod_iso_quiz = models.CharField(max_length=30)

    def __str__(self):
        return self.sname

    class Meta:
        ordering = ('sname', )
        verbose_name = _("Respuesta")
        verbose_name_plural = _("Respuestas")

class Choose_Customer(models.Model):
    
    TYPE_SEX = (
        (0, _("Hombre")),
        (1, _("Mujer")),
        (2, _("Otros"))
    )

    ntype_customer = models.IntegerField(verbose_name='Tipo Cliente')
    ndescription = models.CharField(max_length=500, verbose_name='descripcion')
    dtimestamp = models.DateTimeField(auto_now_add=True , help_text=_("Fecha de creación"))
    bis_active = models.BooleanField(verbose_name='Activo')
    ntype_sex = models.IntegerField(choices=TYPE_SEX, default=1, verbose_name='Sexo')

    def __str__(self):
        return self.ndescription
    
    class Meta:
        ordering =('ntype_customer',)
        verbose_name = _('Tipo de Cliente')
        verbose_name_plural = _('Tipos de Clientes')

class Quiz_Customer(models.Model):
    created_by = models.ForeignKey(Login_Customer, related_name='login_customer', on_delete=models.CASCADE)
    type_customer = models.ForeignKey(Choose_Customer, related_name='choose_customer', on_delete=models.CASCADE)
    nbiotype = models.IntegerField(verbose_name=None)
    nnumber_shirt = models.IntegerField(verbose_name=None)
    nnumber_pants =  models.IntegerField(verbose_name=None)
    nnumber_height = models.IntegerField(verbose_name=None)
    nnumber_weight = models.IntegerField(verbose_name=None)
    nsex_customer = models.IntegerField(verbose_name=None)
    nexpenses_shirt = models.IntegerField(verbose_name=None)
    nexpenses_tshirt = models.IntegerField(verbose_name=None)
    nexpenses_pants = models.IntegerField(verbose_name=None)
    nexpenses_shorts = models.IntegerField(verbose_name=None)
    nexpenses_shoes = models.IntegerField(verbose_name=None)
    nexpenses_sneakers = models.IntegerField(verbose_name=None)
    bimported_brands = models.BooleanField(verbose_name=None)
    bnational_brands = models.BooleanField(verbose_name=None)
    dtimestamp = models.DateTimeField(auto_now_add=True , help_text=_("Fecha de creación"))

    def __str__(self):
        return self.dtimestamp

    class Meta:
        ordering = ('dtimestamp',)
        verbose_name = _("Cuestionario Cliente")
        verbose_name_plural = _("Cuestionarios Clientes")

"""
Modelo de los socios - Tiendas.
"""

class register_partners(models.Model):
    created_by= models.ForeignKey(Login_Partner, related_name='login_partner', on_delete=models.CASCADE)
    sname_representative  = models.CharField(max_length=300, verbose_name='Nombre Representate')
    sname_company = models.CharField(max_length=300, verbose_name='Nombre Empresa')
    sname_fantasy = models.CharField(max_length=300, verbose_name='Nombre Fantasia de la Empresa')
    snumber_ruc = models.CharField(max_length=11, verbose_name='Numero Ruc')
    sstreet_commercial = models.CharField(max_length=500, verbose_name='Direccion Comercial')
    dtimestamp = models.DateTimeField(auto_now_add=True, help_text=_("Fecha de creación"))

    def __str__(self):
        return self.sname_company

    class Meta:
        ordering = ('sname_company',)
        verbose_name = _("Registro Socio")
        verbose_name_plural = _("Registros de los Socios")


"""
Modelo Transaccion Financiera
"""
class Account(models.Model):
    """
    Cuentas del usuario
    """
    created_by = models.ForeignKey(User, help_text=_("Usuario que ha creado la cuenta"), on_delete= models.CASCADE)
    name = models.CharField(max_length=1000, verbose_name=_("Nombre"))
    description = models.TextField(max_length=1000, verbose_name=_("Descripción"), null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, help_text=_("Fecha de creación"))
    is_active = models.BooleanField(default=True, help_text=_("¿Se puede utilizar esta cuenta o está inactiva?"))

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )
        verbose_name = _("Cuenta")
        verbose_name_plural = _("Cuentas")


class Category(models.Model):
    TYPE_OPTIONS = (
        (0, _("Egreso")),
        (1, _("Ingreso"))
    )

    name = models.CharField(max_length=500)
    type = models.IntegerField(choices=TYPE_OPTIONS, default=1)

    def __str__(self):
        if self.type == 0:
            return "[Egreso] {0}".format(self.name)
        else:
            return "[Ingreso] {0}".format(self.name)

    class Meta:
        ordering = ('name', )
        verbose_name = _("Categoría")
        verbose_name_plural = _("Categorías")


class Transaction(models.Model):
    """
    Registra los ingresos / egresos
    """

    created_by = models.ForeignKey(User, help_text=_("Usuario que ha creado la cuenta"), on_delete=models.CASCADE)
    account = models.ForeignKey(Account, help_text=_("Cuenta a afectar"), verbose_name=_("Cuenta"), on_delete=models.CASCADE)
    name = models.CharField(max_length=500, verbose_name=_("Descripción"))
    category = models.ForeignKey(Category, verbose_name=_("Categoría"), on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=12, verbose_name=_("Monto"))
    date = models.DateField(help_text=_("Fecha del movimiento"), verbose_name=_("Fecha"))
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("-date",)
        verbose_name = _("Transacción")
        verbose_name_plural = _("Transacciones")


class TransactionComment(models.Model):
    transaction = models.ForeignKey(Transaction, verbose_name=_("Transacción"), on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, verbose_name=_("Usuario"), on_delete=models.CASCADE)
    comment = models.TextField(max_length=1200, verbose_name=_("Comentario"))
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

    class Meta:
        ordering = ('-timestamp', )
        verbose_name = _("Comentario de la transacción")
        verbose_name_plural = _("Comentarios de transacciones")