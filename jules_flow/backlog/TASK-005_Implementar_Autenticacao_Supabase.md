---
id: TASK-005
title: "Implementar Configuração de Autenticação (Supabase & JWT Validation)"
epic: "Backend"
status: backlog
priority: high
dependencies: []
assignee: Jules
---

### Descrição

Configurar a API Julião para validar JWTs emitidos pelo Supabase Auth. Implementar o mecanismo de sincronização de perfil de usuário (`PerfilDeUsuario`) após o primeiro login/registro via Supabase.

Conforme Seção 1 da `docs/ESPECIFICACAO_BACKEND_MVP.md`:
- Integrar com Supabase Auth como provedor principal.
- Validar JWTs (access tokens) enviados no header `Authorization` (Bearer token) usando a chave pública do Supabase.
- Implementar o endpoint `POST /api/v1/users/sync_profile` para criar/atualizar o `PerfilDeUsuario` local com base no ID de usuário do Supabase. Este endpoint deve ser protegido, exigindo um token Supabase válido.
- Garantir que o `id` do `PerfilDeUsuario` local seja o mesmo UUID do usuário no Supabase.
- Proteger todos os endpoints subsequentes da API para que exijam um token JWT válido.

### Critérios de Aceitação

- [ ] A API pode validar corretamente um JWT emitido pelo Supabase Auth.
- [ ] Endpoints protegidos retornam 401/403 para tokens inválidos ou ausentes.
- [ ] O endpoint `POST /api/v1/users/sync_profile` funciona:
    - Cria um `PerfilDeUsuario` local se não existir, usando o ID do token Supabase.
    - Atualiza o `PerfilDeUsuario` se já existir (ex: last_login).
    - Retorna erro se o token Supabase for inválido.
- [ ] Utilitários/dependências para validação de JWT estão configurados no FastAPI.
- [ ] Testes unitários/integração cobrem a validação do token e a lógica de `sync_profile`.
- [ ] A estrutura do `PerfilDeUsuario` está alinhada com `juliao_api/app/models/user_models.py`.

### Arquivos Relevantes

* `docs/ESPECIFICACAO_BACKEND_MVP.md` (Seção 1)
* `juliao_api/app/core/config.py`
* `juliao_api/app/auth/jwt.py` (novo)
* `juliao_api/app/api/v1/endpoints/users.py`
* `juliao_api/app/services/user_service.py` (novo)
* `juliao_api/app/models/user_models.py`
* `juliao_api/app/main.py`

### Relatório de Execução

(Esta seção deve ser deixada em branco)
