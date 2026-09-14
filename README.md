# AI-Assisted Content Operations & Publishing Automation

A sanitized product case about building a production-validated content operations system: AI-assisted analysis, human approval, FIFO planning, external publishing, state synchronization, observability and recovery.

> **Status:** V1 complete · production validated · operational release
> **Role:** Product Builder · Automation Designer · Product/System Designer
> **Development:** ~5 weeks of part-time iterative work

## What I built

```text
Content Intake → Asset Repository → AI Analysis → Human Approval
→ FIFO Planner → Publishing Queue → Exclusive Claim / Ownership
→ Media Container Creation → Readiness / Polling
→ Protected External Publish Boundary → Instagram Graph API
→ State Synchronization → Watchdog / Observability / Recovery
```

AI accelerates analysis, while a human retains editorial approval. Persistent operational state connects specialized workflows and makes recovery explicit.

## Reliability decisions that shaped V1

- **M2 — Exclusive claim:** a publisher claims an item and rechecks ownership before the external boundary.
- **M3 — External outcome handling:** confirmed success is synchronized; deterministic rejection is recorded without blind republish; ambiguity is protected from automatic retry and requires human reconciliation.
- **M4 — State terminality:** late branches cannot downgrade published, protected, or externally ambiguous states.
- **WF05E ownership:** the planner uses a fail-closed allowlist and mutates only explicitly plannable states.
- **WF07 isolation:** reconciliation isolates malformed relations per item so unrelated valid items continue.

The design does not claim exactly-once delivery. Local state and an irreversible external API are not one atomic transaction. V1 provides exclusive local ownership, duplicate-risk reduction, protected states, no unsafe automatic republish after ambiguity, and human exception handling: best-effort consistency across both systems.

## Production canary

The final release included a clean real production canary. Public evidence is intentionally aggregate:

```text
PLANNING=PASS · EXCLUSIVE_CLAIM=PASS · CREATION_ID_PRESERVATION=PASS
MEDIA_PUBLISH_COUNT=1 · DUPLICATE_PUBLICATION=NO · STATE_FLOW=PASS
TERMINALITY=PASS · QUEUE_FINAL_STATE=PUBLISHED · REPOSITORY_FINAL_STATE=PUBLISHED
SYNCHRONIZATION=PASS · POST-PUBLISH_PLANNER_IMMUTABILITY=PASS
GLOBAL_INCONSISTENCIES=0
```

No post, container, account, webhook, or execution identifiers are published.

## Case study

- [Full Product Case](docs/index.md)
- [System Architecture](docs/architecture.md)
- [Workflow Architecture](docs/workflows.md)
- [Data & State Model](docs/data-model.md)
- [Reliability & Release](docs/reliability.md)
- [Timeline](docs/timeline.md)
- [Future Product Roadmap](docs/future-roadmap.md)
- [Learning Roadmap](docs/learning-roadmap.md)

## Repository scope

This is a sanitized public case study, not a deployable production export. It contains no credentials, tokens, private identifiers, databases, raw execution payloads, private URLs, customer content, or production workflow exports. See [SANITIZATION.md](SANITIZATION.md).

## Portuguese summary

Este repositório documenta um sistema de operações de conteúdo assistido por IA, com aprovação humana, planejamento FIFO, publicação, sincronização e recuperação. A V1 foi validada em produção e concluída como release operacional, sem expor dados ou infraestrutura privada.
