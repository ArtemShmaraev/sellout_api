1. /admin/ - Админ панель

____

2. /api/v1/product/ - инфа по всем товарам
3. /api/v1/product/1 - инфа по товару с id=1

4. api/v1/product_unit/ - инфа по всем ProductUnit
5. api/v1/product_unit/1 - инфа по ProductUnit с id=1

6. api/v1/product_unit/product/1 - инфа по всем ProductUnit для ТОВАРА с id = 1

7. api/v1/product_unit/product-main/1 - инфа по товару, когда мы формируем страницу товарОВ (бренд, название, фото, цена) есть проблемка, я думаю это долгий запрос, из-зв формата бд
