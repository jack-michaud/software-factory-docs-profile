# Public Distribution Exclusions

Generated or public `softwarefactorydocs` distributions must exclude all private runtime and operator state.

## Exclude entirely

- credentials, API tokens, OAuth secrets, SSH keys, private certificates,
- environment files and local config overrides,
- auth stores and state databases,
- memory stores, session transcripts, gateway or agent logs,
- Kanban databases, task workspaces, run directories, raw task logs, task IDs, and operational metadata,
- private sprite names, private sprite URLs, Fly.io operational metadata, service inventories, checkpoint identifiers, and deployment logs,
  - Treat every literal `https://*.sprites.app` URL as private unless the exact URL is intentionally approved in `approved-public-sprite-urls.txt` or the line is plainly placeholder/example context.
- user/private notes or vault contents,
- raw traces, crash dumps, or debugging transcripts.

## Safe to include

- conceptual architecture explanations,
- approved public role names and public repository names,
- public release notes summarizing user-visible changes,
- docs-ready release packets after redaction review,
- templates and checklists that describe safety policy without containing real secrets or private local state.

## Rule of thumb

If a detail is not required for a public user to understand, install, use, or contribute to Software Factory, omit it or generalize it.
