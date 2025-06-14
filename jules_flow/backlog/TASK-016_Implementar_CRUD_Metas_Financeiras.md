---
id: TASK-016
title: "(Preliminar) Implementar CRUD para Metas Financeiras (MetaFinanceira)"
epic: "Backend"
status: backlog
priority: low
dependencies: ["TASK-005", "TASK-006"] # Pode depender de Conta
assignee: Jules
---

### Descrição

Implementação preliminar do CRUD para `MetaFinanceira`, conforme Seção 4.4 da `docs/ESPECIFICACAO_BACKEND_MVP.md`.
Modelo `MetaFinanceira` (id_usuario, nome, valor_alvo, data_alvo, valor_atual, id_conta_associada).
Endpoints CRUD.
Lógica para atualizar `valor_atual` com transações de "depósito na meta".

### Critérios de Aceitação

- [ ] Endpoints CRUD para `MetaFinanceira` funcionam.
- [ ] `valor_atual` da meta é atualizado por transações específicas.
- [ ] Testes cobrem a funcionalidade.

### Arquivos Relevantes

* `docs/ESPECIFICACAO_BACKEND_MVP.md` (Seção 4.4)
* `juliao_api/app/models/finance_models.py` (novo `MetaFinanceira`)
* `juliao_api/app/schemas/finance_schemas.py`
* `juliao_api/app/api/v1/endpoints/metas_financeiras.py` (novo)
* `juliao_api/app/services/meta_financeira_service.py` (novo)
* `juliao_api/app/crud/crud_meta_financeira.py` (novo)

### Relatório de Execução

(Esta seção deve ser deixada em branco)
