# VibeCheck SARIF test

> **Intentionally vulnerable. Do not deploy or copy this code.**

A tiny fixture app with known security problems: open Firestore rules, SQL injection, `eval`, CORS `*`, endpoints with no login check and Flask debug mode. It exists to check that [VibeCheck](https://github.com/Meetrao/vibe-coded-app-fixer)'s SARIF output shows up correctly in GitHub code scanning (**Security → Code scanning**).

It contains no secrets, not even fake ones.

The workflow in `.github/workflows/vibecheck.yml` checks out VibeCheck (a private repo) with the `VIBECHECK_DEPLOY_KEY` secret, which is a read-only deploy key for that one repo. It then runs the action and uploads `vibecheck.sarif`.
