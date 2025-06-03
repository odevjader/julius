## Roadmap Detalhado do Projeto "Julião" (MVP)

**Legenda:**
* ⭐ **Task para Google Jules:** Tarefa específica a ser atribuída ao Google Jules.
* 🧑‍💻 **Task para Orquestrador:** Tarefa a ser executada pelo Orquestrador (você), possivelmente com instruções do Arquiteto ou do Google Jules.
* 🧪 **Teste Unitário/Componente (Jules):** Solicitação para o Jules escrever testes automatizados.
* 🧐 **Teste Manual/Revisão Crítica:** Ponto onde o Orquestrador (você) e o Arquiteto (eu) devem realizar testes manuais e revisões detalhadas.
* 🔒 **Foco em Segurança:** Lembrar de aplicar as melhores práticas de segurança.

---

### **Fase 1: Concepção e Planejamento Detalhado (CONCLUÍDA)**

* **Status:** 100% Concluída.
* **Entregas Principais Realizadas:**
    * Definição da Persona "Julião".
    * Escopo detalhado do MVP.
    * Diretrizes da Experiência do Usuário (UX).
    * Definição da Arquitetura de Alto Nível e Stack Tecnológico.
    * Modelagem do Banco de Dados.
    * Estrutura inicial dos Endpoints da API Backend.
    * Definição do uso do Google Jules como agente de desenvolvimento.
    * Criação do README e deste Roadmap inicial.

---

### **Fase 2: Design (UX/UI) (ADIADA/REVISÃO POSTERIOR)**

* **Objetivo:** Definir visualmente o dashboard web. (Esta fase será revisitada quando absolutamente necessário. As tarefas de design visual complexo não serão atribuídas ao Google Jules).
* **Status:** Adiada

* **2.1. Definição Textual do Guia de Estilo Visual (se necessário antes do design visual):**
    * ⭐ **Task para Google Jules (Opcional):** "Jules, com base nas diretrizes (estilo minimalista, inspiração estrutural no app Organizze, paleta de cores primária azul-lilás-roxo, secundária amarelo/mostarda, fontes sans-serif modernas), gere um *documento textual* descrevendo o guia de estilo visual para o dashboard web do projeto Julião. Inclua:
        1.  Sugestões de códigos hexadecimais para a paleta de cores.
        2.  Sugestões de famílias de fontes e hierarquia de tamanhos/pesos para tipografia.
        3.  Descrição do estilo esperado para componentes básicos (botões, inputs, cards)."
    * 🧐 **Teste Manual/Revisão Crítica:** Validar se a descrição textual do guia de estilo é clara e alinhada com a visão (se esta task for executada).

* **2.2. Criação do Avatar Estilizado "Julião" e Ícones:**
    * **Status:** Adiada (Requer designer gráfico externo ao Google Jules).

* **2.3. Wireframes e Protótipos de Baixa Fidelidade:**
    * **Status:** Adiada (Requer designer gráfico/UX externo ao Google Jules, ou pode ser tentado com ferramentas de prototipagem pelo Orquestrador).

* **2.4. Design de Interface (UI) de Alta Fidelidade (Mockups):**
    * **Status:** Adiada (Requer designer gráfico/UI externo ao Google Jules).

---

### **Fase PREP: Configuração do Ambiente de Desenvolvimento Local (Windows 11 com VSCode)**

* **Objetivo:** Preparar o ambiente local do Orquestrador para desenvolver e testar o projeto Julião.
* **Status:** A Iniciar
* **Responsável Principal:** 🧑‍💻 Orquestrador (com instruções do Arquiteto)

* **PREP.1. Instalação do WSL 2 (Windows Subsystem for Linux):**
    * 🧑‍💻 **Task para Orquestrador:**
        1.  Abra o PowerShell ou o Terminal do Windows como Administrador.
        2.  Execute o comando: `wsl --install`. Este comando habilitará os recursos necessários, baixará o kernel Linux mais recente e instalará o Ubuntu como a distribuição padrão. (Se você já tiver o WSL instalado, mas não o WSL 2, ou quiser outra distribuição, pode precisar de comandos adicionais como `wsl --set-default-version 2` ou `wsl --install -d <NomeDaDistribuicao>`).
        3.  Reinicie o computador quando solicitado.
        4.  Após reiniciar, o Ubuntu será configurado. Você precisará criar um nome de usuário e senha para o seu ambiente Linux no WSL.
    * 🧐 **Teste Manual/Revisão Crítica:** Abra o terminal do Ubuntu (pesquisando "Ubuntu" no menu Iniciar) e verifique se você consegue executar comandos Linux básicos (ex: `ls`, `pwd`).

