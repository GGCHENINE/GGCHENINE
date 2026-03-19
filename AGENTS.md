# AGENTS.md
#
# This file gives Codex and collaborators consistent project context.
# Keep it short, concrete, and update it when conventions change.

## Project Overview
- Purpose: Learning Python for data analysis by reproducing the author's code from the book.
- Focus chapters: pandas, NumPy, matplotlib/seaborn.
- Support needed: Explain code execution logic and underlying principles on request.
- Primary languages: Python.

## Repo Structure
- `pandasch05.ipynb`: Active notebook.
- `python_for_risk_control_1/`: Exercises and code for risk control (part 1).
- `python_for_risk_control_2/`: Exercises and code for risk control (part 2).

## Conventions
- Prefer clear, explicit variable names over terse ones.
- Keep notebook outputs minimal; avoid printing large frames unless asked.
- When adding code, include a short comment only if the intent is non-obvious.

## Runtime / Environment
- Python version: 3.11.15
- Package manager: conda (Anaconda)
- Common commands:
  - Run notebook: `jupyter notebook`
  - Lint/format: (if any)

## Testing
- Tests: (if any)
- If no tests, describe how to manually verify changes.

## Review Checklist For Changes
- Notebook cells run top-to-bottom without errors.
- Outputs are concise and readable.
- No unnecessary new dependencies.

## Explanation Template (Use When Asked)
- Goal: What this cell/block is trying to achieve.
- Step-by-step: Describe the execution flow in plain language.
- Key APIs: Explain important functions/parameters and why they matter.
- Output: What the user should expect to see and how to interpret it.
- Pitfalls: Common mistakes or edge cases (if relevant).

## Tasks That Are In Scope
- Data wrangling, plotting, and explanation cells.
- Refactors for readability.
- Bug fixes in existing scripts/notebooks.

## Out of Scope / Avoid
- Installing global packages without asking.
- Large refactors across both `python_for_risk_control_*` directories unless requested.
