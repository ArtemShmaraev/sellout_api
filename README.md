Плейлист про все https://www.youtube.com/watch?v=m7asgk5F0u8&list=PLA0M1Bcd0w8xZA3Kl1fYmOH_MfLpiYMRs&index=7
____
Краткая выжимка за 10 мин https://www.youtube.com/watch?v=TmDetBtk5rw
____
Официальня дока https://www.django-rest-framework.org/api-guide/serializers/
____
0. /admin/ - Админ панель

1. /api/v1/user инфа о пользователях

2. /api/v1/product/ - инфа по всем товарам
3. /api/v1/product/<int:product_id> - инфа по товару по его id
____
4. /api/v1/product_unit/ - инфа по всем ProductUnit
5. /api/v1/product_unit/<int:product_unit_id> - инфа по ProductUnit по id
____
6. /api/v1/product_unit/product/<int:product_id> - инфа по всем ProductUnit для ТОВАРА с id = 1
____
7. /api/v1/product_unit/product_main/<int:product_id>/<int:user_id> - инфа по товару, когда мы формируем страницу товарОВ (бренд, название, фото, цена) есть проблемка, я думаю это долгий запрос, из-зв формата бд
____
8. /api/v1/user инфа о пользователях
9. /api/v1/user/<int:id> инфа о пользователе
10. /api/v1/user/last_seen/<int:id> инфа 7 последних просмотров пользователя
____
11. /api/v1/user/wishlist/<int:user_id> избранное пользователя
12.  /api/v1/user/add_wishlist/<int:user_id>/<int:product_id>/<int:size_id> добавить в избранное пользователя товар и его размер
