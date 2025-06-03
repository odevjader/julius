# Julião: Seu Coach Financeiro Linha Dura

**Status do Projeto:** Em Desenvolvimento (Fase de Planejamento do MVP Concluída, Início do Desenvolvimento)

## Descrição Curta

Julião é um aplicativo de gestão financeira pessoal projetado para ajudar os usuários a tomarem controle de suas finanças com uma abordagem direta, bem-humorada e um toque de "linha dura". A interação principal para registro de transações e consultas rápidas ocorre via WhatsApp, onde a Inteligência Artificial "Julião" atua como um coach financeiro com uma personalidade única. Um dashboard web moderno complementa a experiência, oferecendo visualizações detalhadas, relatórios e configurações.

## A Persona "Julião"

Inspirado no icônico personagem Julius Rock da série "Todo Mundo Odeia o Chris", o assistente de IA do aplicativo é:

* **Extremamente Econômico:** Sabe o valor de cada centavo.
* **Direto e Sem Rodeios:** Fala a verdade sobre seus gastos, doa a quem doer.
* **Humorístico e Debochado:** Usa frases de efeito e ironia para tornar a gestão financeira menos intimidante e mais memorável.
* **Educador "Linha Dura":** Ajuda a distinguir necessidades de desejos, incentivando a responsabilidade financeira.
* **Foco no Essencial:** Sem funcionalidades complexas desnecessárias, apenas o que você precisa para não "torrar" seu dinheiro à toa.

## Funcionalidades Principais do MVP

* **Interação via WhatsApp com a IA Julião:**
    * Registro de despesas (avulsas e parceladas) e receitas usando linguagem natural.
    * Gestão de múltiplas contas bancárias/carteiras.
    * Gestão de múltiplos cartões de crédito (acompanhamento de faturas, registro de pagamentos).
    * Registro e acompanhamento de compras parceladas.
    * Criação e gerenciamento de transações recorrentes (contas a pagar e recebimentos).
    * Transferências entre contas.
    * Consultas de saldo, extrato de faturas, próximas parcelas/recorrências.
    * Lembretes de vencimentos de faturas e contas recorrentes.
    * Respostas e dicas com a personalidade única do Julião.
* **Dashboard Web Moderno:**
    * Configuração inicial de contas, cartões de crédito e transações recorrentes.
    * Visão geral consolidada dos saldos, próximas faturas e resumos mensais.
    * Listagem detalhada de todas as transações com filtros avançados.
    * Seção dedicada para gerenciamento de cartões de crédito (faturas, parcelamentos).
    * Seção dedicada para gerenciamento de transações recorrentes.
    * Relatórios visuais simples (ex: despesas por categoria, evolução de saldo).

## Backend API (Julião API)

The backend for the Julião application is built using FastAPI and is located in the `juliao_api/` directory. It's designed to be run with Docker for both development and production.

### Development Setup

1.  **Navigate to the API directory:**
    ```bash
    cd juliao_api
    ```
2.  **Create your development environment file:**
    Copy the example environment file `.env.example` to `.env.dev` and fill in any necessary local configurations.
    ```bash
    cp .env.example .env.dev
    ```
    For the basic setup, the defaults in `.env.example` for `DATABASE_URL_LOCAL` should work with the provided `docker-compose.yml`.

3.  **Build and run the services using Docker Compose:**
    ```bash
    docker-compose up --build -d
    ```
    The `-d` flag runs the containers in detached mode.

4.  **Accessing the API:**
    Once the containers are running, the API will be accessible at `http://localhost:8001`.
    You can check the health of the API by navigating to `http://localhost:8001/health`.

### Project Structure

The `juliao_api/` directory follows a standard structure for FastAPI applications:

-   `app/`: Contains the core application logic, including:
    -   `main.py`: The entry point for the FastAPI application.
    -   `core/`: Configuration, settings.
    -   `apis/`: API versioning and endpoint definitions.
    -   `models/`: Pydantic models for request/response validation.
    -   `schemas/`: (Alternative or complementary to `models/` for Pydantic schemas, if needed).
    -   `services/`: Business logic.
    -   `db/`: Database session management and configuration.
    -   `crud/`: Functions for Create, Read, Update, Delete operations.
-   `tests/`: Unit and integration tests.
-   `Dockerfile`: For building the production Docker image.
-   `docker-compose.yml`: For local development orchestration.
-   `pyproject.toml` & `poetry.lock`: Dependency management with Poetry.
-   `.env.example`: Example environment variables.
-   `alembic.ini`: Alembic configuration for database migrations.
