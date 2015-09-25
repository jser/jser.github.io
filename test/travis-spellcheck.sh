#!/bin/bash
set -e
if [ -n "${TRAVIS_PULL_REQUEST}" ] && [ "${TRAVIS_PULL_REQUEST}" != "false" ]; then
  gem install --no-document checkstyle_filter-git saddler saddler-reporter-github

  npm run textlint && exit 0

  # 変更行のみを対象にする
  npm run textlint -- -f checkstyle \
   | checkstyle_filter-git diff develop \
   | saddler report \
      --require saddler/reporter/github \
      --reporter Saddler::Reporter::Github::PullRequestReviewComment
fi
exit 0