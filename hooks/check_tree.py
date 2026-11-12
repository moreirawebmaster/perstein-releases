#!/usr/bin/env python3
import argparse
import subprocess
import sys

FORBIDDEN_SUFFIXES = (
    ".dmg",
    ".zip",
    ".exe",
    ".pkg",
    ".msi",
    ".deb",
    ".rpm",
    ".tar.gz",
    ".tgz",
    ".sig",
    ".sha256",
)
MAGICS = (
    b"MZ",
    b"\x7fELF",
    b"PK\x03\x04",
    b"\xcf\xfa\xed\xfe",
    b"\xfe\xed\xfa\xcf",
    b"\xfe\xed\xfa\xce",
    b"\x1f\x8b",
    b"7z\xbc\xaf",
    b"xar!",
)


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], text=True)


def forbidden_name(path: str) -> bool:
    lowered = path.lower()
    return lowered.endswith(FORBIDDEN_SUFFIXES)


def forbidden_bytes(blob: bytes) -> bool:
    if b"\x00" in blob[:8192]:
        return True
    head = blob[:8]
    return any(head.startswith(magic) for magic in MAGICS)


def blobs(rev: str) -> list[tuple[str, str]]:
    out = git("ls-tree", "-r", "--full-tree", rev)
    found = []
    for line in out.splitlines():
        meta, path = line.split("\t", 1)
        mode, kind, sha = meta.split()
        if kind == "blob":
            found.append((path, sha))
    return found


def check_rev(rev: str) -> list[str]:
    problems = []
    for path, sha in blobs(rev):
        if forbidden_name(path):
            problems.append(f"{rev[:12]} {path}: extensão de binário ou checksum")
            continue
        raw = subprocess.check_output(["git", "cat-file", "blob", sha])
        if forbidden_bytes(raw):
            problems.append(f"{rev[:12]} {path}: conteúdo binário")
    return problems


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--commit")
    parser.add_argument("--all", action="store_true")
    args = parser.parse_args()
    revs = [args.commit] if args.commit else []
    if args.all:
        revs = git("rev-list", "--all").split()
    if not revs:
        revs = [git("rev-parse", "HEAD").strip()]
    problems = []
    for rev in revs:
        problems.extend(check_rev(rev))
    if problems:
        print("\n".join(problems), file=sys.stderr)
        return 1
    print(f"tree ok ({len(revs)} commit(s))")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
