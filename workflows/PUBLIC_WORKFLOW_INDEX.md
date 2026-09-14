# Public Workflow Blueprints

These eleven files are structure-only, sanitized representations of the frozen V1 workflows. They intentionally exclude parameters, credentials, URLs, webhook paths, production IDs, node names and business data.

| Workflow | Nodes | Connections | Trigger types | File |
|---|---:|---:|---|---|
| Media Maintenance | 7 | 6 | schedule | `01-media-maintenance.public-structure.json` |
| Multi-format Publisher | 60 | 77 | schedule | `02-multiformat-publisher.public-structure.json` |
| Editorial View | 6 | 5 | webhook | `03-editorial-view.public-structure.json` |
| History & Observability | 7 | 5 | webhook | `04-history-observability.public-structure.json` |
| Content Intake | 7 | 6 | form | `05-content-intake.public-structure.json` |
| Repository Operations | 6 | 5 | webhook | `06-repository-operations.public-structure.json` |
| Automatic AI Analysis | 17 | 16 | manual, schedule, webhook | `07-ai-analysis.public-structure.json` |
| Editorial Decision | 9 | 8 | webhook | `08-editorial-decision.public-structure.json` |
| FIFO Planner | 31 | 34 | manual, schedule | `09-fifo-planner.public-structure.json` |
| Publication State Synchronization | 8 | 8 | execute workflow | `10-state-synchronization.public-structure.json` |
| Consistency Watchdog | 6 | 5 | schedule | `11-consistency-watchdog.public-structure.json` |

The critical blueprints make final behavior explicit in their companion case documentation: WF02 covers exclusive ownership, semantic creation-ID preservation, readiness, outcome protection and terminality; WF05E covers its fail-closed plannable-state allowlist; WF07 covers per-item failure isolation.
