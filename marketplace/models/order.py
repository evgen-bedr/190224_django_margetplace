"""
Создайте модель Order с полями:
    - order_date (дата и время, устанавливаемые автоматически при создании записи).
    - customer (внешний ключ на модель Customer с поведением PROTECT при удалении
    и с названием обратной связи orders).

Реализуйте метод __str__, чтобы он возвращал строку в формате "Order {id} by {customer}".


Добавьте мета-класс для модели:
    - Установите сортировку по полю order_date в порядке от самых новых записей к самым старым.
    - Установите поле order_date как используемое для получения последней записи.
"""
from django.db import models


class Order(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(
        'Customer',
        on_delete=models.PROTECT,
        related_name='orders'
    )

    def __str__(self):
        return f"Order {self.id} by {self.customer}"

    class Meta:
        ordering = ['-order_date']
        get_latest_by = 'order_date'


"""
Создайте модель OrderItem с полями:
    - order (внешний ключ на модель Order с поведением CASCADE при удалении
    и с названием обратной связи order_items).
    - product (внешний ключ на модель Product с поведением PROTECT при удалении
    и с названием обратной связи order_items).
    - quantity (положительное целое число).
    - price (десятичное поле с максимумом 10 цифр и 2 десятичными знаками).

Реализуйте метод __str__, чтобы он возвращал строку в формате "{quantity} x {product} for {order}".
"""


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='order_items'
    )
    product = models.ForeignKey(
        'Product',
        on_delete=models.PROTECT,
        related_name='order_items'
    )
    quantity = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} X {self.product.name} for {self.order}"
