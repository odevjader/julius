---
id: TASK-006
title: "Implementar CRUD para Contas (Conta)"
epic: "Backend"
status: backlog
priority: medium
dependencies: ["TASK-005"] # Depends on auth
assignee: Jules
---

### Descrição

Implementar as operações CRUD (Create, Read, Update, Delete) para o modelo `Conta` conforme a Seção 2.1 da `docs/ESPECIFICACAO_BACKEND_MVP.md`.
Endpoints a serem criados:
- `POST /api/v1/contas`
- `GET /api/v1/contas`
- `GET /api/v1/contas/{id_conta}`
- `PUT /api/v1/contas/{id_conta}`
- `DELETE /api/v1/contas/{id_conta}`
Garantir que todas as operações sejam protegidas por autenticação e associadas ao usuário autenticado. Considerar soft delete.

### Critérios de Aceitação

- [ ] Endpoint `POST /api/v1/contas` cria uma nova conta.
- [ ] Endpoint `GET /api/v1/contas` lista as contas do usuário.
- [ ] Endpoint `GET /api/v1/contas/{id_conta}` retorna a conta especificada.
- [ ] Endpoint `PUT /api/v1/contas/{id_conta}` atualiza a conta.
- [ ] Endpoint `DELETE /api/v1/contas/{id_conta}` deleta a conta (soft delete).
- [ ] Validações de request (payloads) estão implementadas.
- [ ] Respostas estão conforme especificado.
- [ ] Apenas o proprietário da conta pode acessá-la/modificá-la.
- [ ] Testes unitários/integração cobrem todos os endpoints e lógicas.

### Arquivos Relevantes

* `docs/ESPECIFICACAO_BACKEND_MVP.md` (Seção 2.1)
* `juliao_api/app/models/finance_models.py` (para `Conta`)
* `juliao_api/app/schemas/finance_schemas.py` (novo ou atualizado para Schemas Pydantic de `Conta`)
* `juliao_api/app/api/v1/endpoints/contas.py` (novo)
* `juliao_api/app/services/conta_service.py` (novo)
* `juliao_api/app/crud/crud_conta.py` (novo)

### Relatório de Execução

(Esta seção deve ser deixada em branco)
