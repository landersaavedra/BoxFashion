# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Account, Transaction, Category, TransactionComment, Quiz_Master, Quiz_Customer
from .models  import Choose_Customer,register_partners

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('created_by', 'name', 'timestamp', 'is_active')


@admin.register(Transaction)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('created_by', 'name', 'amount', 'date')


@admin.register(TransactionComment)
class TransactionCommentAdmin(admin.ModelAdmin):
    list_display = ('created_by', 'transaction', 'timestamp')
    search_fields = ['created_by__first_name', 'created_by__last_name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')

@admin.register(Quiz_Master)
class Quiz_Master(admin.ModelAdmin):
    list_display=('sname', 'ncod_quiz', 'scod_iso_quiz')

@admin.register(Quiz_Customer)
class Quiz_Customer(admin.ModelAdmin):
    list_display=( 'created_by', 'type_customer', 'nbiotype', 'nnumber_shirt', 'nnumber_pants','nnumber_height',
    'nnumber_weight','nsex_customer','nexpenses_shirt','nexpenses_tshirt','nexpenses_pants',
    'nexpenses_shorts','nexpenses_shoes','nexpenses_sneakers','bimported_brands',
    'bnational_brands','dtimestamp')

@admin.register(Choose_Customer)
class Choose_Customer(admin.ModelAdmin):
    list_display = ('ntype_customer','ndescription','dtimestamp','ntype_sex','bis_active')


@admin.register(register_partners)
class Register_Partners(admin.ModelAdmin):
    list_display = ('created_by','sname_representative','sname_company','sname_fantasy','snumber_ruc',
    'sstreet_commercial', 'dtimestamp')