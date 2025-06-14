---
id: TASK-007
title: "Implementar CRUD para Categorias (Categoria)"
epic: "Backend"
status: backlog
priority: medium
dependencies: ["TASK-005"]
assignee: Jules
---

### Descrição

Implementar as operações CRUD para o modelo `Categoria` conforme a Seção 2.2 da `docs/ESPECIFICACAO_BACKEND_MVP.md`.
Endpoints: `POST /api/v1/categorias`, `GET /api/v1/categorias`, `GET /api/v1/categorias/{id_categoria}`, `PUT /api/v1/categorias/{id_categoria}`, `DELETE /api/v1/categorias/{id_categoria}`.
Considerar categorias padrão do sistema versus categorias do usuário.

### Critérios de Aceitação

- [ ] Endpoints CRUD para `Categoria` estão implementados e funcionais.
- [ ] Validações de request e formatos de response corretos.
- [ ] Usuário pode gerenciar suas próprias categorias.
- [ ] Deleção de categoria considera impacto em transações existentes.
- [ ] Testes cobrem a funcionalidade.

### Arquivos Relevantes

* `docs/ESPECIFICACAO_BACKEND_MVP.md` (Seção 2.2)
* `juliao_api/app/models/finance_models.py` (para `Categoria`)
* `juliao_api/app/schemas/finance_schemas.py` (para Schemas Pydantic de `Categoria`)
* `juliao_api/app/api/v1/endpoints/categorias.py` (novo)
* `juliao_api/app/services/categoria_service.py` (novo)
* `juliao_api/app/crud/crud_categoria.py` (novo)

### Relatório de Execução

(Esta seção deve ser deixada em branco)
