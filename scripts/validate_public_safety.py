#!/usr/bin/env python3
"""Validate the softwarefactorydocs skeleton for public-safety hygiene.

The scanner is conservative about real leaks (absolute local paths, task IDs,
private sprite URLs, obvious credential assignments, and forbidden runtime files)
while allowing templates/policy docs to mention excluded file names as examples.

Sprite URL rule: any literal https://*.sprites.app URL is treated as private by
default. It is allowed only when the exact URL appears in an explicit allowlist
file named approved-public-sprite-urls.txt at the scan root, or when the matching
line is clearly placeholder/example context rather than a live operational URL.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT_ARG = sys.argv[1] if len(sys.argv) > 1 else None
ROOT = Path(ROOT_ARG).resolve() if ROOT_ARG else Path(__file__).resolve().parents[1]
ROOT_DISPLAY = ROOT_ARG if ROOT_ARG else str(ROOT)

SKIP_DIRS = {'.git', '__pycache__', '.pytest_cache', 'node_modules', 'dist', 'build'}
FORBIDDEN_FILENAMES = {
    '.env', 'auth.json', 'state.db', 'kanban.db', 'credentials.json', 'id_rsa', 'id_ed25519'
}
FORBIDDEN_DIRNAMES = {'sessions', 'logs', 'memory', 'memories', 'workspaces', 'checkpoints'}
APPROVED_PUBLIC_URLS_FILE = 'approved-public-sprite-urls.txt'
PLACEHOLDER_CONTEXT_RE = re.compile(
    r'(?i)(placeholder|example|sample|template|replace[- ]me|your[-_ ]sprite|approved[-_ ]public)'
)
PATTERNS = {
    'absolute_home_path': re.compile(r'/home/[^\s)`>]+'),
    'kanban_task_id': re.compile(r'\bt_[0-9a-f]{8,}\b'),
    'sprite_url': re.compile(r'https://[^\s)`>"\']*\.sprites\.app\b'),
    'secret_assignment': re.compile(r'(?i)(api[_-]?key|token|secret|password)\s*[:=]\s*[^\s<>{}\[\]"\'`]+'),
    'private_key_block': re.compile(r'-----BEGIN (?:RSA |OPENSSH |EC |DSA )?PRIVATE KEY-----'),
}


def load_approved_public_urls(root: Path) -> set[str]:
    path = root / APPROVED_PUBLIC_URLS_FILE
    if not path.exists():
        return set()
    approved: set[str] = set()
    for raw_line in path.read_text(encoding='utf-8').splitlines():
        line = raw_line.strip()
        if not line or line.startswith('#'):
            continue
        approved.add(line.rstrip('/'))
    return approved


def is_placeholder_sprite_url(url: str, line: str) -> bool:
    parsed = urlparse(url)
    host = (parsed.hostname or '').lower()
    if host in {'example.sprites.app', 'placeholder.sprites.app'}:
        return True
    if host.startswith(('example-', 'placeholder-', 'sample-', 'your-sprite')):
        return True
    return bool(PLACEHOLDER_CONTEXT_RE.search(line))


approved_public_urls = load_approved_public_urls(ROOT)
findings = []
files_scanned = 0
policy_mentions = []

for path in sorted(ROOT.rglob('*')):
    rel = path.relative_to(ROOT)
    if any(part in SKIP_DIRS for part in rel.parts):
        continue
    if path.is_dir():
        if path.name in FORBIDDEN_DIRNAMES:
            findings.append({'type': 'forbidden_directory', 'path': str(rel)})
        continue
    if path.name in FORBIDDEN_FILENAMES:
        findings.append({'type': 'forbidden_filename', 'path': str(rel)})
    try:
        text = path.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        findings.append({'type': 'non_text_file', 'path': str(rel)})
        continue
    files_scanned += 1
    for name, pattern in PATTERNS.items():
        for match in pattern.finditer(text):
            # Allow this validator's source to contain the regex examples and
            # policy constants it enforces.
            if rel.as_posix() == 'scripts/validate_public_safety.py':
                continue
            matched = match.group(0)
            line_start = text.rfind('\n', 0, match.start()) + 1
            line_end = text.find('\n', match.end())
            if line_end == -1:
                line_end = len(text)
            line = text[line_start:line_end]
            if name == 'sprite_url':
                normalized = matched.rstrip('/')
                if normalized in approved_public_urls or is_placeholder_sprite_url(normalized, line):
                    continue
                findings.append({'type': 'private_sprite_url', 'path': str(rel), 'match': matched[:120]})
                continue
            findings.append({'type': name, 'path': str(rel), 'match': matched[:120]})
    if any(term in text for term in ['.env', 'auth.json', 'state.db', 'kanban.db', 'sessions', 'logs', 'workspaces']):
        policy_mentions.append(str(rel))

result = {
    'root': ROOT_DISPLAY,
    'files_scanned': files_scanned,
    'findings': findings,
    'policy_mentions': sorted(set(policy_mentions)),
    'approved_public_sprite_urls': sorted(approved_public_urls),
    'passed': not findings,
}
print(json.dumps(result, indent=2, sort_keys=True))
sys.exit(0 if not findings else 1)
