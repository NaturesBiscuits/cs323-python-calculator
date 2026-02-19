Group Members:
Achas, Dan Philip
Belongilot, Clyde Joshua
Butad, John Esteve
Flores, John Vincent

Applied Analysis: CSRS Case
Based on the UP Mindanao CSRS breach, answer the following:
1. If the leaked CSV file had been encrypted symmetrically, would it have reduced
damage?
- Yes. If the leaked CSV file containing approximately 19,000 student and faculty records had been protected using symmetric encryption, the overall damage of the breach would have been significantly reduced.
Even if attackers successfully exfiltrated the file, the data would remain unreadable without the encryption key. This would protect sensitive information such as names, IDs, and academic records from immediate misuse,
thereby limiting privacy violations and secondary attacks such as identity theft or phishing.

2. What if the encryption key was stored on the same compromised server?
- If the symmetric encryption key was stored on the same compromised server as the encrypted CSV file, the protection would be largely ineffective. Once attackers gain access to both the encrypted data and its key, decryption becomes trivial.
This highlights that key management is as critical as encryption itself. Poor key storage practices can nullify the benefits of encryption and still result in full data exposure.

3. Would asymmetric encryption alone protect the entire database?
- No. Asymmetric encryption alone is not practical for protecting an entire database containing 19,000 records.
While asymmetric encryption is excellent for secure key exchange and authentication, it is computationally expensive and inefficient for encrypting large volumes of data. In real-world systems, asymmetric encryption is typically used to securely exchange or protect symmetric keys, not to encrypt bulk data directly.

4. Does encryption prevent data exfiltration, or only protect confidentiality?
- Encryption does not prevent data exfiltration. Attackers can still steal encrypted files from a compromised system.
However, encryption does protect confidentiality, ensuring that stolen data cannot be read or meaningfully used without the correct decryption key. Therefore, encryption reduces the impact of a breach but does not stop the breach itself.

Deliverable
Each group submits a one-page analysis addressing:

Which encryption model is more practical for protecting 19,000 records?
- Symmetric encryption is more practical for protecting 19,000 records due to its speed and efficiency when handling large datasets such as CSV files or databases.
It imposes minimal performance overhead compared to asymmetric encryption and is widely used for data-at-rest protection in real systems.

Where should private keys be securely stored?
- Encryption keys should never be stored on the same server as the encrypted data. Secure storage options include:
Hardware Security Modules (HSMs) Dedicated key management services (KMS), Encrypted key vaults with strict access controls
Environment-based secrets with role-based access and auditing, By Separating keys from data significantly limits attacker capabilities even after system compromise.

Is encryption alone sufficient to prevent data breaches? Explain.
- No. Encryption alone is not sufficient to prevent data breaches.
While it is a critical confidentiality control, it must be combined with other security measures such as access control, intrusion detection, secure authentication, regular patching, and monitoring.
Encryption reduces breach impact, but preventing breaches requires a layered defense (defense-in-depth) approach.


