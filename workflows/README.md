# Sanitized Workflow Exports

Do not copy production workflow exports directly into this folder.

Only reviewed and sanitized exports should be added.

Recommended public set:

- content-intake.example.json
- ai-analysis.example.json
- editorial-decision.example.json
- fifo-planner.example.json
- publisher.example.json
- synchronization.example.json
- watchdog.example.json

These should communicate architecture without exposing production details.

## Gate

No JSON workflow should be published until:
- automated scan passes;
- manual credential/API review passes;
- identifiers are replaced;
- sample data is synthetic.
