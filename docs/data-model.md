# Data & State Model

## Core datasets

The system uses two main operational datasets:

### Publishing Queue
Represents scheduling and publishing lifecycle.

### Asset Repository
Represents content lifecycle and editorial state.

Production table identifiers are intentionally omitted.

---

## Queue states

Core states include:

- `PENDING`
- `PROCESSING`
- `TEMPORARY_ERROR`
- `PUBLISHED`

Names are normalized here for public documentation.

---

## Repository states

Relevant operational states include:

- queued;
- published;

AI analysis and editorial approval are represented through additional fields.

---

## Canonical relationship

Queue records generated from repository items embed a canonical content identity.

The public representation is:

```text
queue_reference -> canonical_content_id
repository_item -> canonical_content_id
```

The production encoding is intentionally omitted.

---

## Release invariants

The release audit verifies that:

- every active queue item has a valid canonical content identity;
- active content identities are unique;
- active queue identifiers are unique;
- active planning slots are unique;
- consumed publishing slots are not reused;
- active queue content exactly matches repository items marked as queued;
- repository queued identities are unique;
- repository-originated publications match published repository items;
- published identities are unique;
- previous published history is not modified.

---

## Legacy history

The final release contained a stable set of legacy published queue rows that predated the repository model.

They were explicitly separated from current repository-originated publishing so historical data would not be misclassified as a synchronization defect.
