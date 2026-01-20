Platinum Master Data Tool: Requirements Specification
1. Universal Data Ingestion (The "Super Driver")
Requirement: The system must automatically detect and process the most common data formats used in modern business, web, and legacy systems.

Supported Formats:

✅ Excel (.xlsx, .xls): Standard business reporting.

✅ CSV (.csv): Standard data exchange.

✅ JSON (.json): Modern web APIs and JavaScript applications.

✅ Parquet (.parquet): Enterprise Big Data systems.

✅ Pipe-Delimited (.txt, .dat): Legacy government and banking mainframes.

2. Automated Fault Tolerance (The "Quarantine")
Requirement: The production line must never stop due to a single bad file.

Behavior: If a file is corrupt or unreadable, the system must:

Catch the specific error.

Log the error details.

Physically move the file to the Quarantine folder to isolate it from good data.

3. Security & Intellectual Property Protection
Requirement: The source code must be protected from unauthorized reading or tampering when not in use.

Implementation:

Encryption: AES-128 encryption via the cryptography library.

Key Management: A unique, locally generated vault.key file is required to unlock the code.

4. Full Auditability (Logging)
Requirement: Every action taken by the system must be recorded for compliance and debugging.

Implementation: A session log (session_history.log) tracks every file processed, every success, and every failure with a precise timestamp.

5. Technical Dependencies (The "Fuel")
Requirement: The host environment must have the following Python libraries installed to support the engine:

pandas (Data manipulation)

openpyxl (Excel engine)

pyarrow (Parquet engine - NEW)

cryptography (Security engine)
