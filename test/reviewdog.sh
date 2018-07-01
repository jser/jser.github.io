#!/usr/bin/env bash

git diff --name-only --diff-filter=ACMR origin/develop \
| grep -a '_i18n/ja/.*.md$' \
| xargs $(npm bin)/textlint -f checkstyle \
| reviewdog -f=checkstyle -name="textlint" -reporter=github-pr-check
