# OSS² Engine — Architecture v0.1

## Implemented in bootstrap

- `oss2_engine.classifier`: deterministic local issue categorization.
- `oss2_engine.__main__`: offline CLI.
- `tests/`: unit tests.
- GitHub Actions: test and smoke-test workflow.

## Proposed, not implemented

1. Discovery adapter (GitHub read-only API).
2. Issue normalization and ranking with explicit evidence.
3. Human-approved patch preparation.
4. Local verification sandbox and evidence registry.
5. Human-reviewed PR handoff.
6. Optional KIANGANA 2.0 / KIF integration.

No autonomous submissions, no secret collection, no paid inference dependencies.
