---
id: TASK-014
title: "(Preliminar) Implementar Lógica de Lembretes e Notificações (Job Agendado)"
epic: "Backend"
status: backlog
priority: low
dependencies: ["TASK-009", "TASK-011"] # Relacionado a faturas e trans recorrentes
assignee: Jules
---

### Descrição

Implementação preliminar da lógica de lembretes e notificações via job agendado, conforme Seção 4.2 da `docs/ESPECIFICACAO_BACKEND_MVP.md`.
Job (APScheduler) para verificar contas a pagar/receber e vencimento de faturas.
Mecanismo inicial de notificação (ex: log no sistema ou email para admin).

### Critérios de Aceitação

- [ ] Job agendado está configurado.
- [ ] Job identifica corretamente itens que necessitam de lembrete/notificação.
- [ ] Mecanismo de notificação (log/email) é acionado.
- [ ] Testes cobrem a lógica do job.

### Arquivos Relevantes

* `docs/ESPECIFICACAO_BACKEND_MVP.md` (Seção 4.2)
* `juliao_api/app/jobs/notification_job.py` (novo)
* `juliao_api/app/core/scheduler.py` (modificado)
* `juliao_api/app/services/notification_service.py` (novo)

### Relatório de Execução

(Esta seção deve ser deixada em branco)
