// MIT © 2017 azu
"use strict";
const JSerStat = require("@jser/stat").JSerStat;
const { fetchItems, fetchPosts } = require("@jser/data-fetcher");

let _jSerStat;

export function getStat() {
    // APIで取ってくる方式
    if (_jSerStat) {
        return Promise.resolve(_jSerStat);
    }
    return Promise.all([fetchItems(), fetchPosts()]).then(([items, posts]) => {
        var jSerStat = new JSerStat(items, posts);
        _jSerStat = jSerStat;
        return jSerStat;
    });
}
