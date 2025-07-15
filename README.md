
# Shopping List

Projeto desenvolvido para aperfeiçoar o uso de API (Application Programming Interface), colocando em prática os metódos básicos e avançados.

Utilizado serializers personalizados para renderizar os models. Usado no projeto também a utilização de Token para permitir o usuário utilizar funções da aplicação.

## Stack utilizada

- Django Rest framework (https://www.django-rest-framework.org/)
- Python 3.13 (https://www.python.org/)


## Documentação da API
#### Rotas
```http
  GET /api/v1/users/
  GET /api/v1/products/
  GET /api/v1/categories/
  GET /api/v1/carts/
  GET /api/v1/carts/items/
```

#### Retorna todos os itens

```http
  GET /api/v1/carts/items/
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `Token` | `string` | **Obrigatório**. O token do seu usuário |

#### Retorna um item

```http
  GET /api/v1/carts/items/${id}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `int` | **Obrigatório**. O ID do item que você quer |



