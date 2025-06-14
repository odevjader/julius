# Especificação Detalhada do Backend - MVP Julião

Este documento detalha as funcionalidades de backend para o MVP do projeto Julião, conforme delineado no `ROADMAP.md`. O objetivo é fornecer uma base clara para o desenvolvimento e criação de tarefas de implementação.

## 1. Autenticação e Autorização de Usuário

Baseado na "Fase 2" do Roadmap.

### 1.1. Provedor e Mecanismo
*   **Provedor Principal:** Supabase Auth será o provedor primário para gerenciamento de identidades.
*   **Mecanismo:** Autenticação baseada em JSON Web Tokens (JWT). Os tokens emitidos pelo Supabase Auth serão validados pela API Julião.
*   **Fluxo de Token:**
    1.  Cliente (frontend/app móvel) autentica-se com Supabase Auth (email/senha, ou OAuth com Google/outros se configurado no Supabase).
    2.  Supabase Auth retorna um JWT (access token e refresh token).
    3.  Cliente envia o JWT (access token) no header `Authorization` (Bearer token) para endpoints protegidos da API Julião.
    4.  API Julião valida o JWT usando a chave pública do Supabase.

### 1.2. Endpoints da API (Gerenciados pelo Supabase, mas a API pode precisar interagir com dados do usuário)
*   Não haverá endpoints diretos na API Julião para registro e login, pois o Supabase GoTrue (serviço de autenticação do Supabase) os gerenciará.
*   A API Julião precisará de um endpoint para sincronizar/criar o perfil do usuário local (`PerfilDeUsuario`) após o primeiro login via Supabase, se necessário.
    *   **`POST /api/v1/users/sync_profile`**: Chamado pelo frontend após um login bem-sucedido no Supabase, se um perfil local ainda não existir. A API valida o token Supabase e cria/atualiza o `PerfilDeUsuario` com base no ID de usuário do Supabase.

### 1.3. Políticas de Senha e Segurança
*   Gerenciadas pelo Supabase Auth (complexidade, expiração, etc.). A API Julião confia na segurança do Supabase para estes aspectos.
*   Hashing de senha é tratado pelo Supabase.

### 1.4. Perfis de Usuário e Dados Adicionais
*   O modelo `PerfilDeUsuario` em `juliao_api/app/models/user_models.py` armazenará informações adicionais do usuário não cobertas pelo Supabase Auth (ex: configurações específicas da aplicação, preferências).
*   O `id` do `PerfilDeUsuario` deve ser o mesmo UUID do usuário no Supabase para fácil correlação.

## 2. Operações CRUD Básicas para Modelos Principais

Baseado na "Fase 2" do Roadmap. Todos os endpoints devem ser protegidos e operar no contexto do usuário autenticado (exceto admin, se houver).

### 2.1. Contas (`Conta`)
*   **`POST /api/v1/contas`**: Criar nova conta para o usuário.
    *   Request: `{ "nome": "string", "tipo_conta": "string (ex: carteira, corrente, poupanca)", "saldo_inicial": "float", "moeda": "string (default BRL)" }`
    *   Response: Detalhes da conta criada.
*   **`GET /api/v1/contas`**: Listar todas as contas do usuário.
    *   Response: Array de contas.
*   **`GET /api/v1/contas/{id_conta}`**: Obter detalhes de uma conta específica.
    *   Response: Detalhes da conta.
*   **`PUT /api/v1/contas/{id_conta}`**: Atualizar uma conta.
    *   Request: `{ "nome": "string", "tipo_conta": "string" }` (saldo não é atualizado diretamente aqui, mas por transações).
    *   Response: Detalhes da conta atualizada.
*   **`DELETE /api/v1/contas/{id_conta}`**: Deletar uma conta (considerar soft delete e impacto em transações existentes).

### 2.2. Categorias (`Categoria`)
*   **`POST /api/v1/categorias`**: Criar nova categoria para o usuário.
    *   Request: `{ "nome": "string", "tipo": "string (receita ou despesa)", "cor_hex": "string (opcional)" }`
    *   Response: Detalhes da categoria criada.
