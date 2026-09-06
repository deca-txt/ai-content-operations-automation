# Public Workflow Blueprints

These files are **structure-only derivatives** of the frozen production workflows.

They intentionally exclude parameters, credentials, URLs, webhook paths, production IDs, node names and business data.

| Workflow | Nodes | Connections | Trigger types | File |
|---|---:|---:|---|---|
| Media Maintenance | 7 | 6 | n8n-nodes-base.scheduleTrigger | `01-media-maintenance.public-structure.json` |
| Multi-format Publisher | 44 | 61 | n8n-nodes-base.scheduleTrigger | `02-multiformat-publisher.public-structure.json` |
| Editorial View | 6 | 5 | n8n-nodes-base.respondToWebhook, n8n-nodes-base.webhook | `03-editorial-view.public-structure.json` |
| History & Observability | 7 | 5 | n8n-nodes-base.respondToWebhook, n8n-nodes-base.webhook | `04-history-observability.public-structure.json` |
| Content Intake | 7 | 6 | n8n-nodes-base.formTrigger | `05-content-intake.public-structure.json` |
| Repository Operations | 6 | 5 | n8n-nodes-base.respondToWebhook, n8n-nodes-base.webhook | `06-repository-operations.public-structure.json` |
| Automatic AI Analysis | 17 | 16 | n8n-nodes-base.manualTrigger, n8n-nodes-base.scheduleTrigger, n8n-nodes-base.webhook | `07-ai-analysis.public-structure.json` |
| Editorial Decision | 9 | 8 | n8n-nodes-base.respondToWebhook, n8n-nodes-base.webhook | `08-editorial-decision.public-structure.json` |
| FIFO Planner | 31 | 34 | n8n-nodes-base.manualTrigger, n8n-nodes-base.scheduleTrigger | `09-fifo-planner.public-structure.json` |
| Publication State Synchronization | 8 | 8 | n8n-nodes-base.executeWorkflowTrigger | `10-state-synchronization.public-structure.json` |
| Consistency Watchdog | 6 | 5 | n8n-nodes-base.scheduleTrigger | `11-consistency-watchdog.public-structure.json` |

## Why structure-only?

The public repository is intended to prove system architecture and workflow complexity without publishing operational implementation details or secrets.
