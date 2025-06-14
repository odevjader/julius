---
id: TASK-015
title: "(Preliminar) Implementar CRUD para Orçamentos (Orcamento)"
epic: "Backend"
status: backlog
priority: low
dependencies: ["TASK-005", "TASK-007"] # Depende de Categoria
assignee: Jules
---

### Descrição

Implementação preliminar do CRUD para `Orcamento`, conforme Seção 4.3 da `docs/ESPECIFICACAO_BACKEND_MVP.md`.
Modelo `Orcamento` (id_usuario, id_categoria, valor_mensal, mes_ano_referencia).
Endpoints CRUD.
Lógica para verificar e atualizar gasto realizado ao registrar transações.

### Critérios de Aceitação

- [ ] Endpoints CRUD para `Orcamento` funcionam.
- [ ] Ao registrar transação de despesa, o gasto no orçamento correspondente é atualizado.
- [ ] Testes cobrem a funcionalidade.

### Arquivos Relevantes

* `docs/ESPECIFICACAO_BACKEND_MVP.md` (Seção 4.3)
* `juliao_api/app/models/finance_models.py` (novo `Orcamento`)
* `juliao_api/app/schemas/finance_schemas.py`
* `juliao_api/app/api/v1/endpoints/orcamentos.py` (novo)
* `juliao_api/app/services/orcamento_service.py` (novo)
* `juliao_api/app/crud/crud_orcamento.py` (novo)

### Relatório de Execução

(Esta seção deve ser deixada em branco)
