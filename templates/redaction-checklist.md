# Public/Private Redaction Checklist

Complete before proposing or publishing docs/release-note changes.

## Blockers: must not appear in public content

- [ ] Credentials, API tokens, OAuth secrets, SSH keys, private certs absent.
- [ ] Environment/config secret files absent.
- [ ] Auth stores, state databases, memory stores, sessions, and logs absent.
- [ ] Raw Kanban DB/workspace references absent.
- [ ] Raw task IDs, run IDs, checkpoint IDs, and operational metadata absent.
- [ ] Private sprite names/URLs and Fly.io operational metadata absent.
- [ ] User/private notes or vault content absent.
- [ ] Raw traces, crash dumps, and debug transcripts absent.
- [ ] Local filesystem paths absent.

## Wording checks

- [ ] Claims are supported by release evidence.
- [ ] Internal implementation details are generalized unless explicitly public.
- [ ] Public links are intentionally approved.
- [ ] Known limitations are stated clearly.
- [ ] No private person/user data is included.

## Decision

- redaction review passed: yes | no
- reviewer:
- unresolved questions:
