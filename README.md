# Advanced Cyber Security & AI Portfolio
### Candidate: [Deadly Sing] | Location: Perth, WA (2026)

This repository demonstrates the deployment of specialized security tools within a constrained, mobile-first environment (iSH/Alpine Linux on iOS). These projects highlight technical proficiency in Python, Bash, and Network Security.

---

## 🛠 Project 1: Sentinel-AI (Automated Threat Analysis)
**Sentinel-AI** is a forensic log analyzer designed to identify unauthorized access attempts.

- **Technical Implementation:** Written in Python 3, leveraging the **Gemini 3 Flash** API for high-speed heuristic analysis.
- **Functionality:** It processes raw authentication logs (`mock_auth.log`), identifies brute-force signatures, and provides a natural language threat assessment.
- **Optimization:** Configured for low-latency inference to minimize resource consumption on mobile hardware.

## 📡 Project 2: Mobile-Recon (Network Discovery & Mapping)
**Mobile-Recon** is an automated reconnaissance utility designed for local network visibility.

- **Technical Implementation:** A modular Bash script utilizing **Nmap 7.91**.
- **The Challenge:** iOS sandboxing blocks raw socket creation (`AF_NETLINK`), which typically prevents port scanning in emulated environments.
- **The Solution:** Implemented **TCP Connect Scans** (`-sT`) and the `--unprivileged` flag. This forces the tool to use standard system calls, allowing for full port discovery without kernel-level permissions.

## 🔐 Project 3: Crypt-Vault (AES-256 Data Protection)
**Crypt-Vault** is a data-at-rest encryption utility for securing sensitive forensic data.

- **Technical Implementation:** Python implementation of the **Fernet (AES-128/256)** specification.
- **Security Logic:** Uses **PBKDF2 (Password-Based Key Derivation Function 2)** with SHA-256 hashing. This ensures that even low-entropy passwords are "stretched" into high-security keys.
- **Utility:** Used to encrypt forensic logs and project assets, ensuring confidentiality even if the local file system is compromised.

---

## 💻 Technical Environment
- **Platform:** iSH Shell (Alpine Linux Emulation) on iOS 15.8.6
- **Device:** iPhone 7 (A10 Fusion Architecture)
- **Version Control:** Git via SSH
