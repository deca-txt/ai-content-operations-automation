# Sanitized Workflow Exports

Do not copy production workflow exports directly into this folder.

Only reviewed and sanitized exports should be added.

The current public set is the eleven reviewed structure-only blueprints listed in `PUBLIC_WORKFLOW_INDEX.md`.

Recommended future additions:

- content-intake.example.json
- ai-analysis.example.json
- editorial-decision.example.json
- fifo-planner.example.json
- publisher.example.json
- synchronization.example.json
- watchdog.example.json

These should communicate architecture without exposing production details. WF02, WF05E and WF07 are accompanied by behavior notes in the public case documentation because their state-machine boundaries are central to V1.

## Gate

No JSON workflow should be published until:
- automated scan passes;
- manual credential/API review passes;
- identifiers are replaced;
- sample data is synthetic.
