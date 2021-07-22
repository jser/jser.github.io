// LICENSE : MIT
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

function detectNotFound(URL, callback) {
    var request = new XMLHttpRequest();
    request.open("HEAD", URL);
    request.onload = function () {
        if (request.status >= 200 && request.status < 300) {
            callback(null);
        } else {
            callback(new Error("status code is " + request.status));
        }
    };
    request.onerror = function () {
        callback(new Error("status code is " + request.status));
    };
    request.send();
}

// if altHref is not 404, then replace href to altHref
function updateAltLink() {
    var altHrefTags = document.querySelectorAll('a[data-alt-href]');
    var links = Array.prototype.slice.call(altHrefTags);
    links.forEach(function (link) {
        var altHref = link.dataset.altHref;
        detectNotFound(altHref, function (error) {
            if (error) {
                return;
            }
            // if altHref is not 404, then replace href to altHref
            link.href = altHref;
        });
    });
}

onReady().then(() => updateAltLink());
