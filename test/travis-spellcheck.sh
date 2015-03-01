#!/bin/bash
set -e
if [ -n "${TRAVIS_PULL_REQUEST}" ] && [ "${TRAVIS_PULL_REQUEST}" != "false" ]; then
  gem install saddler saddler-reporter-github

  echo "= gif diff"
  git diff --name-only origin/master \
   | grep -e '\.md$'

  echo "= checkstyle"
  git diff -z --name-only origin/master \
     | grep -e '\.md$' \
     | xargs $(npm bin)/textlint --rulesdir test/rules -f checkstyle

  git diff -z --name-only origin/master \
   | grep -e '\.md$' \
   | xargs $(npm bin)/textlint --rulesdir test/rules -f checkstyle \
   | saddler report \
      --require saddler/reporter/github \
      --reporter Saddler::Reporter::Github::PullRequestComment
fi
exit 0
