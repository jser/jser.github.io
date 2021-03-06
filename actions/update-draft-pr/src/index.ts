import { rename } from "./rename"
// ${{ toJSON(github.event) }}
if (!process.env.PULL_REQUEST_EVENT) {
    throw new Error("process.env.PULL_REQUEST_EVENT is not defined");
}
const GITHUB_TOKEN = process.env.GITHUB_TOKEN!;
const PULL_REQUEST_EVENT = JSON.parse(process.env.PULL_REQUEST_EVENT!);
console.log("PULL_REQUEST_EVENT", PULL_REQUEST_EVENT);
(async () => {
    const authorAssociation = PULL_REQUEST_EVENT.pull_request.author_association;
    const canUserCommit = authorAssociation === "MEMBER" || authorAssociation === "OWNER";
    if (!canUserCommit) {
        return;
    }
    const PR_TITLE_PATTERN = /^(\d{4})-(\d{2})-(\d{2})のJS:(.*)/;
    const pullRequestTitle = PULL_REQUEST_EVENT.pull_request.title;
    const pullRequestBody = PULL_REQUEST_EVENT.pull_request.body;
    // No update if the pull request is new draft pr
    // Prevent to apply new slug logic to old articles
    if (!PR_TITLE_PATTERN.test(pullRequestTitle)) {
        return;
    }
    if (PULL_REQUEST_EVENT.action === "synchronize") {
        await rename({
            head: PULL_REQUEST_EVENT.pull_request.head,
            base: PULL_REQUEST_EVENT.pull_request.base,
            owner: "jser",
            repo: "jser.github.io",
            GITHUB_TOKEN: GITHUB_TOKEN
        })
    } else if (PULL_REQUEST_EVENT.action === "edited" || PULL_REQUEST_EVENT.action === "opened") {
        await rename({
            head: PULL_REQUEST_EVENT.pull_request.head,
            base: PULL_REQUEST_EVENT.pull_request.base,
            owner: "jser",
            repo: "jser.github.io",
            forceFitToTitle: pullRequestTitle,
            headline: pullRequestBody,
            GITHUB_TOKEN: GITHUB_TOKEN
        });
    }
})().catch(error => {
    console.error(error);
    process.exit(1);
})
