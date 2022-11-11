from django.db import models


class Gender(models.Model):
    title = models.CharField('Название', max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пол'
        verbose_name_plural = 'Пол'


class Card(models.Model):
    name = models.CharField('Имя', max_length=255)
    number = models.PositiveBigIntegerField('Номер карты', default=10000000000000000)
    cvv = models.PositiveSmallIntegerField('CVV код')
    deadline = models.DateField('Срок истечения действия карты')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Банковская карта'
        verbose_name_plural = 'Банковские карты'
    

class Category(models.Model):
    title = models.CharField('Категория', max_length=255)
    description = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='category/', null=True, blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Courier(models.Model):
    name = models.CharField('Имя', max_length=255)
    email = models.CharField('Емеил', max_length=255)
    phone = models.PositiveBigIntegerField('Номер телефона', default=89000000000)
    address = models.CharField('Адрес', max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Курьер'
        verbose_name_plural = 'Курьеры'

    
class Delivery(models.Model):
    date = models.DateField('Дата доставки')
    cost = models.DecimalField('Стоимость доставки', default=0, max_digits=12, decimal_places=2)
    courier = models.ForeignKey(Courier, verbose_name='Курьер', db_index=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.courier} - {self.date}'

    class Meta:
        verbose_name = 'Доставка'
        verbose_name_plural = 'Доставки'


class Point(models.Model):
    address = models.CharField('Адрес', max_length=255)
    time = models.CharField('Время', max_length=255)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'Точка доставки'
        verbose_name_plural = 'Точки доставки'


class Color(models.Model):
    title = models.CharField('Цвет', max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'


class Size(models.Model):
    title = models.CharField('Размер', max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'


class Product(models.Model):
    title = models.CharField('Название', max_length=255)
    description = models.TextField('Описание')
    price_product = models.DecimalField('Цена продукта', default=0, max_digits=12, decimal_places=2)
    price_purchase = models.DecimalField('Цена закупки', default=0, max_digits=12, decimal_places=2)
    color = models.ForeignKey(Color, verbose_name='Цвет', on_delete=models.SET_NULL, null=True, blank=True)
    size = models.ManyToManyField(Size, verbose_name='Размер', null=True, blank=True)
    count = models.PositiveIntegerField('Количество', default=0)
    image = models.ImageField('Изображение', upload_to='product/', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Customer(models.Model):
    name = models.CharField('Имя', max_length=255)
    login = models.CharField('Логин', max_length=255)
    phone = models.CharField('Номер телефона', max_length=255)
    address = models.CharField('Адрес', max_length=255)
    gender = models.ForeignKey(Gender, verbose_name='Пол', on_delete=models.CASCADE)
    email = models.CharField('Емеил', max_length=255)
    password = models.CharField('Пароль', max_length=255)
    card = models.ManyToManyField(Card, verbose_name='Банковская карта', related_name='customer_card')
    favorite = models.ManyToManyField(Product, verbose_name='В сохраненных', related_name='customer_favorite')
    basket = models.ManyToManyField(Product, verbose_name='В корзине', related_name='customer_basket')

    def __str__(self):
        return self.login

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'


class StatusOrder(models.Model):
    title = models.CharField('Название', max_length=255)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказов'


class Pay(models.Model):
    title = models.CharField('Оплата', max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Оплата'
        verbose_name_plural = 'Оплата'


class Getting(models.Model):
    title = models.CharField('Точка выдачи', max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Способ получения'
        verbose_name_plural = 'Способы получения'


class Order(models.Model):
    date = models.DateTimeField('Дата', auto_now_add=True)
    cost = models.DecimalField('Стоимость', default=0, max_digits=12, decimal_places=2)
    pay = models.ForeignKey(Pay, verbose_name='Оплата', db_index=True, on_delete=models.CASCADE)
    weight = models.PositiveSmallIntegerField('Вес', default=0)
    getting = models.ForeignKey(Getting, verbose_name='Способ получения', db_index=True, on_delete=models.CASCADE)
    status = models.ForeignKey(StatusOrder, verbose_name='Статус заказа', db_index=True, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, verbose_name='Покупатель', db_index=True, on_delete=models.CASCADE)
    point = models.ForeignKey(Point, verbose_name='Точка выдачи', db_index=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.customer} - {self.point}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Comment(models.Model):
    text = models.TextField('Текст')
    review = models.ForeignKey('self', verbose_name='Ответы на комментарий', db_index=True, on_delete=models.SET_NULL, blank=True, null=True)
    product = models.ForeignKey(Product, verbose_name='Продукт', db_index=True, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, verbose_name='Покупатель', db_index=True, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField('Рейтинг', default=0)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        