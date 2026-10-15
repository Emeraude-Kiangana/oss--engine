# OSS² Engine

**Open Source des Open Source** — evidence-first, human-reviewed open-source contribution tooling. 🇨🇩

Status: **experimental bootstrap**. No autonomous changes to third-party repositories.

## Principles

- TOOL-FIRST · API-FIRST · EVIDENCE-FIRST · COST-GUARDED
- Human approval before publishing any contribution.
- Reproducible tests and auditable evidence.
- Python standard library first; no paid services required for local tests.

## Quickstart

```bash
python -m unittest discover -s tests -v
python -m oss2_engine --help
python -m oss2_engine classify --title 'Fix typo in README' --labels documentation good-first-issue
```

## Scope v0.1

A deterministic, offline issue classifier. GitHub discovery, AI patch generation, PR automation and KIANGANA 2.0 integration are **not implemented**.

See [architecture](docs/ARCHITECTURE.md) and [evidence policy](docs/EVIDENCE.md).
