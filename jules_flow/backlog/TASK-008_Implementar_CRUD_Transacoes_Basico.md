---
id: TASK-008
title: "Implementar CRUD para Transações (Transacao) (Básico)"
epic: "Backend"
status: backlog
priority: medium
dependencies: ["TASK-005", "TASK-006", "TASK-007"] # Depends on Conta and Categoria
assignee: Jules
---

### Descrição

Implementar as operações CRUD básicas para `Transacao` (sem parcelamento inicialmente) conforme Seção 2.3 da `docs/ESPECIFICACAO_BACKEND_MVP.md`.
Endpoints: `POST /api/v1/transacoes`, `GET /api/v1/transacoes` (com filtros), `GET /api/v1/transacoes/{id_transacao}`, `PUT /api/v1/transacoes/{id_transacao}`, `DELETE /api/v1/transacoes/{id_transacao}`.
Implementar lógica de atualização de saldo da `Conta` associada.

### Critérios de Aceitação

- [ ] Endpoints CRUD para `Transacao` (básicos) estão implementados.
- [ ] Saldo da conta é atualizado corretamente ao criar/atualizar/deletar transação.
- [ ] Filtros para `GET /api/v1/transacoes` funcionam (conta, período, tipo, categoria).
- [ ] Testes cobrem a funcionalidade e a lógica de atualização de saldo.

### Arquivos Relevantes

* `docs/ESPECIFICACAO_BACKEND_MVP.md` (Seção 2.3)
* `juliao_api/app/models/finance_models.py` (para `Transacao`)
* `juliao_api/app/schemas/finance_schemas.py` (para Schemas Pydantic de `Transacao`)
* `juliao_api/app/api/v1/endpoints/transacoes.py` (novo)
* `juliao_api/app/services/transacao_service.py` (novo)
* `juliao_api/app/crud/crud_transacao.py` (novo)

### Relatório de Execução

(Esta seção deve ser deixada em branco)
