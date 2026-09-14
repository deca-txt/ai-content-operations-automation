# V1 Release Notes

## Status

**V1 complete · production validated · operational release**

```text
GATE_Z=PASS
V1_OPERATIONAL_RELEASE=PASS
V1=COMPLETE
KNOWN_CRITICAL_DEFECTS=0
FUNCTIONAL_BLOCKERS=0
OPEN_TECH_DEBT=0
```

The release included runtime and Compose hygiene, workflow cleanup, backup, freeze and documentation closure. Accepted historical exceptions remain summarized and do not block normal operation.

## Real canary

The clean canary passed planning, exclusive claim, creation-ID preservation, one media publish, no duplicate publication, state flow, terminality, synchronization and post-publish planner immutability. Queue and repository ended `PUBLISHED`; global inconsistencies were `0`.

## Iterations from real findings

- carousel partial-success risk → exact child cardinality and atomic preparation;
- concurrent executions → exclusive claim/ownership;
- external ambiguity → protected outcome state and no blind retry;
- late error regression → terminality guards;
- environment binding mismatch → target-environment validation;
- creation-ID collision → explicit `meta_creation_id`;
- planner state violation → fail-closed allowlist;
- watchdog propagation → per-item failure isolation.
