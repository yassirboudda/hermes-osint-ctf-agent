---
name: captcha-mail-browser
description: >-
  Captcha solvers (CapSolver, 2Captcha), dedicated CTF mailbox, Browser-Use and Apify hooks.
---

# Captcha · Mail · Browser automation

## Captcha
- CapSolver → `CAPSOLVER_API_KEY`
- 2Captcha → `TWOCAPTCHA_API_KEY`
- AntiCaptcha → `ANTICAPTCHA_API_KEY`

Use only when a **legitimate** OSINT flow requires account creation / form access allowed by rules.

## Mail
Dedicated CTF inbox via IMAP or Gmail OAuth refresh token (`GMAIL_REFRESH_TOKEN=****`).
Never reuse a personal primary mailbox.

## Browser
- Browser-Use pool: `BROWSER_USE_API_KEY`
- Apify actors: `APIFY_TOKEN`

Always set `CTF_UA`. Soft crawl only. No parallel hammering.
