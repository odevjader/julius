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
