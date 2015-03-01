#!/bin/bash
set -e
if [ -n "${TRAVIS_PULL_REQUEST}" ] && [ "${TRAVIS_PULL_REQUEST}" != "false" ]; then
  gem --no-document checkstyle_filter-git install saddler saddler-reporter-github

  echo "gif diff"
  git diff --name-only origin/master \
   | grep -a '\.md$' || RETURN_CODE=$?

  case "$RETURN_CODE" in
    "" ) echo "found" ;;
    "1" )
      echo "not found"
      exit 0 ;;
    * )
      echo "Error"
      exit $RETURN_CODE ;;
  esac

  # 変更行のみを対象にする
  git diff --name-only origin/master \
   | grep -a '\.md$' \
   | xargs $(npm bin)/textlint --rulesdir test/rules -f checkstyle \
   | checkstyle_filter-git diff origin/master \
   | saddler report \
      --require saddler/reporter/github \
      --reporter Saddler::Reporter::Github::PullRequestReviewComment
fi
exit 0
