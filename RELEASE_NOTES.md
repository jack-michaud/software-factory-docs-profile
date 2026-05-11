# software-factory-docs-profile v0.1.0

Generated Hermes profile distribution for Software Factory documentation maintenance.

- Source repo: https://github.com/jack-michaud/software-factory
- Source tag: profiles/v0.1.0
- Source commit: 63035a90746ab304b7e8c5f231d9d89c2106e9d8
- Generated manifest: distribution.yaml
- Generated tree hash: ab857f752986153855e2a50a1f1530ea33cf60e38de3ffd09a773141a1cdec5f
- Validation: docs validate_public_safety.py exit 0
- Public-safety scan: 0 findings in publisher preflight
- Publication gates: human approval, dry-run validation, and publisher execution completed.

Branch protection is intentionally deferred for v0 by human decision.

## Unreleased

- Switched the docs profile default model to the approved GPT-5.3 Codex Spark pilot coordinate (`gpt-5.3-codex-spark` via `openai-codex` with `chat_completions`) while preserving the existing docs role authority boundaries.
- Restructured `SOUL.md` into an actual progressive-disclosure root map with detailed conditional role doctrine moved to `references/role-operating-guidance.md` and distribution-managed reference wiring.
- Added progressive-disclosure Kanban task-spec guidance so root profile instructions remain concise maps while detailed PM/task-writing doctrine lives in linked references with explicit `When X, read Y` triggers. The guidance defines required task fields, evidence-linked acceptance criteria, and role-specific routing for future maintainers.
