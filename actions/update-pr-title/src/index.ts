import { rename } from "./rename"
import { Octokit } from "@octokit/rest";
// ${{ toJSON(github.event) }}
if (!process.env.PULL_REQUEST_EVENT) {
    throw new Error("process.env.PULL_REQUEST_EVENT is not defined");
}
const GITHUB_TOKEN = process.env.GITHUB_TOKEN!;
const PULL_REQUEST_EVENT = JSON.parse(process.env.PULL_REQUEST_EVENT!);
console.log("PULL_REQUEST_EVENT", PULL_REQUEST_EVENT);
(async () => {
    const octokit = new Octokit({
        auth: GITHUB_TOKEN
    });
    await rename(octokit, {
        head: PULL_REQUEST_EVENT.head,
        base: PULL_REQUEST_EVENT.base,
        owner: "jser",
        repo: "jser.github.io"
    })
})();
