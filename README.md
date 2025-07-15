# Shopping List

O projeto tem como objetivo colocar em prática os fundamentos de criação de uma API e autenticação via Token

## Stack utilizada

- Django Rest framework (https://www.django-rest-framework.org/)
- Python 3.13 (https://www.python.org/)


## Documentação da API

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



