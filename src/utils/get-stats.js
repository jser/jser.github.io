// MIT © 2017 azu
"use strict";
const JSerStat = require("jser-stat").JSerStat;
const ItemData = require("jser-stat/data/items");
const PostData = require("jser-stat/data/posts");
function fetchURL(URL) {
    return new Promise(function(resolve, reject) {
        var req = new XMLHttpRequest();
        req.open('GET', URL);
        req.onload = function() {
            if (req.status == 200) {
                resolve(req.response);
            } else {
                reject(Error(req.statusText));
            }
        };
        req.onerror = function() {
            reject(Error(req.statusText));
        };
        req.send();
    });
}
export function getStat() {
    return Promise.resolve(new JSerStat(ItemData, PostData));
    // APIで取ってくる方式
    if (getStat._jSerStat) {
        return Promise.resolve(getStat._jSerStat);
    }
    return Promise.all([
        fetchURL("https://jser.info/posts.json"),
        fetchURL("https://jser.info/source-data/items.json")
    ]).then(function(results) {
        var posts = JSON.parse(results[0]).reverse();
        var items = JSON.parse(results[1]);
        var jSerStat = new JSerStat(items, posts);
        getStat._jSerStat = jSerStat;
        return jSerStat;
    });
}