*   **`GET /api/v1/categorias`**: Listar todas as categorias do usuário (e talvez categorias padrão do sistema).
    *   Response: Array de categorias.
*   **`GET /api/v1/categorias/{id_categoria}`**: Obter detalhes de uma categoria.
*   **`PUT /api/v1/categorias/{id_categoria}`**: Atualizar uma categoria.
*   **`DELETE /api/v1/categorias/{id_categoria}`**: Deletar uma categoria (considerar impacto em transações existentes).

### 2.3. Transações (`Transacao`)
*   **`POST /api/v1/transacoes`**: Registrar nova transação.
    *   Request: `{ "descricao": "string", "valor": "float", "data_transacao": "date", "id_conta": "integer", "id_categoria": "integer", "tipo": "string (receita ou despesa)", "observacoes": "string (opcional)" }`
    *   Response: Detalhes da transação.
    *   Lógica: Atualizar saldo da `Conta` associada.
*   **`GET /api/v1/transacoes`**: Listar transações do usuário (com filtros: por conta, período, tipo, categoria).
*   **`GET /api/v1/transacoes/{id_transacao}`**: Obter detalhes de uma transação.
*   **`PUT /api/v1/transacoes/{id_transacao}`**: Atualizar uma transação.
    *   Lógica: Reverter impacto no saldo antigo, aplicar novo impacto.
*   **`DELETE /api/v1/transacoes/{id_transacao}`**: Deletar uma transação.
    *   Lógica: Reverter impacto no saldo.

### 2.4. Cartões de Crédito (`CartaoDeCredito`)
*   **`POST /api/v1/cartoes`**: Adicionar novo cartão de crédito.
    *   Request: `{ "nome": "string", "limite": "float", "dia_fechamento": "integer", "dia_vencimento": "integer", "id_conta_padrao_pagamento": "integer (opcional)"}`
*   **`GET /api/v1/cartoes`**: Listar cartões do usuário.
*   **`GET /api/v1/cartoes/{id_cartao}`**: Detalhes do cartão.
*   **`PUT /api/v1/cartoes/{id_cartao}`**: Atualizar cartão.
*   **`DELETE /api/v1/cartoes/{id_cartao}`**: Deletar cartão.
*   **Faturas (`FaturaCartao`)**: Este modelo não foi explicitamente listado nos modelos SQLModel, mas é essencial. Pode ser gerado dinamicamente ou necessitar de um modelo.
    *   **`GET /api/v1/cartoes/{id_cartao}/faturas`**: Listar faturas (abertas, fechadas, pagas).
    *   **`GET /api/v1/cartoes/{id_cartao}/faturas/{mes_ano}`**: Detalhes de uma fatura específica.
    *   Transações do tipo "despesa" podem ser associadas a um `CartaoDeCredito` e a uma fatura.

### 2.5. Transações Parceladas (`Parcela` e `Transacao`)
*   Quando uma `Transacao` é uma compra parcelada, múltiplas instâncias de `Parcela` são criadas.
*   A `Transacao` original pode representar o valor total, e as `Parcela`s os pagamentos individuais mensais.
*   Detalhar como o `POST /api/v1/transacoes` lidaria com `eh_parcelada: true, numero_parcelas: X`.

### 2.6. Transações Recorrentes (`TransacaoRecorrente`)
*   **`POST /api/v1/transacoes_recorrentes`**: Criar transação recorrente.
    *   Request: `{ "descricao": "string", "valor": "float", "data_inicio": "date", "frequencia": "string (mensal, semanal, etc.)", "dia_recorrencia": "integer (opcional)", "id_conta": "integer", "id_categoria": "integer", "tipo": "string" }`
*   **`GET /api/v1/transacoes_recorrentes`**: Listar.
*   **Lógica de Negócio:** Um job agendado (APScheduler) verificará transações recorrentes e criará `Transacao` concretas quando devido.

## 3. Integração Inicial com Supabase

Baseado na "Fase 2" do Roadmap.

