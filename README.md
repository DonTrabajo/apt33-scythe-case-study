# APT33 SCYTHE Case Study

Public-safe case study of an APT33-like emulation exercise using an adversary emulation platform and defensive detections. This repo focuses on methodology and detection artifacts; step-by-step offensive commands and lab identifiers are intentionally excluded.

Built and executed by DonTrabajo. Released under the MIT License.

## Contents
- `case-study.md`: One-page public case study with ATT&CK mapping, lessons learned, [Telemetry required](case-study.md#telemetry-required), and [Results](case-study.md#results).
- `emulation/apt33_emulation_plan.md`: High-level, lab-only emulation phases (no commands).
- `emulation/attack-flow.md`: Guidance for modeling the flow without operational details.
- `detections/`: Sigma rules used in the defender view.
- `queries/`: Splunk hunting queries derived from Sigma logic.
- `License.md`: License info (MIT).
- `.gitignore`: Basic ignore patterns for text-based infosec repos.

## Summary
- APT33-like behaviors are modeled at a high level for lab-only use.
- Defensive artifacts (Sigma + Splunk) are included for detection validation.
- Internal infrastructure details and credentials are omitted by design.

Prox Offensive | Emulate. Detect. Evolve.
