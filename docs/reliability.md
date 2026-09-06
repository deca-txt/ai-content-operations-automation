# Reliability & Release Engineering

## Reliability goals

The product must:

- preserve state;
- avoid duplicate effects;
- detect inconsistency;
- survive restart;
- keep publishing history immutable;
- expose operational state;
- provide evidence for release decisions.

---

## Watchdog & reconciliation

A dedicated watchdog checks for consistency problems.

A reusable synchronization component centralizes reconciliation logic instead of duplicating it across workflows.

---

## Execution retention

The system uses aggressive execution retention to control SQLite growth.

The exact production configuration is intentionally not duplicated here, but the principle is:

- retain enough history for diagnosis;
- avoid unbounded execution accumulation;
- separate product data from execution history.

---

## SQLite integrity

Release validation includes SQLite integrity checks.

A clean result is required before freeze.

---

## Baseline hashing

The production workflow set is reduced to a deterministic baseline hash.

That makes it possible to detect unintended workflow changes during audit.

Public repository hashes are not production secrets, but detailed internal evidence is intentionally kept private.

---

## Restart / recovery

The final release included a controlled restart test:

1. verify preconditions;
2. stop runtime;
3. create consistent backup;
4. start runtime;
5. verify application health;
6. verify functional endpoint readiness;
7. revalidate data invariants;
8. confirm no post-restart execution failures.

A useful lesson emerged:

> application health and functional readiness are not always the same event.

---

## Release claim

The project intentionally avoids claiming that software is “bug free”.

The final claim is:

> zero known defects + all critical invariants PASS + final adversarial release suite PASS
