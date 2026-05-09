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
2. Confirm the release has been approved for public communication.
3. Decide which docs pages require updates.
4. Draft changes using only public-safe evidence.
5. Fill out the redaction checklist.
6. Fill out the docs freshness checklist.
7. Run the safety scanner against proposed content.
8. Return a diff-first handoff with checklist results, validation summary, and any blocked questions.

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
- publication authority or target repo is unclear,
- docs changes would require infrastructure mutation.
