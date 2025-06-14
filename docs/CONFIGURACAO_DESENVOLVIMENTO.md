# Configuração do Ambiente de Desenvolvimento da Julião API

A API backend para a aplicação Julião é construída usando FastAPI e está localizada no diretório `juliao_api/`. Ela é projetada para ser executada com Docker tanto para desenvolvimento quanto para produção.

## Configuração de Desenvolvimento

1.  **Navegue até o diretório da API:**
    ```bash
    cd juliao_api
    ```
2.  **Crie seu arquivo de ambiente de desenvolvimento:**
    Copie o arquivo de ambiente de exemplo `.env.example` para `.env.dev` e preencha quaisquer configurações locais necessárias.
    ```bash
    cp .env.example .env.dev
    ```
    Para a configuração básica, os padrões em `.env.example` para `DATABASE_URL_LOCAL` devem funcionar com o `docker-compose.yml` fornecido.

3.  **Construa e execute os serviços usando Docker Compose:**
    ```bash
    docker-compose up --build -d
    ```
    O sinalizador `-d` executa os contêineres em modo desanexado (detached).

4.  **Acessando a API:**
    Assim que os contêineres estiverem em execução, a API estará acessível em `http://localhost:8001`.
    Você pode verificar a saúde da API navegando para `http://localhost:8001/health`.

## Estrutura do Projeto

O diretório `juliao_api/` segue uma estrutura padrão para aplicações FastAPI:

*   `app/`: Contém a lógica principal da aplicação, incluindo:
    *   `main.py`: O ponto de entrada para a aplicação FastAPI.
    *   `core/`: Configurações.
    *   `apis/`: Versionamento da API e definições de endpoint.
    *   `models/`: Modelos Pydantic para validação de requisição/resposta. (Nota: No projeto atual, são modelos SQLModel que também servem para validação Pydantic).
    *   `schemas/`: (Alternativa ou complementar a `models/` para esquemas Pydantic, se necessário).
    *   `services/`: Lógica de negócios.
    *   `db/`: Gerenciamento de sessão de banco de dados e configuração.
    *   `crud/`: Funções para operações de Criar, Ler, Atualizar, Deletar (CRUD).
*   `tests/`: Testes unitários e de integração.
*   `Dockerfile`: Para construir a imagem Docker de produção.
*   `docker-compose.yml`: Para orquestração de desenvolvimento local.
*   `pyproject.toml` & `poetry.lock`: Gerenciamento de dependências com Poetry.
*   `.env.example`: Variáveis de ambiente de exemplo.
*   `alembic.ini`: Configuração do Alembic para migrações de banco de dados.
*   `alembic/`: Contém os scripts de migração e configuração do Alembic.

## Migrações de Banco de Dados (Alembic)

Alterações no esquema do banco de dados são gerenciadas usando Alembic. Os scripts de migração estão localizados no diretório `juliao_api/alembic/versions/`. Certifique-se de que o contêiner do banco de dados de desenvolvimento Docker esteja em execução antes de executar os comandos do Alembic.

**Principais comandos do Alembic (executar de dentro do diretório `juliao_api/`):**

*   **Certifique-se de que o contêiner do banco de dados está em execução:**
    ```bash
    docker-compose up -d db
    ```
    (Se você estiver executando o serviço completo da API com `docker-compose up -d`, o serviço `db` já estará ativo.)

*   **Aplicar todas as migrações pendentes:**
    Este comando atualizará o esquema do seu banco de dados para a versão mais recente.
    ```bash
    poetry run alembic upgrade head
    ```

*   **Gerar um novo script de migração:**
    Após fazer alterações nas suas definições SQLModel em `juliao_api/app/models/`, você precisará gerar um novo script de migração.
    ```bash
    poetry run alembic revision -m "sua_mensagem_descritiva_da_migracao"
    ```
    Inspecione o script gerado em `juliao_api/alembic/versions/` e preencha as funções `upgrade()` e `downgrade()` conforme necessário.

*   **Verificar a revisão atual do banco de dados:**
    ```bash
    poetry run alembic current
    ```

*   **Mostrar histórico de migrações:**
    ```bash
    poetry run alembic history
    ```

**Importante:**
*   O Alembic usa a `DATABASE_URL_LOCAL` do seu arquivo `.env.dev` (dentro de `juliao_api/`) para se conectar ao banco de dados. Certifique-se de que isso esteja configurado corretamente.
*   O esquema inicial do banco de dados baseado nos SQLModels definidos foi criado e versionado.
```
