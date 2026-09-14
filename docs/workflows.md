# Workflow Architecture

V1 contains eleven active workflows. The public JSON files are sanitized structural representations, never production exports.

1. **Media Maintenance** — scheduled media housekeeping.
2. **Multi-format Publisher** — exclusive claim, container creation, readiness/polling, protected publish boundary, outcome classification and synchronization.
3. **Editorial View** — human-facing editorial view.
4. **History & Observability** — operational history.
5. **Content Intake** — fast repository entry.
6. **Repository Operations** — review and actions.
7. **Automatic AI Analysis** — AI-assisted analysis with controlled triggers.
8. **Editorial Decision** — human decision to planner eligibility.
9. **FIFO Planner** — slot assignment with a fail-closed plannable-state allowlist.
10. **Publication State Synchronization** — repository projection.
11. **Consistency Watchdog** — reconciliation with per-item failure isolation.

The publisher owns publication state; the planner owns schedule changes only in allowed states; synchronization owns the repository projection. Confirmed success, deterministic rejection and ambiguous external outcomes follow separate paths, and late errors cannot downgrade protected terminal states. See the [public workflow index](../workflows/PUBLIC_WORKFLOW_INDEX.md).
