from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .models import User, Shop, Category, Product, Pricat, Parameter, ProductParameter, Order, OrderItem, \
    Contact, ConfirmEmailToken


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """
    Панель управления пользователями
    """
    model = User

    fieldsets = (
        (None, {'fields': ('email', 'password', 'type')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'company', 'position')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('email', 'first_name', 'last_name', 'position', 'company', 'is_staff')


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'state', ]
    list_filter = ['name', 'state', ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


class ProductParameterInline(admin.TabularInline):
    model = ProductParameter
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'article', 'name', ]
    list_filter = ['article', 'name', ]
    inlines = [ProductParameterInline, ]


@admin.register(Parameter)
class ParameterAdmin(admin.ModelAdmin):
    pass


@admin.register(Pricat)
class PricatAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'quantity', 'price', 'price_rrc', 'shop', ]
    list_filter = ['product', 'shop', ]


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    fields = ('user', 'state', 'contact', 'created_at')
    list_display = ('id', 'user', 'created_at', 'state', 'contact')
    inlines = [OrderItemInline, ]


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass


@admin.register(ConfirmEmailToken)
class ConfirmEmailTokenAdmin(admin.ModelAdmin):
    list_display = ('user', 'key', 'created_at',)
