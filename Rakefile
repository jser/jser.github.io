require 'rake-jekyll'

Rake::Jekyll::GitDeployTask.new(:deploy) do |t|
    # master branch for machine
    t.deploy_branch = 'master'

    # Skip commit and push when building a pull request or env. variable
    # SKIP_COMMIT represents truthy.
    t.skip_commit = -> {
        false
    }
end