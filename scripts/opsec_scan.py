#!/usr/bin/env python3
import argparse
import os
import re
import sys

DEFAULT_EXCLUDES = {".git", "venv", ".venv", "__pycache__"}
BINARY_EXTS = {
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".pdf",
    ".zip",
    ".exe",
    ".dll",
    ".bin",
}

def build_pattern(parts, flags=0):
    return re.compile("".join(parts), flags)


RULES = [
    ("hostname_local", build_pattern([r"\.", "lo", "cal", r"\b"], re.IGNORECASE)),
    ("operator_name", build_pattern([r"\b", "fel", "ix", r"\b"], re.IGNORECASE)),
    ("windows_user_path", build_pattern(["C:\\\\", "Users\\\\"] , re.IGNORECASE)),
    ("mac_user_path", build_pattern(["/", "Users/"], re.IGNORECASE)),
    ("appdata_path", build_pattern(["App", "Data\\\\"], re.IGNORECASE)),
    ("ssh_path", build_pattern([r"\.", "ssh", r"\b"], re.IGNORECASE)),
    ("aws_path", build_pattern([r"\.", "aws", r"\b"], re.IGNORECASE)),
    (
        "private_ip",
        build_pattern(
            [
                r"\b(",
                "10",
                r"\.",
                r"\d{1,3}\.|",
                "172",
                r"\.",
                "(1[6-9]|2\\d|3[01])",
                r"\.|",
                "192",
                r"\.",
                "168",
                r"\.",
                ")",
            ]
        ),
    ),
    ("aws_key", build_pattern(["AK", "IA", "[0-9A-Z]{16}"])),
    ("github_token", build_pattern(["g", "hp_", "[0-9A-Za-z]+"])),
    ("slack_token", build_pattern(["xo", "x", "[baprs]-"])),
    ("openai_key", build_pattern(["s", "k-", "[0-9A-Za-z]+"])),
    (
        "private_key_block",
        build_pattern(["BEGIN ", "(RSA|OPENSSH|EC)", " PRIVATE KEY"]),
    ),
    (
        "credential_strings",
        build_pattern(["Pass", "word:", "|pass", "wd|p", "wd"], re.IGNORECASE),
    ),
]

IP_REGEX = re.compile(
    r"\b(?:25[0-5]|2[0-4]\d|1?\d?\d)(?:\.(?:25[0-5]|2[0-4]\d|1?\d?\d)){3}\b"
)
ALLOWED_IP_PREFIXES = ("192.0.2.", "198.51.100.", "203.0.113.")


def is_allowed_ip(ip: str) -> bool:
    return ip.startswith(ALLOWED_IP_PREFIXES)


def iter_files(root: str):
    for base, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in DEFAULT_EXCLUDES]
        for name in files:
            path = os.path.join(base, name)
            _, ext = os.path.splitext(path)
            if ext.lower() in BINARY_EXTS:
                continue
            yield path


def scan_file(path: str, root: str):
    rel = os.path.relpath(path, root)
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as handle:
            for idx, line in enumerate(handle, 1):
                for rule_name, pattern in RULES:
                    if pattern.search(line):
                        yield rel, idx, rule_name
                for ip in IP_REGEX.findall(line):
                    if not is_allowed_ip(ip):
                        yield rel, idx, "non_rfc5737_ip"
    except OSError:
        return


def main() -> int:
    parser = argparse.ArgumentParser(description="OPSEC regression scan")
    parser.add_argument("--root", default=".", help="Root directory to scan")
    args = parser.parse_args()

    root = os.path.abspath(args.root)
    findings = []

    for path in iter_files(root):
        for rel, line_no, rule_name in scan_file(path, root):
            findings.append((rel, line_no, rule_name))

    if findings:
        for rel, line_no, rule_name in findings:
            print(f"FOUND suspicious pattern at {rel}:{line_no} -> [REDACTED] ({rule_name})")
        print(f"OPSEC scan failed with {len(findings)} finding(s).")
        return 1

    print("OPSEC scan passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
