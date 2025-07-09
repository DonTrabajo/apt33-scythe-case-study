
# 🎯 Bonus Module: Creating an Attack Flow

## 🧠 Objective

This module teaches how to map out attack flows and transform research into structured threat emulation plans. By visualizing the attack lifecycle, red teams can better replicate real-world adversary behaviors in a clear, actionable sequence.

---

## 🧱 Tool Used

**Attack Flow Builder** – from the Center for Threat-Informed Defense

Website: [https://attackflow.org](https://attackflow.org)

---

## 📝 Step-by-Step Guide

### 1. Adding Actions
- Right-click in the Attack Flow canvas → `Create` → `Attack Flow` → `Action`
- Name the action based on behavior (e.g., `Download Payload`, `Disable Logs`)

### 2. Map to MITRE ATT&CK
- Click the action → enter the **Tactic** (e.g., `Defense Evasion`)
- Enter **Technique** using ATT&CK ID (e.g., `T1070 - Indicator Removal on Host`)

### 3. Add Descriptions
- Provide a short explanation in the **Description** field.
- Example: “The adversary cleared security logs on the Windows endpoint.”

### 4. Add Command-Line or STIX Artifact
- Right-click → `Create` → `Attack Flow` → `Action`
- Add a process command: `wevtutil cl System`

---

## 📊 Visual Emulation Flow
Create or import .afb files to visualize full campaigns. You can start with provided templates like:

- **BlackSuit Ransomware.afb** (55KB) — import into the tool to modify and extend.

---

## 🔚 Summary
Mapping an adversary attack flow allows for:

✅ Clear documentation of each adversarial step  
✅ Stronger emulation reproducibility  
✅ MITRE ATT&CK alignment  
✅ Easier collaboration between red/blue/purple teams  
