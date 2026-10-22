# Setup (delete after publishing)

1. Repo must be `Chathupachamika/Chathupachamika` (public).
2. Copy README.md, assets/, scripts/, .github/ to the repo root; delete the old assets/section-divider.svg; commit to the default branch.
3. Edit assets/project-card-1..3.svg with real project info (or remove the Featured Projects block).
4. Settings → Actions → General → Workflow permissions → Read and write.
5. Actions → "Generate Contribution Snake" → Run workflow. When green, branch `output` holds the SVGs.
6. Local check: `python3 scripts/check-readme.py`. "README checks" workflow runs it on push/PR.
7. Preview on github.com (desktop + phone, light and dark theme). Broken widgets = third-party; retry later or remove.
Troubleshooting: snake missing → check Actions log and permissions; animations frozen → some viewers show SVGs static, which is fine; stats cards blank → rate limit.
