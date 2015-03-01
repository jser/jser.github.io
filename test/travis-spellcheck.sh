#!/bin/bash
set -v
if [ -n "${TRAVIS_PULL_REQUEST}" ] && [ "${TRAVIS_PULL_REQUEST}" != "false" ]; then
  gem install saddler saddler-reporter-github

  git diff -z --name-only origin/master \
   | xargs $(npm bin)/textlint --rulesdir test/rules -f checkstyle \
   | saddler report \
      --require saddler/reporter/github \
      --reporter Saddler::Reporter::Github::PullRequestComment
fi
exit 0
