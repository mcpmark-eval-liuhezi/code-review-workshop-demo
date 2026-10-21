# Contributing to the Workshop Demo

This repository is a demo for our hands-on GitHub review-workflow workshop.

## How the review process works

1. **Create a branch.** All changes are made on a working branch off `main`, never committed directly to `main`.
2. **Open a pull request.** When your change is ready, open a PR from your working branch into `main` and describe what changed and why.
3. **Wait for CI.** The CI workflow runs a `build` job and a `lint` job on every push and pull request. Let it finish before asking for review.
4. **Draft a review.** Reviewers click "Start a review", add line comments anchored to specific lines of the diff, and keep the review pending while they read the rest of the change.
5. **Submit the review.** Submit it as a comment, approve, or request changes. Questions and observations are usually submitted as comments; requests for concrete edits are "request changes".
6. **Discuss and iterate.** The author replies to comments, pushes fixes, and re-requests review until everyone is happy.
7. **Merge.** Only merge once CI is green and the review conversation is resolved.

## Tips for attendees

- Anchor every comment to a specific line — it keeps the discussion grounded in the code.
- Ask questions before requesting changes; many findings turn out to be misunderstandings.
- Review the "Files changed" tab, not just the diff preview on the conversation tab.
