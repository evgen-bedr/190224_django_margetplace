from django.contrib import admin

from marketplace.models import (
    Address,
    Category,
    Customer,
    Order,
    OrderItem,
    Product,
    ProductDetail,
    Supplier
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # список отображаемых полей
    search_fields = ('name',)  # список полей, по которым можно делать поиск
    ordering = ('name',)  # сортировка категорий по имени в алфавитном порядке


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_email', 'phone_number')
    search_fields = ('name', 'contact_email', 'phone_number')
    ordering = ('name',)


class ProductDetailInline(admin.StackedInline):
    model = ProductDetail
    can_delete = True  # устанавливаем настройку, что нельзя будет удалять связаные объекты напрямую из интерфейса
    verbose_name_plural = 'Product Details'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'supplier', 'price', 'quantity', 'article', 'available')
    list_filter = ('category', 'supplier', 'available')
    search_fields = ('name', 'article')
    ordering = ('category', 'quantity')
    list_editable = ('price', 'quantity', 'available')
    inlines = [ProductDetailInline]


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('country', 'city', 'street', 'house')
    search_fields = ('country', 'city', 'street', 'house')
    ordering = ('country', 'city', 'street')


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'date_joined', 'deleted')
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    ordering = ('-date_joined',)
    list_filter = ('deleted',)
    list_editable = ('deleted',)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 3


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_date', 'customer')
    search_fields = ('customer__first_name', 'customer__last_name', 'customer__email')  # Тут мы для поиска
    # указали поля, которые являются вторичными ключами - customer. Обычно искать данные по вторичным
    # ключам напрямую мы не можем. Так что нужно указывать сперва название вторичного ключа, два
    # нижних подчёркивания, название конкретного поля из этого объекта, по которому хотим устроить
    # поиск. Поэтому тут строятся поля customer__first_name, customer__last_name и прочие
    ordering = ('-order_date',)
    inlines = [OrderItemInline]
