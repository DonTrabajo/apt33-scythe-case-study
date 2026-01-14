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

## Telemetry required

### Data sources
- Windows Security Event Log (logon events, account management).
- Sysmon (process creation, network connections, image loads) if deployed.
- EDR telemetry (process tree, command line, network).
- DNS logs (resolver and endpoint DNS where available).
- Proxy or web gateway logs (egress destinations and user agent).
- Firewall or NetFlow (lateral movement visibility).
- AnyDesk logs if remote access tooling is in scope.
- PowerShell logging (Module and Script Block).

### Expected signals and tuning notes
- Sigma rules in `detections/` should trigger on discovery and tooling patterns.
- False positives are likely from legitimate admin tooling and IT scripts.
- Prefer allowlisting signed binaries and approved tool hashes where available.
- Correlate user, host, and time window to reduce noise.
- Look for new binaries paired with outbound connections or service creation.

## Results

### What worked
- Process creation and command-line telemetry were the most reliable signal sources.
- Discovery patterns mapped cleanly to `detections/` and `queries/` with minimal tuning.
- Correlation of new binary execution plus outbound connections improved fidelity.
- Service and persistence-related events aligned with expected emulation signals.

### What produced noise
- Legitimate IT/admin tooling triggered discovery-like patterns.
- Approved remote access tools produced alerts similar to adversary tooling.
- Broad query patterns required allowlisting to avoid routine admin activity.

### Next iteration improvements
- Enrich detections with parent-child process constraints.
- Add allowlist patterns for known admin hosts and approved tools.
- Add correlation rules with time windows across user and host context.
- Expand queries to include lateral movement pivots.
- Validate detections on additional lab endpoints and datasets.

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
