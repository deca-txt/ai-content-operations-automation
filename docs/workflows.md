# Workflow Architecture

The production V1 contains eleven active workflows.

Public documentation uses functional names only. Production IDs and real webhook paths are intentionally omitted.

## 1. Media Maintenance
Scheduled cleanup of media infrastructure.

## 2. Multi-format Publisher
Central publishing engine.

Responsibilities:
- select eligible item;
- process publishing;
- handle temporary failure paths;
- register publication evidence;
- request synchronization.

## 3. Editorial View
Human-facing editorial/campaign view.

## 4. History & Observability
Operational history and visibility.

## 5. Content Intake
Fast form-based entry into the repository.

## 6. Repository Operations
Repository review and operational actions.

## 7. Automatic AI Analysis
AI-assisted content analysis.

Triggers may include:
- event-driven request;
- fallback schedule;
- manual execution for controlled testing.

## 8. Editorial Decision
Converts human decision into planner eligibility.

## 9. FIFO Planner
Automatic planning engine.

Responsibilities:
- determine available slots;
- preserve existing assignments;
- schedule approved content;
- avoid slot duplication;
- avoid consumed-slot reuse.

## 10. Publication → Repository Synchronization
Shared consistency component.

Used by:
- normal publication;
- recovery path;
- watchdog.

## 11. Consistency Watchdog
Detects operational divergence and requests reconciliation.

---

## Functional grouping

```text
INTAKE & EDITORIAL
Content Intake
→ AI Analysis
→ Repository Operations
→ Editorial Decision

PLANNING
FIFO Planner

PUBLISHING
Multi-format Publisher

RELIABILITY & OBSERVABILITY
Synchronization
Watchdog
Editorial View
History
Media Maintenance
```
