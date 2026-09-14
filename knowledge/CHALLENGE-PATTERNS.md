# Knowledge — patterns that solve OSINT CTF challenges

Sanitized lessons from live OSINT CTFs (including Deep Threats–style scenarios).  
Techniques only — no personal cookies, tokens, or private message history.

## Steganography & files
- A **ZIP can be appended/hidden inside a PNG/JPG** (polyglot / after IEND). Check with `binwalk`, `foremost`, or `zip` magic bytes (`PK\x03\x04`).
- Passworded ZIP: derive passphrase from OSINT lore (ferry names, mottos, bilingual hints) — not blind rockyou if rules forbid bruteforce.
- EXIF / C2PA / AI watermarks: useful metadata, not always the flag.

## Dual networks / TLDs
- Fiction nations often split **internal** TLDs (e.g. `.ln`) vs **Internet-exposed** (`.int`, clearnet).
- WHOIS “internal only” vs public A records → which host is worth opening.
- Wiki pages on “domain extensions” are often the hint.

## Document trails
- `robots.txt` → unexpected paths; Apache `server-status` sometimes **lists** sensitive dirs (if already exposed — do not fuzz for it).
- Strategic PDFs / NDAs / SDA contracts: search articles on “alternative transfer”, export control, IP assignment.
- National law portals (`.gouv.*`): minerals export, intelligence cooperation duties, patent offices.

## People & influence
- Think-tank façade ↔ darknet messenger: creds from OSINT (sticky notes OCR → ASCII, social bios), never bruteforce login.
- Official title on government page beats “also advises …” blurbs on university sites.
- Threat emails: parse `Received` / `X-Originating-IP` → infra → civil registry / company registry.

## Money & chain
- Testnet ETH memos (UTF-8 input data) can name payers / invoice refs.
- Faucet → intermediary → target; flag may be in the **memo**, not the address.

## CTFd hygiene
- Session cookie lets you inventory challenges; wrong submits cost points.
- Automating **fuzz** against event infra = ban risk. Soft OSINT only.

## Mapping
- Maintain a live graph (OSINTMapper): entities + links as you go; export JSON for reports.

## OPSEC
See `../opsec/REGLES-DOR-OPSEC.md` — dedicated UA/API keys, no desktop fingerprint reuse.
