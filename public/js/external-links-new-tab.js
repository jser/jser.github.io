function onReady() {
    return new Promise((resolve) => {
        const readyState = document.readyState;
        if (readyState === "interactive" || readyState === "complete") {
            resolve();
        } else {
            window.addEventListener("DOMContentLoaded", resolve);
        }
    });
}

// If it is an external link, set target="_blank"
function setExternalLinksOpenInNewTabs() {
    var externalLinkNodeList = document.querySelectorAll("a[href^='http']:not([href*='jser.info'])")
    var links = Array.prototype.slice.call(externalLinkNodeList);
    // add _blank and track
    links.forEach(function (link) {
        if (!link.target) {
            link.target = "_blank";
        }
    });
}

onReady().then(() => setExternalLinksOpenInNewTabs());
