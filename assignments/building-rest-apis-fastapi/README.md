# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Construa uma API REST para gerenciar uma coleção de livros usando FastAPI. Você praticará rotas HTTP, validação de dados com Pydantic e respostas apropriadas para recursos existentes ou não encontrados.

## 📝 Tasks

### 🛠️ Criar a Rota para Listar Livros

#### Descrição

Instale as dependências com `pip install "fastapi[standard]"` e inicie a aplicação com `fastapi dev starter-code.py`. Em seguida, complete o código inicial para criar uma rota que retorne todos os livros armazenados na lista em memória e explore os endpoints pela documentação interativa em `/docs`.

#### Requisitos
O programa concluído deve:

- Iniciar uma aplicação FastAPI usando o arquivo de código inicial
- Implementar `GET /books` para retornar a coleção de livros como JSON
- Retornar uma lista vazia quando não houver livros
- Permitir que a rota seja testada em `/docs`

### 🛠️ Cadastrar Livros

#### Descrição

Crie uma rota para cadastrar um livro. Use o modelo Pydantic fornecido para validar os dados recebidos e atribua um identificador ao novo recurso.

#### Requisitos
O programa concluído deve:

- Implementar `POST /books` recebendo título e autor no corpo da requisição
- Rejeitar título ou autor vazios usando a validação do modelo
- Adicionar o livro à coleção em memória com um identificador único
- Retornar o livro criado com o status HTTP `201 Created`

Exemplo de corpo da requisição:

```json
{
  "title": "The Hobbit",
  "author": "J. R. R. Tolkien"
}
```

### 🛠️ Gerenciar Livros por Identificador

#### Descrição

Implemente operações para consultar, atualizar e remover um livro específico. Quando o identificador não corresponder a nenhum livro, informe que o recurso não foi encontrado.

#### Requisitos
O programa concluído deve:

- Implementar `GET /books/{book_id}` para retornar um livro específico
- Implementar `PUT /books/{book_id}` para atualizar o título e o autor
- Implementar `DELETE /books/{book_id}` para remover o livro
- Retornar status HTTP `404 Not Found` quando o livro não existir
- Retornar status HTTP `204 No Content` após uma remoção bem-sucedida
