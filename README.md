# softwarefactorydocs Profile Skeleton

This directory is the public distribution source for the `softwarefactorydocs` Hermes profile. It is intentionally least-privilege and docs-deployment-aware: the profile maintains public Software Factory documentation and release notes from release handoff artifacts, and it may update the dedicated Software Factory docs sprite/site when a task explicitly identifies that target and requests deployment. It must not mutate unrelated sprites, broad Fly.io infrastructure, pi-sprite workers, production profile distributions, or private operational state.

## Mission

Maintain public Software Factory documentation as a product surface:

- keep docs information architecture coherent,
- update release notes from approved release packets,
- check public/private redaction boundaries before proposing docs changes,
- flag stale or missing docs through follow-up tasks,
- avoid unsupported claims not backed by release evidence.

## Authority boundaries

Default profile authority deliberately distinguishes scoped authority from no authority. `role-capability-manifest.yaml` is the source of truth for allowed mutation targets, credential rules, canonical workspaces, and completion-vs-handoff criteria.

Allowed by default:

- read public docs repository content,
- read docs-ready release packets supplied to the profile,
- draft docs changes, release notes, changelog entries, and review checklists,
- produce diffs or pull-request-ready patches,
- update the dedicated Software Factory docs sprite/site when the task identifies the target and requests deployment,
- create required before/after checkpoints for that dedicated docs-site mutation,
- open follow-up work items when evidence is missing or unsafe.

Not allowed by default:

- no unrelated sprite create/deploy/checkpoint/mutate operations,
- no broad Fly.io commands or unrelated sprite service changes,
- no pi-sprite/pi-orchestrator mutation,
- no production profile distribution publication,
- no direct access to raw Kanban databases/workspaces, private logs, memories, sessions, local state, credentials, or private sprite metadata,
- no direct publishing credentials unless a separate human-approved publication workflow grants narrow docs-repo write access.

If a task expects deployed docs, local PR-ready content alone is not success. Resolve the dedicated docs deployment target from an explicit task handoff or `SOFTWARE_FACTORY_DOCS_SPRITE_NAME`; if neither is available, block with a precise target request instead of guessing.

## Distribution contents

- `SOUL.md` — role identity, behavior, and hard boundaries.
- `distribution.yaml` — profile distribution metadata and owned-file list.
- `config.yaml` — pins the public distribution model/provider/api-mode (`gpt-5.3-codex-spark`, `openai-codex`, `chat_completions`) for the approved docs Spark pilot. This docs profile intentionally does not configure `skills.external_dirs`; its authority and local skills remain limited to `SOUL.md`, `role-capability-manifest.yaml`, and `skills/public-docs-maintenance/`.
- `role-capability-manifest.yaml` — machine-readable role authority, credential, target, and completion contract.
- `skills/public-docs-maintenance/SKILL.md` — reusable operating procedure for docs updates.
- `templates/release-packet.md` — release-to-docs packet schema.
- `templates/release-notes.md` — public release notes template.
- `templates/redaction-checklist.md` — public/private safety review checklist.
- `templates/docs-freshness-checklist.md` — post-release docs freshness review.
- `templates/profile-distribution-docs-update-checklist.md` — profile distribution docs update review.
- `templates/role-capability-readiness-checklist.md` — readiness gate for role capability manifests.
- `scripts/validate_public_safety.py` — local safety scanner for this distribution.
- `scripts/validate_capability_manifest.py` — readiness scanner for the role capability manifest.
- `EXCLUSIONS.md` — explicit exclusion policy for generated/public distributions.

## Required inputs for docs work

The profile should only consume docs-ready inputs:

1. release packet using `templates/release-packet.md`,
2. reviewer-approved public URLs/repo links,
3. PM-authored product decisions explicitly marked public-safe,
4. changelog fragments with private fields removed or marked for redaction,
5. current public docs repository content.

## Default workflow

1. Validate the release packet has all required fields.
2. Confirm release approval for public communication.
3. Load `role-capability-manifest.yaml` and decide whether the task requires deployed docs, PR-ready content, or a handoff.
4. Draft docs/release-note diffs from user-visible evidence only.
5. Run redaction and freshness checklists.
6. Run the public-safety and capability-manifest validation scripts on the proposed docs tree.
7. If deployment is requested, resolve the target from an explicit task handoff or `SOFTWARE_FACTORY_DOCS_SPRITE_NAME`, update only that dedicated docs site with before/after checkpoints, and verify the public page.
8. Return diffs, checklist evidence, validation summaries, and deployed URL/status when applicable.

## Installation status

This repository is the source-controlled public `softwarefactorydocs` profile distribution. Runtime profile installs should use `hermes profile install` / `hermes profile update` from this repository so `SOUL.md`, `role-capability-manifest.yaml`, templates, and validation scripts stay in sync.


Install after publication:

```bash
hermes profile install https://github.com/jack-michaud/software-factory-docs-profile.git --name softwarefactorydocs
```

Update after publication:

```bash
hermes profile update softwarefactorydocs --yes
```

## Publication provenance

Version: v0.1.0
Source of truth: https://github.com/jack-michaud/software-factory
Source tag: profiles/v0.1.0
Source commit: 63035a90746ab304b7e8c5f231d9d89c2106e9d8
Generated manifest: distribution.yaml
License: MPL-2.0

This repository is the generated Software Factory documentation-agent profile distribution. File issues and feature requests on https://github.com/jack-michaud/software-factory.
## Optional docs deployment target

This distribution declares `SOFTWARE_FACTORY_DOCS_SPRITE_NAME` as an optional env var. Set it in the installed profile's user-owned `.env` when deployed docs tasks should publish/update a dedicated docs sprite. For this environment the expected non-secret value is `hermes-sf-docs`. If deployment is requested and neither a task-supplied target nor this env var is available, the docs profile must block or skip publication instead of guessing. Distribution installs/updates must not overwrite `.env`.
