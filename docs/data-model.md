# Data & State Model

## Core datasets

- **Publishing Queue:** scheduling and publishing lifecycle.
- **Asset Repository:** content lifecycle and editorial state.
- **Planner events:** scheduling history and consumed-slot evidence.

Production table identifiers and row data are intentionally omitted.

## State ownership

The publisher owns publishing states and external evidence. WF05E owns schedule fields only for explicitly plannable states: `PENDENTE`, `AGENDADO`, `EM_FILA` and `ERRO_TEMPORARIO`. Other states fail closed. WF06 projects publication state to the repository; WF07 reconciles independent relations.

Representative states include `PENDENTE`, `PROCESSANDO`, `CRIANDO`, `PUBLISHING_EXTERNAL`, `PUBLICADO`, `PUBLICADO_SEM_COMENTARIO`, `EXTERNAL_OUTCOME_UNKNOWN`, `ERRO_DEFINITIVO`, `CANCELADO` and `SEM_VAGA_15D`.

## Publication identity

The local row identifier and external Meta creation identifier have different meanings. V1 stores the latter explicitly as `meta_creation_id` before `media_publish`; it is never inferred from a generic `id`. For carousels, all required child containers must exist before the parent is publishable.

## Release invariants

Validation covers canonical identity, unique active slots, consumed-slot protection, queue/repository coherence, publication immutability, external identifier preservation and terminality. These are consistency controls, not a claim of exactly-once delivery.
