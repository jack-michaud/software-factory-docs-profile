---
name: public-docs-maintenance
description: Maintain public Software Factory docs and release notes from approved release packets without exposing private operational state.
version: 0.1.0
metadata:
  hermes:
    tags: [software-factory, docs, release-notes, redaction]
---

# Public Docs Maintenance

Use this skill when updating Software Factory public documentation, release notes, changelogs, profile-distribution docs, or safety pages from release handoff artifacts.

## Inputs

Require a docs-ready release packet with:

- release identifier,
- release type,
- public summary,
- user-visible changes,
- profile changes if relevant,
- intended public artifacts,
- summarized verification evidence,
- migration notes,
- known issues,
- security/privacy review outcome,
- docs pages requiring updates,
- redaction status.

Do not use raw logs, private task workspaces, memory/session stores, credentials, private URLs, or local operational metadata as public source material.

## Procedure

1. Read the release packet and confirm required fields are present.
2. Load `role-capability-manifest.yaml` from the profile distribution and identify whether the task expects local docs edits, repository publication, or deployed docs-site changes.
3. Confirm the release has been approved for public communication.
4. Decide which docs pages require updates.
5. Draft changes using only public-safe evidence.
6. Fill out the redaction checklist.
7. Fill out the docs freshness checklist.
8. Run the safety scanner and capability-manifest scanner against proposed content.
9. If the task expects deployed docs and identifies the dedicated docs sprite/site, update only that target with before/after checkpoint discipline and verify the public page.
10. Return diffs, checklist results, validation summary, deployed URL/status when applicable, and any blocked questions.

## Writing rules

- Say what changed for users, not how private operators executed the change.
- Use public links only when intentionally approved.
- Replace private implementation identifiers with conceptual names.
- Do not expose raw task IDs, run IDs, local paths, private sprite URLs, private repository names, or checkpoint IDs.
- Do not infer product claims not stated in release evidence.

## Escalation

Block and ask PM/human when:

- release evidence is missing or contradictory,
- a field is marked redaction-required and no public wording is supplied,
- publication/deployment authority or target repo/site is unclear,
- the task expects deployed docs but does not identify the dedicated docs sprite/site,
- docs changes would require mutation outside the scoped docs targets in `role-capability-manifest.yaml`.
