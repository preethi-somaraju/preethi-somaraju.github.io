# Custom Agent Rules & Guidelines

This file defines global rules for the Antigravity AI coding assistant working in this workspace.

---

## 1. Project Launch & Delivery Rule
Whenever a new portfolio project is created:
1.  **Unified Launch Email:** Send exactly ONE email to the user.
2.  **Email Content:** It must include the Technical Briefing (Why, What, How, Business Value, legit references) in the HTML body, detailed local file paths, and live GitHub URLs.
3.  **Inline Visualization (CID Method):** Embed any project charts/visuals using the native Content-ID (CID) attachment method (e.g., `<img src="cid:forecast_plot">`) rather than raw base64 HTML strings.
4.  **File Attachment:** Attach the generated Microsoft Word document (`.docx` version of the report) directly to the email.
5.  **No Split Mailings:** Do not send multiple separate emails for a single project launch.

---

## 2. GitHub & Privacy Rules
1.  **Strict PII Isolation:** Never add or commit personal documents, private resumes containing real phone numbers, or credentials configuration (`config.json`, `jobs.db`) to her public GitHub repositories.
2.  **Personal Documents Local-Only:** Keep personal workspace summaries and agent tutorials locally in her folder (`C:\Projects\Preethi\project-documents\`) and explicitly add them to `.gitignore` so they are never pushed to GitHub.
3.  **Meaningful Commit Messages:** Use conventional developer prefixes (`perf:`, `feat:`, `refactor:`, `docs:`, `style:`) with descriptions that accurately reflect the work actually done in each commit. Do not create commits on days with no real changes.