* **PREP.2. Instalação do Docker Desktop para Windows:**
    * 🧑‍💻 **Task para Orquestrador:**
        1.  Baixe o Docker Desktop para Windows do site oficial da Docker (docker.com).
        2.  Execute o instalador e siga as instruções. Certifique-se de que a opção para usar o backend WSL 2 esteja habilitada durante a instalação ou nas configurações do Docker Desktop após a instalação.
        3.  O Docker Desktop pode exigir uma reinicialização.
    * 🧐 **Teste Manual/Revisão Crítica:** Após a instalação e reinicialização, abra o Docker Desktop. Verifique nas configurações se ele está usando o backend WSL 2. Abra um terminal (PowerShell ou o terminal do Ubuntu no WSL) e execute `docker --version` e `docker compose version` para confirmar a instalação. Tente rodar um contêiner de teste: `docker run hello-world`.

* **PREP.3. Instalação e Configuração do Visual Studio Code (VSCode):**
    * 🧑‍💻 **Task para Orquestrador:**
        1.  Baixe e instale o VSCode do site oficial (code.visualstudio.com), se ainda não o tiver.
        2.  Instale as seguintes extensões essenciais no VSCode:
            * `WSL` (da Microsoft) - Para integração com o ambiente WSL.
            * `Docker` (da Microsoft) - Para gerenciamento de contêineres e Dockerfiles.
            * `Python` (da Microsoft) - Para desenvolvimento Python.
            * `Pylance` (da Microsoft) - Para melhor intellisense Python (geralmente instalado com a extensão Python).
            * `Prettier - Code formatter` (da Prettier) - Para formatação de código (JavaScript, TypeScript, JSON, Markdown, etc.).
            * `ESLint` (da Microsoft, se for usar ESLint para o frontend React) - Para linting de JavaScript/TypeScript.
            * (Opcional) `GitLens` (da GitKraken) - Para funcionalidades avançadas do Git.
            * (Opcional) `Tailwind CSS IntelliSense` (se for usar Tailwind CSS no frontend).
        3.  Após instalar a extensão WSL, você verá um ícone verde no canto inferior esquerdo do VSCode. Clique nele e selecione "Connect to WSL" ou "Open Folder in WSL" para abrir seus projetos diretamente no ambiente Linux.
    * 🧐 **Teste Manual/Revisão Crítica:** Abra o VSCode, conecte-se ao WSL e tente abrir um terminal integrado (Ctrl+`). Ele deve abrir um terminal do Ubuntu.

* **PREP.4. Configuração do Python e Poetry no WSL:**
    * 🧑‍💻 **Task para Orquestrador (dentro do terminal Ubuntu no WSL):**
        1.  Verifique se o Python 3 já está instalado: `python3 --version`. O Ubuntu geralmente vem com uma versão. Para ter mais controle, considere usar `pyenv` para gerenciar múltiplas versões do Python (instalação do `pyenv` pode ser uma subtarefa). Para o MVP, a versão padrão do Ubuntu (se for 3.9+) pode ser suficiente.
        2.  Instale o pip (gerenciador de pacotes Python), se não estiver presente: `sudo apt update && sudo apt install python3-pip -y`.
        3.  Instale o Poetry (gerenciador de dependências e empacotamento para Python): `curl -sSL https://install.python-poetry.org | python3 -`.
        4.  Adicione Poetry ao seu PATH. O instalador do Poetry geralmente fornece o comando para isso, algo como: `export PATH="/home/SEU_USUARIO_LINUX/.local/bin:$PATH"`. Adicione esta linha ao seu arquivo de configuração do shell (ex: `~/.bashrc` ou `~/.zshrc`) e depois execute `source ~/.bashrc` (ou `source ~/.zshrc`).
    * 🧐 **Teste Manual/Revisão Crítica:** Em um novo terminal do Ubuntu no WSL, execute `python3 --version` e `poetry --version` para confirmar que estão instalados e acessíveis.

* **PREP.5. Configuração do Node.js e npm/yarn no WSL:**
    * 🧑‍💻 **Task para Orquestrador (dentro do terminal Ubuntu no WSL):**
        1.  Instale o nvm (Node Version Manager) para gerenciar versões do Node.js: `curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash` (verifique a URL para a versão mais recente do nvm).
        2.  Após a instalação, feche e reabra o terminal, ou execute o comando que o script do nvm indicar para carregar o nvm (geralmente algo como `source ~/.nvm/nvm.sh` ou `source ~/.bashrc`).
        3.  Instale a versão LTS mais recente do Node.js: `nvm install --lts`.
        4.  Defina a versão LTS como padrão: `nvm alias default lts/*`.
        5.  O npm (Node Package Manager) é instalado junto com o Node.js. Se preferir usar o Yarn: `npm install --global yarn`.
    * 🧐 **Teste Manual/Revisão Crítica:** Em um novo terminal do Ubuntu no WSL, execute `node --version`, `npm --version`, e (se instalado) `yarn --version` para confirmar.

* **PREP.6. Configuração do Git:**
    * 🧑‍💻 **Task para Orquestrador (dentro do terminal Ubuntu no WSL, se o Git não estiver instalado):**
        1.  Instale o Git: `sudo apt update && sudo apt install git -y`.
        2.  Configure seu nome e email para o Git:
            `git config --global user.name "Seu Nome"`
            `git config --global user.email "seu.email@exemplo.com"`
        3.  Configure o Git para usar o gerenciador de credenciais do Windows para não ter que digitar senhas do GitHub toda hora (opcional, mas recomendado):
            `git config --global credential.helper "/mnt/c/Program\ Files/Git/mingw64/bin/git-credential-manager.exe"` (o caminho pode variar dependendo de onde o Git para Windows está instalado, se estiver). Uma alternativa mais simples pode ser usar chaves SSH para autenticação com o GitHub.
    * 🧐 **Teste Manual/Revisão Crítica:** Execute `git --version`.

* **PREP.7. Clone do Repositório do Projeto (Quando Criado):**
    * 🧑‍💻 **Task para Orquestrador:** "Quando o repositório GitHub do projeto 'Julião' for criado, clone-o para dentro do seu ambiente WSL (ex: `cd ~ && mkdir projects && cd projects && git clone URL_DO_REPOSITORIO`). Abra a pasta do projeto no VSCode usando a integração WSL."

* **PREP.8. Configuração do Supabase CLI (Opcional para Desenvolvimento Local Avançado):**
    * 🧑‍💻 **Task para Orquestrador (se desejar simular o ambiente Supabase totalmente local):**
        1.  Siga as instruções do Supabase para instalar a Supabase CLI no seu ambiente WSL (geralmente via npm ou gerenciador de pacotes do sistema operacional).
        2.  Com a CLI, você pode iniciar um ambiente Supabase local: `supabase init` (dentro da pasta do projeto) e `supabase start`. Isso rodará instâncias Docker do PostgreSQL, Supabase Auth, etc.
    * 🧐 **Teste Manual/Revisão Crítica:** Se instalado, verifique se `supabase start` funciona e se você consegue acessar os serviços locais do Supabase. (Para o MVP, podemos depender mais do Supabase na nuvem para desenvolvimento, mas o local é uma opção).

* **PREP.9. Configuração do WAHA Localmente (Se Viável):**
    * 🧑‍💻 **Task para Orquestrador:** "Pesquise se existe uma imagem Docker oficial ou comunitária estável do WAHA (ou da alternativa escolhida) que possa ser adicionada ao `docker-compose.yml` de desenvolvimento para testes locais da integração com WhatsApp. Configure as variáveis de ambiente necessárias para o WAHA local."
    * 🧐 **Teste Manual/Revisão Crítica:** Se configurado, tente iniciar o contêiner do WAHA localmente e veja se consegue conectar a uma instância de teste do WhatsApp.

---

### **Fase 3: Desenvolvimento do Backend (API Julião)**

* **Objetivo:** Construir o "cérebro" da aplicação.
* **Duração Estimada:** (A ser definida)
* **Status:** A Iniciar

* **3.1. Configuração Inicial do Projeto Backend e Ambiente Docker (Revisado):**
    * ⭐ **Task para Google Jules:** "Jules, para o projeto Julião (backend FastAPI em Python), assumindo que o Orquestrador já configurou Python e Poetry no ambiente de desenvolvimento WSL:
        1.  No repositório GitHub clonado, crie a estrutura de pastas inicial padrão para um projeto FastAPI.
        2.  Inicialize o projeto com Poetry: `poetry init` (interativamente ou com opções) e adicione as seguintes dependências principais via `poetry add`: `fastapi uvicorn[standard] pydantic psycopg2-binary asyncpg APScheduler python-jose[cryptography] supabase sqlalchemy alembic sqlmodel` (SQLModel é uma alternativa ao SQLAlchemy que integra bem com Pydantic e FastAPI, considere-o).
        3.  Crie um `Dockerfile` otimizado para produção para a aplicação FastAPI, usando Poetry para gerenciar dependências.
        4.  Crie um arquivo `docker-compose.yml` para desenvolvimento local. Este compose deve incluir:
            * Um serviço para a API FastAPI, montando o código local no contêiner para hot-reloading.
            * Um serviço para uma instância do PostgreSQL (ex: imagem `postgres:latest` ou `supabase/postgres` se disponível e adequada) para simular o banco de dados Supabase localmente. Configure volumes para persistência de dados do PostgreSQL local.
            * (Opcional, se o Orquestrador configurou WAHA localmente) Um serviço para o WAHA.
        5.  Crie um script `initial_setup.sh` para o ambiente da VM do Google Jules que instale Python (versão 3.9+), Poetry, e execute `poetry install` para instalar as dependências do projeto."
    * 🧐 **Teste Manual/Revisão Crítica:** Verificar a estrutura do projeto, `pyproject.toml`, Dockerfile, docker-compose.yml e script de setup. O Orquestrador deve conseguir rodar `docker compose up` no seu ambiente WSL e ver a API FastAPI e o PostgreSQL local subirem.

* **3.2. Modelagem e Criação das Tabelas no Supabase/PostgreSQL:** 🔒
    * **Contexto:** Usar a modelagem de banco de dados definida na Fase 1.
    * ⭐ **Task para Google Jules:** "Jules, para o projeto Julião:
        1.  Configure Alembic no projeto FastAPI.
        2.  Com base na modelagem de banco de dados definida (tabelas: `user_profiles`, `accounts`, `credit_cards`, `categories`, `transactions`, `installments`, `recurring_transactions`), gere os modelos SQLAlchemy (ou SQLModel) correspondentes.
        3.  Gere o primeiro script de migração do Alembic que cria todas essas tabelas no banco de dados, incluindo chaves, tipos de dados, constraints e timestamps."
    * 🧪 **Teste Unitário/Componente (Jules):** (Sugerir verificações no script de migração).
    * 🧐 **Teste Manual/Revisão Crítica:** Validar modelos e script de migração. Aplicar a migração no PostgreSQL local (via `docker compose run --rm backend alembic upgrade head`) e também no ambiente de desenvolvimento Supabase na nuvem.

* **(As demais tarefas da Fase 3 e subsequentes permanecem como no roadmap anterior, mas agora com o entendimento de que o Orquestrador tem um ambiente local configurado para testar e rodar o que o Google Jules produzir, e para executar as tarefas manuais de configuração do servidor VPS na Fase 7).**

---

### **Fase 4: Desenvolvimento do Frontend (Dashboard Web - React.js)**
    (...conforme roadmap anterior...)

---

### **Fase 5: Configuração e Integração do Gateway WhatsApp (WAHA)**
    (...conforme roadmap anterior, mas o Orquestrador pode tentar configurar o WAHA localmente primeiro, se viável, antes de configurar no VPS...)

---

### **Fase 6: Testes Integrados e de Sistema**
    (...conforme roadmap anterior...)

---

### **Fase 7: Implantação do MVP e Configuração do Servidor**

* **Objetivo:** Colocar o MVP do Julião no ar para seu uso e configurar o servidor VPS.
* **Duração Estimada:** (A ser definida)
* **Status:** A Iniciar

* **7.1. Configuração do Servidor VPS Oracle (Detalhado):** 🔒
    * **7.1.1. Acesso Inicial e Atualizações de Segurança Básicas:**
        * 🧑‍💻 **Task para Orquestrador (com instruções do Arquiteto):** "Acesse seu VPS Oracle (Ubuntu Linux) via SSH usando as credenciais fornecidas pela Oracle."
        * 🧑‍💻 **Task para Orquestrador:** "Execute os seguintes comandos para atualizar o sistema: `sudo apt update && sudo apt upgrade -y`."
        * 🧑‍💻 **Task para Orquestrador:** "Crie um novo usuário não-root com privilégios sudo (ex: `sudo adduser nome_do_seu_usuario`, `sudo usermod -aG sudo nome_do_seu_usuario`). Configure o acesso SSH para este novo usuário (copiando sua chave pública SSH para `~/.ssh/authorized_keys` do novo usuário). Teste o login com o novo usuário."
        * 🧑‍💻 **Task para Orquestrador:** "Desabilite o login root via SSH e o login por senha, permitindo apenas login por chave SSH. Edite o arquivo `/etc/ssh/sshd_config` (ex: `PermitRootLogin no`, `PasswordAuthentication no`) e reinicie o serviço SSH (`sudo systemctl restart sshd`)."
        * 🧑‍💻 **Task para Orquestrador:** "Configure o firewall UFW (Uncomplicated Firewall):
            * `sudo ufw allow OpenSSH`
            * `sudo ufw allow http` (porta 80)
            * `sudo ufw allow https` (porta 443)
            * (Adicione outras portas se necessário para WAHA ou outras ferramentas, mas seja restritivo)
            * `sudo ufw enable`
            * `sudo ufw status verbose` para verificar."
        * 🧐 **Teste Manual/Revisão Crítica:** "Confirme que você consegue acessar o VPS com o novo usuário via SSH e que o firewall está ativo com as regras corretas. Verifique se o login root via SSH está desabilitado."

    * **7.1.2. Instalação do Docker e Docker Compose:**
        * ⭐ **Task para Google Jules:** "Jules, forneça um script shell (`.sh`) ou uma sequência de comandos para instalar a versão mais recente do Docker Engine e do Docker Compose V2 no Ubuntu Linux (versão LTS mais recente suportada pelo VPS Oracle). O script deve incluir a adição do repositório oficial do Docker, instalação do Docker Engine, e instalação do plugin Docker Compose. Inclua comandos para adicionar o usuário atual ao grupo `docker` para evitar usar `sudo` com comandos docker."
        * 🧑‍💻 **Task para Orquestrador:** "Execute o script/comandos fornecidos por Jules no seu VPS para instalar o Docker e o Docker Compose. Após a instalação, reinicie a sessão SSH ou execute `newgrp docker` para aplicar as permissões de grupo."
        * 🧐 **Teste Manual/Revisão Crítica:** "Execute `docker --version` e `docker compose version` para verificar se ambos estão instalados corretamente e funcionando. Tente rodar um contêiner de teste simples (ex: `docker run hello-world`)."

    * **7.1.3. Configuração do Reverse Proxy (Nginx ou Caddy):** 🔒
        * ⭐ **Task para Google Jules:** "Jules, forneça a configuração para Nginx como reverse proxy no VPS Ubuntu. Ele deve:
            1.  Ser instalado via `apt`.
            2.  Ouvir nas portas 80 e 443.
            3.  Redirecionar todo o tráfego HTTP (porta 80) para HTTPS (porta 443) para todos os domínios configurados.
            4.  Utilizar Certbot com o plugin Nginx para obter e renovar automaticamente certificados SSL/TLS da Let's Encrypt para o(s) domínio(s) do projeto Julião (ex: `app.juliao.com.br`, `api.juliao.com.br`).
            5.  Configurar blocos de servidor (`server blocks`) para:
                * Um subdomínio (ex: `app.juliao.com.br`) para servir a aplicação frontend React (que estará rodando em um contêiner Docker, por exemplo, na porta 3000 do host).
                * Outro subdomínio ou path (ex: `api.juliao.com.br` ou `app.juliao.com.br/api/v1`) para redirecionar requisições para a API backend FastAPI (que estará rodando em outro contêiner Docker, por exemplo, na porta 8000 do host).
                * (Opcional) Um subdomínio ou path para o WAHA, se ele precisar ser acessado externamente e for servido via Docker.
            6.  Incluir headers de segurança recomendados (HSTS, X-Frame-Options, X-Content-Type-Options, CSP básico se possível)."
        * 🧑‍💻 **Task para Orquestrador:** "Siga as instruções e use os arquivos de configuração do Nginx fornecidos por Jules. Instale Nginx e Certbot. Configure os domínios (você precisará ter os registros DNS apontando para o IP do seu VPS). Execute o Certbot para obter os certificados."
        * 🧐 **Teste Manual/Revisão Crítica:** "Após o deploy dos contêineres do frontend e backend (em uma etapa posterior), teste o acesso via HTTPS, o redirecionamento HTTP->HTTPS, a validade dos certificados SSL e o correto roteamento das requisições para o frontend e para a API backend. Verifique os headers de segurança."

    * **7.1.4. Configuração de Variáveis de Ambiente de Produção e Gerenciamento de Segredos:** 🔒
        * 🧑‍💻 **Task para Orquestrador (com orientação do Arquiteto):** "Defina as variáveis de ambiente de produção de forma segura no VPS para serem usadas pelos contêineres Docker. Crie um arquivo `.env.production` na pasta raiz do seu projeto no VPS (fora do versionamento do Git) para cada serviço (backend, frontend se necessário, WAHA). Este arquivo será usado pelo `docker-compose.production.yml`. As variáveis incluem:
            * Para o Backend (FastAPI): `DATABASE_URL` (string de conexão do Supabase), `SUPABASE_URL`, `SUPABASE_ANON_KEY`, `SUPABASE_SERVICE_ROLE_KEY` (se necessário para operações admin no backend), `GEMINI_API_KEY`, `JWT_SECRET_KEY` (se o Supabase não gerenciar tudo ou para outros usos), `WAHA_API_ENDPOINT`, `WAHA_API_KEY` (se o WAHA usar), `ENVIRONMENT=production`, `API_BASE_URL=https://api.seudominio.com.br`.
            * Para o Frontend (React): `REACT_APP_API_BASE_URL=https://api.seudominio.com.br`, `REACT_APP_SUPABASE_URL`, `REACT_APP_SUPABASE_ANON_KEY`.
            * Garanta que o arquivo `.env.production` tenha permissões restritas (ex: `chmod 600 .env.production`)."
        * ⭐ **Task para Google Jules:** "Jules, modifique o `docker-compose.yml` (ou crie um `docker-compose.production.yml`) para que os serviços (backend, frontend) leiam as variáveis de ambiente de um arquivo `.env.production` especificado."
        * 🧐 **Teste Manual/Revisão Crítica:** "Verifique se os contêineres conseguem ler as variáveis de ambiente corretamente quando iniciados com o compose de produção."

    * **7.1.5. (Opcional) Configuração de Monitoramento Básico e Logs:**
        * ⭐ **Task para Google Jules:** "Jules, sugira ferramentas ou métodos simples para monitoramento básico do servidor VPS (uso de CPU, memória, disco - ex: `htop`, `vmstat`, `df`) e para a configuração de rotação e gerenciamento de logs dos contêineres Docker (ex: usando o driver de log do Docker para `json-file` com opções de `max-size` e `max-file`, ou configurando `logrotate` para os arquivos de log do Docker se necessário)."
        * 🧑‍💻 **Task para Orquestrador:** "Implemente as sugestões de monitoramento e gerenciamento de logs."
        * 🧐 **Teste Manual/Revisão Crítica:** "Verifique se os logs dos contêineres estão sendo capturados e rotacionados corretamente e se você consegue acessar as ferramentas básicas de monitoramento do servidor."

* **7.2. Scripts de Deploy e Implantação:**
    * ⭐ **Task para Google Jules:** "Jules, crie um script de deploy (`deploy.sh`) que automatize o processo no VPS de produção:
        1.  Navegar para o diretório do projeto.
        2.  Fazer `git pull` da branch principal (ou da branch de release).
        3.  (Se necessário) Parar os serviços do `docker-compose.production.yml`.
        4.  Construir as imagens Docker para o backend e frontend (se não estiverem sendo puxadas de um registro Docker Hub/GHCR): `docker compose -f docker-compose.production.yml build --no-cache`.
        5.  (Se aplicável) Executar migrações do banco de dados usando Alembic dentro do contêiner do backend: `docker compose -f docker-compose.production.yml run --rm backend alembic upgrade head`.
        6.  Iniciar os novos contêineres em modo detached: `docker compose -f docker-compose.production.yml up -d --remove-orphans`.
        7.  (Opcional) Executar um `docker image prune -af` para limpar imagens antigas não utilizadas."
    * 🧐 **Teste Manual/Revisão Crítica:** Testar o script de deploy em um ambiente de staging (se possível, mesmo que seja uma simulação no VPS antes de apontar o DNS real) ou diretamente no VPS de produção com cautela e rollback planejado.

* **7.3. Implantação Final e Testes Pós-Implantação:**
    * 🧑‍💻 **Task para Orquestrador:** Executar o deploy final usando o script.
    * 🧐 **Teste Manual/Revisão Crítica:** Realizar um smoke test completo no ambiente de produção (acessando pelos domínios configurados) para garantir que todas as funcionalidades principais estão operando como esperado. Verificar logs por erros.

---

### **Fase 8: Coleta de Feedback, Iteração e Melhorias Contínuas (Pós-MVP)**

* **Objetivo:** Aprender com o uso inicial e planejar os próximos passos.
* **Status:** Contínuo após o lançamento do MVP

* **Atividades Contínuas:**
    * Coleta de feedback do Orquestrador (primeiro usuário).
    * Monitoramento da aplicação.
    * Priorização de correções e melhorias.
    * Planejamento de novas funcionalidades.

---

## Project Roadmap: Julião (High-Level Overview)

This document outlines the development progress and future plans for the Julião personal finance application.

## Phase 1: Foundation and Core Setup

### Completed
-   [X] **Initial Backend Project Setup (FastAPI, Docker, Poetry)**
    -   Established project structure for `juliao_api`.
    -   Integrated FastAPI with a basic health check endpoint.
    -   Set up Poetry for dependency management.
    -   Configured Docker (`Dockerfile`, `docker-compose.yml`) for development and production environments.
    -   Created `.env.example` for environment configuration.

### Upcoming
-   [ ] **User Authentication & Authorization**
    -   Implement JWT-based authentication (potentially leveraging Supabase).
    -   Define user registration and login endpoints.
    -   Set up password hashing and recovery mechanisms.
-   [ ] **Core Data Models Definition**
    -   Define Pydantic models and SQLAlchemy/SQLModel schemas for:
        -   Users
        -   Accounts (e.g., checking, savings, credit cards)
        -   Transactions (income, expenses, transfers)
        -   Categories
        -   Budgets
-   [ ] **Database Setup and Migrations**
    -   Finalize database schema.
    -   Configure and initialize Alembic for database migrations.
    -   Create initial migration scripts.
-   [ ] **Basic CRUD Operations for Core Models**
    -   Develop API endpoints for creating, reading, updating, and deleting core data entities (e.g., accounts, transactions).
-   [ ] **Supabase Integration (Initial)**
    -   Connect to Supabase for database and potentially authentication.
    -   Explore Supabase for storage if needed.

## Phase 2: Feature Development

### Planned
-   [ ] Transaction Management Enhancements
-   [ ] Budgeting Features
-   [ ] Financial Goals Setting
-   [ ] Reporting and Analytics
-   [ ] Credit Card Management
-   [ ] Investment Tracking (Basic)
-   [ ] Notifications System

## Phase 3: Refinements and Advanced Features

### Planned
-   [ ] AI-powered Financial Insights (Gemini API integration)
-   [ ] Advanced Reporting and Data Visualization
-   [ ] Debt Management Tools
-   [ ] Multi-currency Support
-   [ ] Third-party Account Aggregation (if feasible)

## Technology Stack (Backend - Julião API)

-   **Framework:** FastAPI
-   **Language:** Python 3.9+
-   **Database:** PostgreSQL
-   **Containerization:** Docker
-   **Dependency Management:** Poetry
-   **Migrations:** Alembic
-   **Authentication:** JWT (potentially via Supabase Auth)
-   **Cloud Services (Potential):** Supabase (Database, Auth, Storage), Gemini API

---

*This roadmap is a living document and will be updated as the project progresses.*
