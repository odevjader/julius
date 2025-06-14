---
id: TASK-013
title: "(Preliminar) Implementar Webhook WhatsApp (WAHA) e Processamento Básico"
epic: "Backend"
status: backlog
priority: low # Fase 4, pode ser menor prioridade inicial
dependencies: ["TASK-005", "TASK-008"]
assignee: Jules
---

### Descrição

Implementação preliminar do webhook para receber mensagens do WAHA e processamento básico de comandos, conforme Seção 4.1 da `docs/ESPECIFICACAO_BACKEND_MVP.md`.
Endpoint: `POST /api/v1/whatsapp/webhook`.
Lógica para identificar usuário pelo telefone e processar comandos simples (registrar despesa/receita, consultar saldo) usando palavras-chave ou NLP muito básico.

### Critérios de Aceitação

- [ ] Endpoint `POST /api/v1/whatsapp/webhook` recebe e processa dados do WAHA.
- [ ] Usuário é identificado (mock ou real, se possível).
- [ ] Comandos básicos de registro de transação e consulta de saldo são processados.
- [ ] Resposta adequada é formatada para o WAHA.
- [ ] Testes (mockando WAHA) cobrem a funcionalidade.

### Arquivos Relevantes

* `docs/ESPECIFICACAO_BACKEND_MVP.md` (Seção 4.1)
* `juliao_api/app/api/v1/endpoints/whatsapp.py` (novo)
* `juliao_api/app/services/whatsapp_service.py` (novo)
* `juliao_api/app/nlp/basic_parser.py` (novo, para NLP básico)

### Relatório de Execução

(Esta seção deve ser deixada em branco)
