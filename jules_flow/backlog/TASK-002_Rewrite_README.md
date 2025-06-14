---
id: TASK-002
title: "Reescrever README e Mover Setup para Docs (pt-br)"
epic: "Documentação"
status: backlog
priority: medium
dependencies: []
assignee: Jules
---

### Descrição

O README.md principal (`/README.md`) deve ser reescrito em português brasileiro (pt-br) para ser mais conciso, focando na descrição geral do projeto Julião, sua proposta de valor e na persona "Julião".

As instruções detalhadas de setup do backend (Julião API), que atualmente residem no README principal, devem ser movidas integralmente para um novo arquivo. Este novo arquivo deve ser criado em `docs/CONFIGURACAO_DESENVOLVIMENTO.md`. O conteúdo movido também deve ser revisado e, se necessário, adaptado para português brasileiro (pt-br), garantindo clareza e usabilidade para o desenvolvedor.

### Critérios de Aceitação

- [ ] O arquivo `README.md` (localizado na raiz do projeto) está em português brasileiro (pt-br).
- [ ] O `README.md` principal está visivelmente mais conciso e focado nos aspectos gerais do projeto.
- [ ] Todas as seções relacionadas ao setup de desenvolvimento do backend (Julião API), incluindo estrutura do projeto backend e comandos Alembic, foram removidas do `README.md` principal.
- [ ] Um novo arquivo chamado `CONFIGURACAO_DESENVOLVIMENTO.md` foi criado dentro da pasta `docs/`.
- [ ] O arquivo `docs/CONFIGURACAO_DESENVOLVIMENTO.md` contém todas as instruções de setup do backend que foram removidas do README principal.
- [ ] O conteúdo em `docs/CONFIGURACAO_DESENVOLVIMENTO.md` está em português brasileiro (pt-br) e é claro e suficiente para um desenvolvedor configurar o ambiente.

### Arquivos Relevantes

* `README.md`
* `docs/`
* `jules_flow/templates/task_template.md`

### Relatório de Execução

(Esta seção deve ser deixada em branco)
