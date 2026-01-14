# APT33 SCYTHE Case Study (Public-Safe)

## Executive Summary
- Emulated APT33-like behaviors in a controlled lab for detection validation.
- Focused on discovery, persistence, and impact behaviors commonly observed in public reporting.
- Produced Sigma rules and Splunk queries to validate telemetry coverage.
- Prioritized reproducibility and safety by excluding credentials, targets, and production systems.
- Captured lessons learned to improve future emulation realism and detection fidelity.

## Threat Emulated
APT33, a publicly reported threat group, was emulated at a high level. The goal was to model realistic behavior patterns without reproducing operational tooling or target-specific procedures.

## Lab-Only Scope and Disclaimers
- All activity is limited to a private lab environment with dummy data.
- No real credentials, malware, or external targets are used.
- This document omits copy-paste offensive commands and internal infrastructure details by design.

## Emulation Plan (Phases)
1. Preparation: establish baseline logging and create benign test files.
2. Initial access simulation: user-initiated execution of a benign payload.
3. Discovery: host, user, and network discovery behaviors.
4. Persistence: simulate a registry-based persistence mechanism using benign binaries.
5. Defense evasion: simulate log clearing in a controlled lab only.
6. Collection and exfiltration: generate and stage a small dummy file and simulate transfer.
7. Impact: simulate encryption of dummy files only.

## Defender View
- Sigma rules are available in `detections/` to capture discovery and tool execution patterns.
- Splunk hunting queries are available in `queries/` to validate detections against lab telemetry.
- Telemetry sources include Windows event logs, Sysmon process creation, and PowerShell logging.

## MITRE ATT&CK Mapping
| Technique ID | Name | Where in Plan | Detection Notes |
| --- | --- | --- | --- |
| T1059 | Command and Scripting Interpreter | Discovery phase | Process creation and PowerShell logging |
| T1087 | Account Discovery | Discovery phase | Command-line discovery indicators |
| T1016 | System Network Configuration Discovery | Discovery phase | Network discovery commands |
| T1112 | Modify Registry | Persistence phase | Registry modification telemetry |
| T1070 | Indicator Removal on Host | Defense evasion phase | Event log clearing behaviors |
| T1486 | Data Encrypted for Impact | Impact phase | File modification patterns and process ancestry |

## Lessons Learned and Next Improvements
- Expand detection coverage for parent-child process anomalies.
- Add timeline correlation between discovery and persistence phases.
- Validate Sigma portability across multiple SIEM backends.

Prox Offensive | Emulate. Detect. Evolve.
