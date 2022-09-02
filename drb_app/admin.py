from django.contrib import admin
from .models import UserModel, TestModel, UnitsModel, ParametersModels, CategoryModel, BrandModel, DiscountModel
from .models import StoreModel, ProductMetaModel, StockModel, DisposableModel, JuiceModel, PodModel
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _


@admin.register(UserModel)
class UserAdmin(BaseUserAdmin):
    fieldsets =(
        (None, {'fields': ('username', 'password',)}),
        (_('Personal Info'), {'fields': ('name',)}),
        (_('Permission'), {'fields': ('is_superuser',)}),
    )

    add_fieldsets = (
        (None, {'fields': ('username', 'password1', 'password2',)}),
        (_('Personal Info'), {'fields': ('name',)}),
        (_('Permission'), {'fields': ('is_superuser', 'is_staff',)}),
    )

    list_display = ('id', 'name', 'username',)
    list_filter = ('is_superuser', 'is_staff',)
    filter_horizontal = ()
    search_fields = ('name', 'username',)
    ordering = ('name',)


@admin.register(ProductMetaModel)
class PrductMetaAdmin(admin.ModelAdmin):
    fieldsets =(
        (None, {'fields': ('brand', 'category', 'size', 'nic', 'price', 'on_sale', 'sale_price', 'popular', 'priority',
                           'discount', 'strong', 'nic_unit', 'size_unit', 'date_created', 'image')}),
    )

    add_fieldsets = (
        (None, {'fields': ('brand', 'category', 'size', 'nic', 'price', 'on_sale', 'sale_price', 'popular', 'priority',
                           'discount', 'strong', 'nic_unit', 'size_unit', 'date_created', 'image')}),

    )

    list_display = ('id', 'brand', 'category', 'nic', 'size', 'price', 'on_sale', 'sale_price', 'strong', 'popular')
    list_filter = ('brand', 'category', 'nic', 'size')
    filter_horizontal = ()
    search_fields = ('brand', 'category')
    ordering = ('brand', 'category')


@admin.register(TestModel)
class TestAdmin(admin.ModelAdmin):
    fieldsets =(
        (None, {'fields': ('data',)}),
    )

    add_fieldsets = (
        (None, {'fields': ('data',)}),

    )

    list_display = ('id', 'data',)
    list_filter = ('data',)
    filter_horizontal = ()
    search_fields = ('data',)
    ordering = ('data',)


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    fieldsets =(
        (None, {'fields': ('category',)}),
    )

    add_fieldsets = (
        (None, {'fields': ('category',)}),

    )

    list_display = ('id', 'category', 'date_created', )
    list_filter = ('category',)
    filter_horizontal = ()
    search_fields = ('category',)
    ordering = ('category',)


@admin.register(BrandModel)
class BrandAdmin(admin.ModelAdmin):
    fieldsets =(
        (None, {'fields': ('brand',)}),
    )

    add_fieldsets = (
        (None, {'fields': ('brand',)}),

    )

    list_display = ('id', 'brand', 'date_created', )
    list_filter = ('brand',)
    filter_horizontal = ()
    search_fields = ('brand',)
    ordering = ('brand',)


@admin.register(DiscountModel)
class DiscountAdmin(admin.ModelAdmin):
    fieldsets =(
        (None, {'fields': ('discount_price', 'discount_qty', )}),
    )

    add_fieldsets = (
        (None, {'fields': ('discount_price', 'discount_qty', )}),

    )

    list_display = ('id', 'discount_price', 'discount_qty', )
    list_filter = ('discount_price',)
    filter_horizontal = ()
    search_fields = ('discount_price',)
    ordering = ('discount_price',)


@admin.register(ParametersModels)
class ParameterAdmin(admin.ModelAdmin):
    fieldsets =(
        (None, {'fields': ('parameter', 'value', )}),
    )

    add_fieldsets = (
        (None, {'fields': ('parameter', 'value', )}),

    )

    list_display = ('id', 'parameter', 'value', )
    list_filter = ('parameter',)
    filter_horizontal = ()
    search_fields = ('parameter',)
    ordering = ('parameter',)


@admin.register(StoreModel)
class StoreAdmin(admin.ModelAdmin):
    fieldsets =(
        (None, {'fields': ('name', 'address', 'date_created', )}),
    )

    add_fieldsets = (
        (None, {'fields': ('name', 'address', 'date_created', )}),

    )

    list_display = ('name', 'address', 'date_created', )
    list_filter = ('name',)
    filter_horizontal = ()
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(UnitsModel)
class UnitsAdmin(admin.ModelAdmin):
    fieldsets =(
        (None, {'fields': ('unit_label', )}),
    )

    add_fieldsets = (
        (None, {'fields': ('unit_label', )}),

    )

    list_display = ('id', 'unit_label', )
    list_filter = ('unit_label',)
    filter_horizontal = ()
    search_fields = ('unit_label',)
    ordering = ('unit_label',)


@admin.register(StockModel)
class StockAdmin(admin.ModelAdmin):
    fieldsets =(
        (None, {'fields': ('store', 'stock', )}),
    )

    add_fieldsets = (
        (None, {'fields': ('store', 'stock', )}),

    )

    list_display = ('id', 'store', 'stock', )
    list_filter = ('store', 'stock', )
    filter_horizontal = ()
    search_fields = ('store', 'stock', )
    ordering = ('store',)


@admin.register(DisposableModel)
class DisposableAdmin(admin.ModelAdmin):
    fieldsets =(
        (None, {'fields': ('product', 'flavour', 'description', 'stock', 'date_created',)}),
    )

    add_fieldsets = (
        (None, {'fields': ('product', 'flavour', 'description', 'stock', 'date_created',)}),

    )

    list_display = ('id', 'product', 'flavour', 'stock')
    list_filter = ('product', 'flavour', 'stock', )
    filter_horizontal = ()
    search_fields = ('product', 'flavour', )
    ordering = ('product', 'flavour')


@admin.register(JuiceModel)
class JuiceAdmin(admin.ModelAdmin):
    fieldsets =(
        (None, {'fields': ('product', 'flavour', 'description', 'stock',  'date_created',)}),
    )

    add_fieldsets = (
        (None, {'fields': ('product', 'flavour', 'description', 'stock', 'date_created',)}),

    )

    list_display = ('id', 'product', 'flavour', 'stock')
    list_filter = ('product', 'flavour', 'stock', )
    filter_horizontal = ()
    search_fields = ('product', 'flavour', )
    ordering = ('product', 'flavour')


@admin.register(PodModel)
class PodAdmin(admin.ModelAdmin):
    fieldsets =(
        (None, {'fields': ('product', 'flavour', 'description', 'empty', 'stock',  'date_created',)}),
    )

    add_fieldsets = (
        (None, {'fields': ('product', 'flavour', 'description', 'empty', 'stock', 'date_created',)}),

    )

    list_display = ('id', 'product', 'flavour', 'stock')
    list_filter = ('product', 'flavour', 'stock', 'empty', )
    filter_horizontal = ()
    search_fields = ('product', 'flavour', )
    ordering = ('product', 'flavour')