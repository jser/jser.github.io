#!/bin/bash
set -e
if [ -n "${TRAVIS_PULL_REQUEST}" ] && [ "${TRAVIS_PULL_REQUEST}" != "false" ]; then
  gem install saddler saddler-reporter-github

  git diff --name-only origin/master \
   | grep -e '\.md$'

  git diff -z --name-only origin/master \
   | grep -e '\.md$' \
   | xargs $(npm bin)/textlint --rulesdir test/rules -f checkstyle \
   | saddler report \
      --require saddler/reporter/github \
      --reporter Saddler::Reporter::Github::PullRequestReviewComment
fi
exit 0
