# softwarefactorydocs Profile Skeleton

This directory is a draft distribution source for a future `softwarefactorydocs` Hermes profile. It is intentionally least-privilege and PR/diff-first: the profile maintains public Software Factory documentation and release notes from release handoff artifacts, but does not mutate sprites, Fly.io infrastructure, pi-sprite workers, production profile distributions, or private operational state by default.

## Mission

Maintain public Software Factory documentation as a product surface:

- keep docs information architecture coherent,
- update release notes from approved release packets,
- check public/private redaction boundaries before proposing docs changes,
- flag stale or missing docs through follow-up tasks,
- avoid unsupported claims not backed by release evidence.

## Authority boundaries

Default profile authority deliberately excludes unrestricted shell access. `distribution.yaml` allows file/web/search/kanban/skills toolsets only; `terminal` is listed solely as an optional, separately granted local validation capability for running static checks in an isolated workspace. That optional validation capability is not part of default profile authority and does not grant sprite, Fly.io, pi-sprite, or pi-orchestrator mutation.

Allowed by default:

- read public docs repository content,
- read docs-ready release packets supplied to the profile,
- draft docs changes, release notes, changelog entries, and review checklists,
- produce diffs or pull-request-ready patches,
- open follow-up work items when evidence is missing or unsafe.

Not allowed by default:

- no sprite create/deploy/checkpoint/mutate operations,
- no Fly.io commands or sprite service changes,
- no pi-sprite/pi-orchestrator mutation,
- no production profile distribution publication,
- no direct access to raw Kanban databases/workspaces, private logs, memories, sessions, local state, credentials, or private sprite metadata,
- no direct publishing credentials unless a separate human-approved publication workflow grants narrow docs-repo write access.

If a task requires infrastructure mutation, publication credentials, DNS, or private operational evidence, the docs profile must create a builder/reviewer/PM handoff instead of acting directly.

## Distribution contents

- `SOUL.md` — role identity, behavior, and hard boundaries.
- `distribution.yaml` — proposed least-privilege distribution metadata.
- `skills/public-docs-maintenance/SKILL.md` — reusable operating procedure for docs updates.
- `templates/release-packet.md` — release-to-docs packet schema.
- `templates/release-notes.md` — public release notes template.
- `templates/redaction-checklist.md` — public/private safety review checklist.
- `templates/docs-freshness-checklist.md` — post-release docs freshness review.
- `templates/profile-distribution-docs-update-checklist.md` — profile distribution docs update review.
- `scripts/validate_public_safety.py` — local safety scanner for this skeleton.
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
3. Draft docs/release-note diffs from user-visible evidence only.
4. Run redaction and freshness checklists.
5. Run the public-safety validation script on the proposed docs tree.
6. Return a diff and checklist evidence; do not publish unless separately authorized.

## Installation status

This is a skeleton artifact only. It is not published externally and has not been installed into a production Hermes profile distribution by this task.

## Publication provenance

Version: v0.1.0
Source of truth: https://github.com/jack-michaud/software-factory
Source tag: profiles/v0.1.0
Source commit: 63035a90746ab304b7e8c5f231d9d89c2106e9d8
Generated manifest: distribution.yaml
License: MPL-2.0

This repository is the generated Software Factory documentation-agent profile distribution. File issues and feature requests on https://github.com/jack-michaud/software-factory.
