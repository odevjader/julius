---
id: TASK-012
title: "Implementar Integração com Supabase Storage para Comprovantes"
epic: "Backend"
status: backlog
priority: medium
dependencies: ["TASK-005", "TASK-008"]
assignee: Jules
---

### Descrição

Implementar a integração com Supabase Storage para upload e download de comprovantes de transação, conforme Seção 3 da `docs/ESPECIFICACAO_BACKEND_MVP.md`.
Endpoints: `POST /api/v1/transacoes/{id_transacao}/upload_comprovante`, `GET /api/v1/transacoes/{id_transacao}/comprovante`.
Configurar buckets e políticas de acesso no Supabase (manual ou via script, se possível).
API Julião deve intermediar os uploads/downloads.

### Critérios de Aceitação

- [ ] Usuário pode fazer upload de um comprovante para uma transação.
- [ ] Comprovante é armazenado no Supabase Storage.
- [ ] Link/path do comprovante é associado à transação no banco de dados.
- [ ] Usuário pode visualizar/baixar o comprovante associado.
- [ ] Acesso aos comprovantes é restrito ao proprietário.
- [ ] Testes cobrem a funcionalidade.

### Arquivos Relevantes

* `docs/ESPECIFICACAO_BACKEND_MVP.md` (Seção 3)
* `juliao_api/app/services/storage_service.py` (novo, para interagir com Supabase Storage)
* `juliao_api/app/api/v1/endpoints/transacoes.py` (modificado)
* `juliao_api/app/core/config.py` (para settings do Supabase Storage)

### Relatório de Execução

(Esta seção deve ser deixada em branco)
