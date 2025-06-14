# Roadmap do Projeto Julião

Este documento descreve o progresso do desenvolvimento e os planos futuros para o aplicativo de finanças pessoais Julião.

## Fase 1: Fundação e Configuração Principal (Concluída)

*   **Configuração Inicial do Projeto Backend (FastAPI, Docker, Poetry)**
    *   Estrutura do projeto estabelecida para `juliao_api/`.
    *   FastAPI integrado com um endpoint básico de verificação de saúde.
    *   Poetry configurado para gerenciamento de dependências.
    *   Docker (`Dockerfile`, `docker-compose.yml`) configurado para ambientes de desenvolvimento e produção.
    *   `.env.example` criado para configuração de ambiente.
*   **Definição dos Modelos de Dados Principais (SQLModel)**
    *   Todas as entidades centrais (PerfilDeUsuario, Conta, Transacao, Categoria, CartaoDeCredito, Parcela, TransacaoRecorrente) e seus relacionamentos definidos usando SQLModel em `juliao_api/app/models/`.
*   **Configuração do Banco de Dados e Migrações (Alembic & SQLModel)**
    *   Esquema inicial do banco de dados criado e versionado usando Alembic. Alembic configurado para gerenciar migrações baseadas nas definições SQLModel.
*   **Definição da Persona "Julião" e Escopo do MVP**
    *   Conceito central do assistente de IA e funcionalidades mínimas viáveis estabelecidas.

## Fase 2: Funcionalidades Essenciais do Backend

*   **Autenticação & Autorização de Usuário**
    *   Implementar autenticação baseada em JWT (potencialmente aproveitando Supabase Auth).
    *   Definir endpoints de registro e login de usuário.
    *   Configurar hashing de senha e mecanismos de recuperação.
*   **Operações CRUD Básicas para Modelos Principais**
    *   Desenvolver endpoints da API para criar, ler, atualizar e deletar entidades de dados centrais (ex: contas, transações, categorias).
*   **Integração Inicial com Supabase**
    *   Conectar ao Supabase para banco de dados e, potencialmente, autenticação.
    *   Explorar Supabase para armazenamento de arquivos (se necessário para comprovantes, etc.).

## Fase 3: Desenvolvimento do Frontend e Páginas de Apresentação

*   **Desenvolvimento do Dashboard Web (React.js na pasta `frontend/`)**
    *   Configuração inicial do projeto React.js em `frontend/`.
    *   Design e implementação das principais visualizações do dashboard:
        *   Visão geral de contas e saldos.
        *   Listagem e filtros de transações.
        *   Gerenciamento de cartões de crédito.
        *   Gerenciamento de transações recorrentes.
    *   Integração com a API Julião para consumo de dados.
    *   Implementação da interface de usuário para configuração inicial de contas e categorias.
*   **Criação das Páginas de Apresentação (Estáticas na pasta `site/`)**
    *   Desenvolvimento de landing pages para marketing e apresentação do produto Julião.
    *   Estas páginas serão servidas a partir da pasta `site/` e podem ser desenvolvidas com HTML/CSS simples ou um gerador de site estático.

## Fase 4: Funcionalidades Avançadas e Integrações

*   **Interação via WhatsApp (Integração com Gateway WAHA)**
    *   Configuração e integração de um gateway WhatsApp (como o WAHA) para permitir:
        *   Registro de despesas e receitas via mensagem.
        *   Consultas de saldo e extrato.
*   **Melhorias na Gestão de Transações**
    *   Suporte a transações parceladas.
    *   Lembretes e notificações (vencimentos de contas, faturas de cartão).
*   **Recursos de Orçamentação**
    *   Definição de orçamentos por categoria.
    *   Acompanhamento de gastos versus orçamento.
*   **Metas Financeiras**
    *   Permitir que usuários criem e acompanhem metas de economia.
*   **Relatórios e Análises (Versão Inicial)**
    *   Relatórios visuais básicos (ex: despesas por categoria, evolução de saldo).

## Fase 5: Refinamentos e Recursos Adicionais

*   **Inteligência Financeira com IA (Integração Gemini API)**
    *   Explorar a integração com a API Gemini para fornecer insights e dicas financeiras personalizadas com a persona "Julião".
*   **Relatórios Avançados e Visualização de Dados**
    *   Dashboards mais detalhados e personalizáveis.
*   **Ferramentas de Gestão de Dívidas** (se aplicável)
*   **Suporte a Múltiplas Moedas** (se aplicável)

## Fase 6: Testes, Implantação e Iteração Contínua

*   **Testes Abrangentes**
    *   Testes unitários, de integração e de ponta a ponta.
*   **Implantação do MVP**
    *   Configuração de servidor (VPS, Docker, Nginx, Certbot).
    *   Processo de deploy automatizado.
*   **Coleta de Feedback e Melhorias Contínuas**
    *   Monitoramento da aplicação.
    *   Priorização de correções e novas funcionalidades com base no uso e feedback.

## Stack Tecnológico Principal

*   **Backend:** FastAPI (Python)
*   **Frontend (Dashboard):** React.js (na pasta `frontend/`)
*   **Páginas de Apresentação:** HTML/CSS ou Gerador de Site Estático (na pasta `site/`)
*   **Banco de Dados:** PostgreSQL (via Supabase)
*   **Containerização:** Docker
*   **Gerenciamento de Dependências (Python):** Poetry
*   **Migrações:** Alembic
*   **Autenticação:** JWT (potencialmente via Supabase Auth)
*   **Serviços em Nuvem (Potenciais):** Supabase, Gemini API, Servidor VPS.

---
*Este roadmap é um documento vivo e será atualizado conforme o projeto avança.*
