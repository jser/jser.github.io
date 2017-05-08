require 'rake-jekyll'

Rake::Jekyll::GitDeployTask.new(:deploy) do |t|
    # master branch for machine
    t.deploy_branch = 'master'

    t.remote_url = -> {
        url = `git config remote.origin.url`.strip.gsub(/^git:/, 'https:')
        next url.gsub(%r{^https://([^/]+)/(.*)$}, 'git@\1:\2')
    }
    # Skip commit and push when building a pull request or env. variable
    # SKIP_COMMIT represents truthy.
    t.skip_commit = -> {
        ENV['TRAVIS_PULL_REQUEST'].to_i > 0 ||
        %w[yes y true 1].include?(ENV['SKIP_COMMIT'].to_s.downcase) ||
        !ENV['TRAVIS_BRANCH'].to_s.include?("develop")
    }
end