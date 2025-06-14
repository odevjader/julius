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

- **Configuração Inicial:**
    - Configurado `Settings` em `juliao_api/app/core/config.py` para carregar `DATABASE_URL`, `SUPABASE_URL`, `SUPABASE_KEY`, `SUPABASE_JWT_SECRET`, `SUPABASE_JWKS_URL` do ambiente.
    - Implementado gerenciamento de sessão de banco de dados em `juliao_api/app/db/session.py` com `get_db_session`.
- **Estrutura de Autenticação e Usuário:**
    - Criado diretório `juliao_api/app/auth/` e arquivos `jwt.py`, `dependencies.py`.
    - Criado diretório `juliao_api/app/services/` e arquivo `user_service.py`.
    - Criado `juliao_api/app/api/v1/endpoints/users.py`.
- **Validação de JWT (`juliao_api/app/auth/jwt.py`):**
    - Implementada função `decode_and_validate_jwt` para validar tokens Supabase (RS256 via JWKS URL e fallback HS256 via secret).
    - Inclui busca e cache de JWKS, validação de `kid`, `aud`, `iss`.
    - Adicionado `httpx` às dependências principais em `juliao_api/pyproject.toml`.
    - Definido `TokenData` Pydantic model.
- **Serviço de Perfil de Usuário (`juliao_api/app/services/user_service.py`):**
    - Implementada função `sync_user_profile` para criar ou buscar `UserProfile` local com base no ID do usuário Supabase. (Nota: `UserProfile` model é definido em `user_models.py` como parte da estrutura de modelos, não diretamente nesta task, mas o serviço o utiliza).
- **Endpoint de Sincronização (`juliao_api/app/api/v1/endpoints/users.py`):**
    - Implementado endpoint `POST /api/v1/users/sync_profile`.
    - Protegido pela dependência `get_current_supabase_user_id`.
- **Integração FastAPI (`juliao_api/app/auth/dependencies.py` e `juliao_api/app/main.py`):**
    - Criada dependência `get_current_supabase_user_id` para extrair e validar o ID do usuário Supabase do token JWT.
    - Roteador de usuários incluído na aplicação principal FastAPI em `juliao_api/app/main.py`.
- **Testes:**
    - Criada estrutura de testes em `juliao_api/tests/`.
    - Adicionado `juliao_api/tests/conftest.py` com setup de banco de dados de teste (SQLite in-memory) e `TestClient`.
    - Implementados testes unitários para validação de JWT (`juliao_api/tests/auth/test_jwt.py`).
    - Implementados testes unitários para o serviço de usuário (`juliao_api/tests/services/test_user_service.py`).
    - Implementados testes de integração para o endpoint `sync_profile` (`juliao_api/tests/api/v1/test_users_api.py`).

**Arquivos Modificados/Criados Principais:**
- `juliao_api/app/core/config.py`
- `juliao_api/app/db/session.py`
- `juliao_api/app/auth/jwt.py`
- `juliao_api/app/auth/dependencies.py`
- `juliao_api/app/services/user_service.py`
- `juliao_api/app/api/v1/endpoints/users.py`
- `juliao_api/app/main.py`
- `juliao_api/pyproject.toml`
- `juliao_api/tests/conftest.py`
- `juliao_api/tests/auth/test_jwt.py`
- `juliao_api/tests/services/test_user_service.py`
- `juliao_api/tests/api/v1/test_users_api.py`
- `juliao_api/tests/auth/__init__.py`
- `juliao_api/tests/services/__init__.py`
- `juliao_api/tests/api/__init__.py`
- `juliao_api/tests/api/v1/__init__.py`
