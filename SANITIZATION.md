# Sanitization Policy

This repository is a public case study.

## Never commit

- API keys
- OAuth credentials
- bearer tokens
- session cookies
- private certificates
- production database files
- SQLite WAL/SHM files
- execution dumps
- real account IDs
- private customer/business data
- production webhook URLs
- production hostnames
- internal file-system dumps
- raw Docker volumes
- backup/freeze paths and local usernames
- production workflow version UUIDs, Data Table IDs, Instagram media IDs and execution payloads
- `.env` files
- secrets exported from n8n

## Workflow exports

Before adding a workflow export:

1. remove credential references where possible;
2. replace account-specific IDs;
3. replace real endpoints with placeholders;
4. remove internal webhook paths;
5. remove business/private sample data;
6. inspect Code nodes for embedded secrets;
7. inspect HTTP headers;
8. inspect query parameters;
9. run `scripts/prepublish_audit.py`;
10. review manually.

## Placeholders

Use patterns such as:

```text
YOUR_INSTAGRAM_ACCOUNT_ID
YOUR_CLOUDINARY_CLOUD
YOUR_AI_ENDPOINT
EXAMPLE_WEBHOOK_PATH
```

## Evidence

Production hashes and release evidence should remain in the private case archive unless there is a reason to expose a specific non-sensitive artifact.

## Final audit scope

Before commit, search the entire repository for tokens, bearer strings, access tokens, credential IDs, private paths, account IDs, production webhook URLs, media IDs, databases, backups and real operational content. Any match is reviewed manually; structural placeholders are preferred.
