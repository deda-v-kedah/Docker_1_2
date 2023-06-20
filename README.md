# Help


## Запуск:

билд:
```
docker build . --tag=my_django_app_1
```
запуск:
```
docker run -d -p 8000:8000 my_django_app_1
```

## Комманды:

[requests-examples.http](https://github.com/deda-v-kedah/homeworks/blob/video/3.2-crud/stocks_products/requests-examples.http).<br>
при смене порта-менять @baseUrl

<br>

```
# создание продукта
POST {{baseUrl}}/products/

Content-Type: application/json
{
  "title": "Помидор",
  "description": "Лучшие помидоры на рынке"
}


# получение продуктов
GET {{baseUrl}}/products/


# обновление продукта
PATCH {{baseUrl}}/products/1/

Content-Type: application/json
{
  "description": "Самые сочные и ароматные помидорки"
}


# удаление продукта
DELETE {{baseUrl}}/products/1/


# поиск продуктов по названию и описанию
GET {{baseUrl}}/products/?search=помидор


# создание склада
POST {{baseUrl}}/stocks/

Content-Type: application/json
{
  "address": "Addres",
  "positions": [
    {
      "product": 1,
      "quantity": 20,
      "price": 120.50
    },
    {
      "product": 1,
      "quantity": 100,
      "price": 180
    }
  ]
}



# обновляем записи на складе
PATCH {{baseUrl}}/stocks/4/

Content-Type: application/json
{
  "positions": [
    {
      "product": 2,
      "quantity": 100,
      "price": 130.80
    },
    {
      "product": 3,
      "quantity": 243,
      "price": 145
    }
  ]
}


# поиск складов, где есть определенный продукт
GET {{baseUrl}}/stocks/?products=2


# поиск складов, где есть определенный продукт
GET {{baseUrl}}/stocks/?search=о


```



