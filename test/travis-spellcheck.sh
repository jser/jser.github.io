#!/bin/bash
if [ -n "${TRAVIS_PULL_REQUEST}" ] && [ "${TRAVIS_PULL_REQUEST}" != "false" ]; then
  gem install --no-document checkstyle_filter-git saddler saddler-reporter-github

  echo "before: npm run textlint checkstyle"
  npm run textlint --silent
  git diff --name-only --diff-filter=ACMR origin/develop | grep -a '_i18n/ja/.*.md$' | xargs $(npm bin)/textlint --rulesdir test/rules -f checkstyle | checkstyle_filter-git diff origin/develop
  echo "after: npm run textlint checkstyle"
  # 変更行のみを対象にする
  npm run textlint --silent -- -f checkstyle \
  | checkstyle_filter-git diff origin/develop \
  | saddler report \
      --require saddler/reporter/github \
      --reporter Saddler::Reporter::Github::PullRequestReviewComment
fi
exit 0