*   **Conexão com Banco de Dados:** Configurada via variáveis de ambiente (`DATABASE_URL`).
*   **Autenticação:** Conforme descrito na seção 1.
*   **Armazenamento de Arquivos (Supabase Storage):**
    *   **Casos de Uso:** Comprovantes de transação, fotos de perfil (opcional).
    *   **Buckets Sugeridos:** `comprovantes_transacoes`, `avatares_usuarios`.
    *   **Controle de Acesso:**
        *   `comprovantes_transacoes`: Acesso restrito ao proprietário da transação. Upload via API Julião que intermedia com Supabase Storage usando service role key. Download similarmente.
        *   `avatares_usuarios`: Acesso público para leitura, upload restrito ao usuário proprietário (via API Julião).
    *   **API Julião Endpoints (Exemplo para comprovantes):**
        *   **`POST /api/v1/transacoes/{id_transacao}/upload_comprovante`**: Faz upload do arquivo para Supabase Storage e associa URL/path à transação.
        *   **`GET /api/v1/transacoes/{id_transacao}/comprovante`**: Retorna URL para acesso ao comprovante ou faz stream.

## 4. Detalhamento Preliminar de Funcionalidades da Fase 4 do Roadmap

### 4.1. Interação via WhatsApp (Integração com Gateway WAHA)
*   **Endpoint de Recepção na API Julião:**
    *   **`POST /api/v1/whatsapp/webhook`**: Recebe mensagens do WAHA.
        *   Request: Estrutura de dados do WAHA (mensagem, número do remetente, etc.).
        *   Lógica: Identificar usuário pelo número de telefone. Processar comando (NLP básico ou palavras-chave):
            *   Registrar despesa: "Gastei 50 em almoço"
            *   Registrar receita: "Recebi 1000 salário"
            *   Consultar saldo: "Qual meu saldo?"
        *   Response: Mensagem de confirmação ou informação para ser enviada de volta ao WAHA.
*   **Processamento de Linguagem Natural (NLP):** Considerar uma biblioteca Python simples para extrair intenção e entidades (valor, descrição, categoria implícita).

### 4.2. Melhorias na Gestão de Transações
*   **Transações Parceladas:**
    *   Ao criar uma transação parcelada, o sistema deve gerar as N `Parcela`s futuras, cada uma com sua data de vencimento e status inicial (pendente).
    *   O pagamento de uma fatura de cartão de crédito que contém parcelas deve atualizar o status dessas parcelas.
*   **Lembretes e Notificações:**
    *   Job agendado para verificar:
        *   Contas a pagar/receber (baseado em `TransacaoRecorrente` ou `Transacao` com data futura).
        *   Vencimento de faturas de cartão.
    *   Mecanismo de notificação (inicialmente pode ser log/email para o admin, futuramente via app/WhatsApp).

### 4.3. Recursos de Orçamentação
*   **Modelo `Orcamento`:**
    *   `id_usuario`, `id_categoria`, `valor_mensal`, `mes_ano_referencia`.
*   **Lógica:** Ao registrar uma transação de despesa, verificar se existe um orçamento para a categoria no mês e atualizar o gasto realizado nesse orçamento.
*   **Endpoints:**
    *   `POST /api/v1/orcamentos`
    *   `GET /api/v1/orcamentos?mes_ano=YYYY-MM`
    *   `PUT /api/v1/orcamentos/{id_orcamento}`

### 4.4. Metas Financeiras
*   **Modelo `MetaFinanceira`:**
    *   `id_usuario`, `nome`, `valor_alvo`, `data_alvo`, `valor_atual` (calculado ou atualizado por transações específicas). `id_conta_associada` (opcional, para metas de poupança em uma conta).
*   **Lógica:** Usuário pode criar metas. Transações de "depósito na meta" podem atualizar o `valor_atual`.
*   **Endpoints:** CRUD básico para `MetaFinanceira`.

Este documento serve como um ponto de partida para o detalhamento. Cada seção pode ser expandida conforme necessário durante o ciclo de desenvolvimento.
```
