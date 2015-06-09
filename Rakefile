require 'rake-jekyll'

Rake::Jekyll::GitDeployTask.new(:deploy) do |t|
    # Skip commit and push when building a pull request or env. variable
    # SKIP_COMMIT represents truthy.
    t.skip_commit = -> {
        ENV['TRAVIS_PULL_REQUEST'].to_i > 0
    }
end
