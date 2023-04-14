# SellOut API
## User API
### 1. `[GET][Admin] user` информация обо всех пользователях, списком

Response:
```json
[
    {
        "id": 2,
        "password": "pbkdf2_sha256$390000$UADInQibzAcqaOZFSEcvAS$A7F5JXyyClktLYYkVZ+mjF7xfF97ArSC/mJW7GEzDA8=",
        "last_login": "2023-04-12T10:07:07Z",
        "is_superuser": false,
        "username": "noadmin",
        "first_name": "no",
        "last_name": "admin",
        "email": "noadmin@mail.ru",
        "is_staff": false,
        "is_active": true,
        "date_joined": "2023-04-12T10:07:34Z",
        "all_purchase_amount": 0,
        "personal_discount_percentage": 0,
        "referral_link": null,
        "preferred_size_grid": null,
        "gender": null,
        "ref_user": null,
        "groups": [],
        "user_permissions": [],
        "my_groups": [],
        "address": [],
        "last_viewed_products": [
            {
                "id": 1,
                "name": "Air Force 1",
                "bucket_link": "/buck",
                "description": "desc",
                "sku": "air_force_1",
                "available_flag": true,
                "last_upd": "2023-04-07T15:28:17Z",
                "add_date": "2023-04-07",
                "fit": 1,
                "rel_num": 1,
                "gender": 1,
                "brands": [
                    1
                ],
                "categories": [
                    1
                ],
                "tags": [
                    1
                ]
            }
        ]
    }
]
```
[:arrow_up:Назад](#SellOut API)
### 2. `[GET][Admin] user/<user_id>` данные пользователя

Response:
```json
{
    "id": 2,
    "password": "pbkdf2_sha256$390000$UADInQibzAcqaOZFSEcvAS$A7F5JXyyClktLYYkVZ+mjF7xfF97ArSC/mJW7GEzDA8=",
    "last_login": "2023-04-12T10:07:07Z",
    "is_superuser": false,
    "username": "noadmin",
    "first_name": "no",
    "last_name": "admin",
    "email": "noadmin@mail.ru",
    "is_staff": false,
    "is_active": true,
    "date_joined": "2023-04-12T10:07:34Z",
    "all_purchase_amount": 0,
    "personal_discount_percentage": 0,
    "referral_link": null,
    "preferred_size_grid": null,
    "gender": null,
    "ref_user": null,
    "groups": [],
    "user_permissions": [],
    "my_groups": [],
    "address": [],
    "last_viewed_products": [
        {
            "id": 1,
            "name": "Air Force 1",
            "bucket_link": "/buck",
            "description": "desc",
            "sku": "air_force_1",
            "available_flag": true,
            "last_upd": "2023-04-07T15:28:17Z",
            "add_date": "2023-04-07",
            "fit": 1,
            "rel_num": 1,
            "gender": 1,
            "brands": [
                1
            ],
            "categories": [
                1
            ],
            "tags": [
                1
            ]
        },
        {
            "id": 2,
            "name": "Dunk",
            "bucket_link": "/buck",
            "description": "desc",
            "sku": "sku",
            "available_flag": true,
            "last_upd": "2023-04-07T15:59:39Z",
            "add_date": "2023-04-07",
            "fit": 0,
            "rel_num": 0,
            "gender": 1,
            "brands": [
                1
            ],
            "categories": [
                1
            ],
            "tags": [
                1
            ]
        }
    ]
}
```
[:arrow_up:Назад](#SellOut API)
### 3. `[POST][Anon] user/register` регистрация пользователя

Body:
```json
{
    "username": "mail@mail.ru",
    "password": "пароль",
    "first_name": "Имя",
    "last_name": "Фамилия",
    "gender": "male"
}

```
Response:
```json
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4MjA4MjEyOSwiaWF0IjoxNjgxNDc3MzI5LCJqdGkiOiI2ZGExNTQ5MmMyODk0YzVmODhiNWRkN2EyNTcwNTg0MiIsInVzZXJfaWQiOjE3fQ.HhBV5bNIFtEaRaS96q_DAPAu5cdQhfRRHTcSHAl_Ffk",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgxNTYzNzI5LCJpYXQiOjE2ODE0NzczMjksImp0aSI6IjJjY2ZiZjNiZTJhYzQ3YTQ4NWRkNTY4ZGQzNWFiNzRhIiwidXNlcl9pZCI6MTd9.l-PcMX4WeUWmD5-egu1PNlgH_EdQb3tm2uIWUp57MzE"
}
```
[:arrow_up:Назад](#SellOut API)
### 4. `[POST][Anon] user/login` вход в систему

Body:
```json
{
  "username": "mail@mail.ru",
  "password": "пароль"
}
```
Response:
```json
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4MjA4MjEyOSwiaWF0IjoxNjgxNDc3MzI5LCJqdGkiOiI2ZGExNTQ5MmMyODk0YzVmODhiNWRkN2EyNTcwNTg0MiIsInVzZXJfaWQiOjE3fQ.HhBV5bNIFtEaRaS96q_DAPAu5cdQhfRRHTcSHAl_Ffk",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgxNTYzNzI5LCJpYXQiOjE2ODE0NzczMjksImp0aSI6IjJjY2ZiZjNiZTJhYzQ3YTQ4NWRkNTY4ZGQzNWFiNzRhIiwidXNlcl9pZCI6MTd9.l-PcMX4WeUWmD5-egu1PNlgH_EdQb3tm2uIWUp57MzE"
}
```
[:arrow_up:Назад](#SellOut API)
### 5. `[GET][User] user/last_seen/<user_id>` последние 7 просмотренных товаров пользователя

Response:
```json
[
    {
        "id": 1,
        "name": "Air Force 1",
        "bucket_link": "/buck",
        "description": "desc",
        "sku": "air_force_1",
        "available_flag": true,
        "last_upd": "2023-04-07T15:28:17Z",
        "add_date": "2023-04-07",
        "fit": 1,
        "rel_num": 1,
        "gender": {
            "id": 1,
            "name": "M"
        },
        "brands": [
            {
                "id": 1,
                "name": "Nike"
            }
        ],
        "categories": [
            {
                "id": 1,
                "name": "Sport"
            }
        ],
        "tags": [
            {
                "id": 1,
                "name": "Style"
            }
        ],
        "min_price": 7,
        "in_wishlist": true
    },
    {
        "id": 2,
        "name": "Dunk",
        "bucket_link": "/buck",
        "description": "desc",
        "sku": "sku",
        "available_flag": true,
        "last_upd": "2023-04-07T15:59:39Z",
        "add_date": "2023-04-07",
        "fit": 0,
        "rel_num": 0,
        "gender": {
            "id": 1,
            "name": "M"
        },
        "brands": [
            {
                "id": 1,
                "name": "Nike"
            }
        ],
        "categories": [
            {
                "id": 1,
                "name": "Sport"
            }
        ],
        "tags": [
            {
                "id": 1,
                "name": "Style"
            }
        ],
        "min_price": 100,
        "in_wishlist": false
    }
]
```
[:arrow_up:Назад](#SellOut API)
## Product APi

### 1. `[GET][Admin] product` все товары
Response:
```json
[
    {
        "id": 1,
        "name": "Air Force 1",
        "bucket_link": "/buck",
        "description": "desc",
        "sku": "air_force_1",
        "available_flag": true,
        "last_upd": "2023-04-07T15:28:17Z",
        "add_date": "2023-04-07",
        "fit": 1,
        "rel_num": 1,
        "gender": {
            "id": 1,
            "name": "M"
        },
        "brands": [
            {
                "id": 1,
                "name": "Nike"
            }
        ],
        "categories": [
            {
                "id": 1,
                "name": "Sport"
            }
        ],
        "tags": [
            {
                "id": 1,
                "name": "Style"
            }
        ]
    },
    {
        "id": 2,
        "name": "Dunk",
        "bucket_link": "/buck",
        "description": "desc",
        "sku": "sku",
        "available_flag": true,
        "last_upd": "2023-04-07T15:59:39Z",
        "add_date": "2023-04-07",
        "fit": 0,
        "rel_num": 0,
        "gender": {
            "id": 1,
            "name": "M"
        },
        "brands": [
            {
                "id": 1,
                "name": "Nike"
            }
        ],
        "categories": [
            {
                "id": 1,
                "name": "Sport"
            }
        ],
        "tags": [
            {
                "id": 1,
                "name": "Style"
            }
        ]
    }
]
```
[:arrow_up:Назад](#SellOut API)
### 2. `[GET][Admin] product/<product_id>` данные одного товара
Response:
```json
{
    "id": 1,
    "name": "Air Force 1",
    "bucket_link": "/buck",
    "description": "desc",
    "sku": "air_force_1",
    "available_flag": true,
    "last_upd": "2023-04-07T15:28:17Z",
    "add_date": "2023-04-07",
    "fit": 1,
    "rel_num": 1,
    "gender": {
        "id": 1,
        "name": "M"
    },
    "brands": [
        {
            "id": 1,
            "name": "Nike"
        }
    ],
    "categories": [
        {
            "id": 1,
            "name": "Sport"
        }
    ],
    "tags": [
        {
            "id": 1,
            "name": "Style"
        }
    ]
}
```
[:arrow_up:Назад](#SellOut API)
### 3. `[GET][Anon] product/all/<num_page>` страница товаров 
Response:
```json
{
    "page number": 1,
    "items": [
        {
            "id": 1,
            "name": "Air Force 1",
            "bucket_link": "/buck",
            "description": "desc",
            "sku": "air_force_1",
            "available_flag": true,
            "last_upd": "2023-04-07T15:28:17Z",
            "add_date": "2023-04-07",
            "fit": 1,
            "rel_num": 1,
            "gender": {
                "id": 1,
                "name": "M"
            },
            "brands": [
                {
                    "id": 1,
                    "name": "Nike"
                }
            ],
            "categories": [
                {
                    "id": 1,
                    "name": "Sport"
                }
            ],
            "tags": [
                {
                    "id": 1,
                    "name": "Style"
                }
            ],
            "min_price": 7,
            "in_wishlist": true
        },
        {
            "id": 2,
            "name": "Dunk",
            "bucket_link": "/buck",
            "description": "desc",
            "sku": "sku",
            "available_flag": true,
            "last_upd": "2023-04-07T15:59:39Z",
            "add_date": "2023-04-07",
            "fit": 0,
            "rel_num": 0,
            "gender": {
                "id": 1,
                "name": "M"
            },
            "brands": [
                {
                    "id": 1,
                    "name": "Nike"
                }
            ],
            "categories": [
                {
                    "id": 1,
                    "name": "Sport"
                }
            ],
            "tags": [
                {
                    "id": 1,
                    "name": "Style"
                }
            ],
            "min_price": 100,
            "in_wishlist": false
        }
    ]
}
```
[:arrow_up:Назад](#SellOut API)
## Shipping API
### 1. `[GET][Anon] product_unit/product/<product_id>` все product_unit для данного товара
Response:
```json
[
    {
        "id": 1,
        "final_price": 7,
        "availability": true,
        "product": {
            "id": 1,
            "name": "Air Force 1",
            "bucket_link": "/buck",
            "description": "desc",
            "sku": "air_force_1",
            "available_flag": true,
            "last_upd": "2023-04-07T15:28:17Z",
            "add_date": "2023-04-07",
            "fit": 1,
            "rel_num": 1,
            "gender": {
                "id": 1,
                "name": "M"
            },
            "brands": [
                {
                    "id": 1,
                    "name": "Nike"
                }
            ],
            "categories": [
                {
                    "id": 1,
                    "name": "Sport"
                }
            ],
            "tags": [
                {
                    "id": 1,
                    "name": "Style"
                }
            ]
        },
        "size": {
            "id": 1,
            "INT": "12",
            "US": "12",
            "UK": "12",
            "EU": "12",
            "IT": "12",
            "RU": "12",
            "product": {
                "id": 1,
                "name": "Air Force 1",
                "bucket_link": "/buck",
                "description": "desc",
                "sku": "air_force_1",
                "available_flag": true,
                "last_upd": "2023-04-07T15:28:17Z",
                "add_date": "2023-04-07",
                "fit": 1,
                "rel_num": 1,
                "gender": 1,
                "brands": [
                    1
                ],
                "categories": [
                    1
                ],
                "tags": [
                    1
                ]
            }
        },
        "currency": {
            "id": 2,
            "name": "pending"
        },
        "delivery_type": {
            "id": 1,
            "name": "Самолёт"
        },
        "platform": {
            "id": 1,
            "platform": "Poizon",
            "site": "/poizon"
        }
    }
]
```
[:arrow_up:Назад](#SellOut API)
### 2. `[GET][Anon] product_unit/product_main/<product_id>/<user_id>` "картока товара" (если пользователь не авторизован user_id = 0)
Response:
```json
{
    "id": 1,
    "name": "Air Force 1",
    "bucket_link": "/buck",
    "description": "desc",
    "sku": "air_force_1",
    "available_flag": true,
    "last_upd": "2023-04-07T15:28:17Z",
    "add_date": "2023-04-07",
    "fit": 1,
    "rel_num": 1,
    "gender": {
        "id": 1,
        "name": "M"
    },
    "brands": [
        {
            "id": 1,
            "name": "Nike"
        }
    ],
    "categories": [
        {
            "id": 1,
            "name": "Sport"
        }
    ],
    "tags": [
        {
            "id": 1,
            "name": "Style"
        }
    ],
    "min_price": 7,
    "in_wishlist": true
}

```
[:arrow_up:Назад](#SellOut API)

## WishList API
