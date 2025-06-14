---
id: TASK-010
title: "Implementar Lógica para Transações Parceladas (Parcela)"
epic: "Backend"
status: backlog
priority: medium
dependencies: ["TASK-008", "TASK-009"] # Extends Transacao, relates to CartaoDeCredito for installments
assignee: Jules
---

### Descrição

Implementar a lógica para transações parceladas, conforme Seção 2.5 da `docs/ESPECIFICACAO_BACKEND_MVP.md`.
Modificar `POST /api/v1/transacoes` para lidar com compras parceladas (gerar múltiplas instâncias de `Parcela`).
Definir como as `Parcela`s são vinculadas à `Transacao` original e ao `CartaoDeCredito` (se aplicável).
Atualizar status das parcelas ao pagar faturas de cartão.

### Critérios de Aceitação

- [ ] `POST /api/v1/transacoes` pode criar transações parceladas, gerando os devidos registros de `Parcela`.
- [ ] Parcelas são corretamente associadas à transação mãe e ao cartão (se for compra no crédito).
- [ ] Status de parcelas são atualizados (ex: ao pagar fatura de cartão).
- [ ] Testes cobrem a criação e gestão de transações parceladas.

### Arquivos Relevantes

* `docs/ESPECIFICACAO_BACKEND_MVP.md` (Seção 2.5)
* `juliao_api/app/models/finance_models.py` (para `Parcela`, `Transacao`)
* `juliao_api/app/services/transacao_service.py` (modificado)
* `juliao_api/app/services/cartao_service.py` (modificado)

### Relatório de Execução

(Esta seção deve ser deixada em branco)
