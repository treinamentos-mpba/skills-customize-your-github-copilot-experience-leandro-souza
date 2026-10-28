# 📘 Assignment: Async Programming with FastAPI

## 🎯 Objective

Aprofunde o uso de FastAPI implementando operações assíncronas com `async`/`await`. Você vai agregar resultados de várias fontes simuladas usando `asyncio.gather` e comparar execução concorrente e sequencial.

## 📝 Tasks

### 🛠️ Simular Consultas Assíncronas

#### Descrição

Complete as funções de consulta no código inicial. Cada função deve simular uma operação de I/O, como consultar um serviço remoto, sem fazer uma chamada real à rede.

#### Requisitos
O programa concluído deve:

- Implementar `fetch_inventory()`, `fetch_shipping()` e `fetch_payments()` como funções assíncronas
- Simular uma espera de um segundo em cada função usando `await asyncio.sleep(1)`
- Retornar um dicionário com o nome do serviço e o status `ok`

### 🛠️ Agregar Resultados Concorrentemente

#### Descrição

Crie um endpoint que consulte os três serviços ao mesmo tempo e retorne os resultados em uma única resposta JSON.

#### Requisitos
O programa concluído deve:

- Implementar `GET /dashboard` como uma rota assíncrona do FastAPI
- Usar `asyncio.gather` para aguardar as três consultas concorrentemente
- Retornar os três resultados em uma chave `services`
- Permitir que a resposta seja explorada em `/docs`

Exemplo de resposta:

```json
{
  "services": [
    {"service": "inventory", "status": "ok"},
    {"service": "shipping", "status": "ok"},
    {"service": "payments", "status": "ok"}
  ]
}
```

### 🛠️ Comparar Execução Concorrente e Sequencial

#### Descrição

Implemente um endpoint de comparação que execute as mesmas consultas uma após a outra e meça o tempo total. Compare a duração com a rota concorrente, sem assumir um tempo exato de execução.

#### Requisitos
O programa concluído deve:

- Implementar `GET /dashboard/sequential` aguardando cada consulta antes de iniciar a próxima
- Medir a duração usando `time.perf_counter()`
- Retornar os resultados e a duração medida em segundos
- Observar que a execução concorrente tende a levar menos tempo do que a sequencial
