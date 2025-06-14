---
id: TASK-009
title: "Implementar CRUD para Cartões de Crédito (CartaoDeCredito) e Gestão de Faturas"
epic: "Backend"
status: backlog
priority: medium
dependencies: ["TASK-005", "TASK-008"]
assignee: Jules
---

### Descrição

Implementar CRUD para `CartaoDeCredito` e lógica de visualização de faturas, conforme Seção 2.4 da `docs/ESPECIFICACAO_BACKEND_MVP.md`.
Endpoints CRUD para `CartaoDeCredito`.
Endpoints para listar faturas (`GET /api/v1/cartoes/{id_cartao}/faturas`) e detalhes de fatura.
Definir como as transações de cartão de crédito são associadas às faturas. Considerar se o modelo `FaturaCartao` precisa ser persistido ou pode ser gerado dinamicamente.

### Critérios de Aceitação

- [ ] Endpoints CRUD para `CartaoDeCredito` funcionam.
- [ ] Endpoints de listagem e detalhe de faturas funcionam.
- [ ] Transações de despesa podem ser corretamente associadas a um cartão e sua fatura correspondente.
- [ ] Testes cobrem a funcionalidade.

### Arquivos Relevantes

* `docs/ESPECIFICACAO_BACKEND_MVP.md` (Seção 2.4)
* `juliao_api/app/models/finance_models.py` (para `CartaoDeCredito`, e possivelmente novo `FaturaCartao`)
* `juliao_api/app/schemas/finance_schemas.py`
* `juliao_api/app/api/v1/endpoints/cartoes.py` (novo)
* `juliao_api/app/services/cartao_service.py` (novo)
* `juliao_api/app/crud/crud_cartao.py` (novo)

### Relatório de Execução

(Esta seção deve ser deixada em branco)
