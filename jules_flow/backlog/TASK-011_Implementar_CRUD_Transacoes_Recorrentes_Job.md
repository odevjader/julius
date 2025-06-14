---
id: TASK-011
title: "Implementar CRUD para Transações Recorrentes (TransacaoRecorrente) e Job de Criação"
epic: "Backend"
status: backlog
priority: medium
dependencies: ["TASK-005", "TASK-008"]
assignee: Jules
---

### Descrição

Implementar CRUD para `TransacaoRecorrente` e o job agendado (APScheduler) para criar `Transacao` concretas, conforme Seção 2.6 da `docs/ESPECIFICACAO_BACKEND_MVP.md`.
Endpoints CRUD para `TransacaoRecorrente`.
Configurar e implementar job com APScheduler para verificar e criar transações.

### Critérios de Aceitação

- [ ] Endpoints CRUD para `TransacaoRecorrente` funcionam.
- [ ] Job agendado (APScheduler) está configurado.
- [ ] Job cria `Transacao` corretamente com base nas `TransacaoRecorrente` ativas.
- [ ] Testes cobrem o CRUD e a lógica do job.

### Arquivos Relevantes

* `docs/ESPECIFICACAO_BACKEND_MVP.md` (Seção 2.6)
* `juliao_api/app/models/finance_models.py` (para `TransacaoRecorrente`)
* `juliao_api/app/schemas/finance_schemas.py`
* `juliao_api/app/api/v1/endpoints/transacoes_recorrentes.py` (novo)
* `juliao_api/app/services/transacao_recorrente_service.py` (novo)
* `juliao_api/app/crud/crud_transacao_recorrente.py` (novo)
* `juliao_api/app/jobs/recurring_transaction_job.py` (novo)
* `juliao_api/app/core/scheduler.py` (novo, para configurar APScheduler)

### Relatório de Execução

(Esta seção deve ser deixada em branco)
