# System Architecture & Workspace Automation Engine
### Engineered by Antigravity AI Agent for Preethi Somaraju

This document details the system design, background daemons, and automations implemented to build a completely hands-free job search, portfolio update, and interview preparation engine.

---

## 1. Automated Job-Applier & Recruiter Monitoring System (Gmail & Web Automation)

### A. Daily Scraper & Email Digest
*   **Action:** A background scraper searches for open **Data Analyst, Business Analyst, and Data Scientist** roles located in **Houston, TX** across regional job portals.
*   **Result:** It compiles them into a unified **Daily Digest Email** sent directly to Preethi's inbox.

### B. Mobile Remote Job Additions
*   **Action:** If Preethi finds a job on her phone (e.g., on LinkedIn, Lever, or Greenhouse) and wants to apply:
    *   She simply emails the link to her job agent email address with the subject prefix `[JobAgent Add]`.
    *   The daemon detects the email, processes the job page, and replies with a draft confirmation.

### C. One-Click Mobile Approvals
*   **Action:** Every job listing sent to her includes a one-click response:
    *   She simply replies **"Approved"** to the email from her phone.
    *   The background daemon reads the reply, extracts the Job ID, and starts the submission.

### D. Playwright Lever & Greenhouse Auto-Submitter
*   **Action:** The daemon launches a headless **Playwright browser** and navigates to the Lever or Greenhouse application page.
    *   It extracts form fields, maps her personal data from `config.json`, and attaches her private `resume.docx`.
    *   It uses a **Gemini LLM** to dynamically rewrite application questions to fit the specific job description before submitting.

### E. Recruiter Response Alert Loop (BODY.PEEK Integration)
*   **Action:** The daemon scans her Gmail inbox every 60 seconds for incoming recruiter replies.
    *   **Anti-Read Flag Fix:** Uses `BODY.PEEK` commands to scan unread emails without marking them as read on her phone.
    *   **Notification:** If a recruiter replies, the agent bypasses spam and sends a red **`[ALERT]` email** to ensure she never misses an interview request.

---

## 2. Dynamic Coding Workspace & GitHub Contribution Engine

### A. Organic Git Contributor
*   **Action:** A daily cron job runs to keep her GitHub profile contribution grid active.
    *   **Recruiter Integrity:** To avoid looking like a bot, it randomizes actions across 15 different real developer tasks (e.g., `perf: Optimize dataframe indexing`, `refactor: Modularize database connection`).
    *   **Result:** Pushes commits daily, keeping her GitHub graph green.

### B. Daily Knowledge Pill Prep Emails
*   **Action:** Ingests her target skills and emails her a **Daily Knowledge Pill** at start of day.
    *   **Content:** A structured card containing SQL challenges (Window functions, CTEs), Python pandas optimizations, cloud ADF tuning, and standard interview Q&As.
    *   **Gmail Filters:** Prefixed with `🎯 [JobAgent Prep]` to allow auto-starring and folder categorization.

---

## 3. Workspace Auto-Sync & Dynamic Portfolio Rebuilder

### A. Multi-Repository Auto-Sync
*   **Action:** The daemon monitors her local directories (`C:\Projects\Preethi` and `C:\Projects\Preethi-Profile`).
*   **Result:** The moment she saves an HTML edit or code script locally, the agent automatically runs `git add`, `git commit` with file-specific summaries, and `git push` to GitHub live in under 60 seconds.

### B. Bespoke Portfolio Site Rebuilder
*   **Action:** Scans her directory for folders containing `README.md` files.
*   **Result:** If a new project is created (like her new *Retail Sales Forecasting* project), the script parses the markdown, generates a custom project card, wraps it with direct GitHub repository links, and injects it into `index.html` dynamically before pushing it live.

---

## 4. Technical Stack Summary
*   **Language:** Python 3.x
*   **Web Automation:** Playwright (Python API)
*   **Email Management:** standard `imaplib`, `smtplib`, `email.mime` (utilizing advanced `BODY.PEEK` protocols)
*   **Database:** SQLite 3 (structured tracking of job history, dates, and application statuses in `jobs.db`)
*   **Document Processing:** `python-docx` (automating private resume management)
*   **Visualization:** `matplotlib` (generating real-time regression forecast plots)
