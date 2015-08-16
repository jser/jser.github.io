// LICENSE : MIT
"use strict";
import element from 'virtual-element'
import { tree, render } from 'deku';
import RelatedItemList from "./component/RelatedItemList"
var JSerStat = require("jser-stat").JSerStat;
function getURL(URL) {
    return new Promise(function (resolve, reject) {
        var req = new XMLHttpRequest();
        req.open('GET', URL);
        req.onload = function () {
            if (req.status == 200) {
                resolve(req.response);
            } else {
                reject(Error(req.statusText));
            }
        };
        req.onerror = function () {
            reject(Error(req.statusText));
        };
        req.send();
    });
}
function getStat() {
    if (getStat._jSerStat) {
        return Promise.resolve(getStat._jSerStat);
    }
    return Promise.all([
        getURL("https://jsonp.afeld.me/?url=http://jser.info/posts.json"),
        getURL("https://jsonp.afeld.me/?url=http://jser.info/source-data/items.json")
    ]).then(function (results) {
        var posts = JSON.parse(results[0]).reverse();
        var items = JSON.parse(results[1]);
        var jSerStat = new JSerStat(items, posts);
        getStat._jSerStat = jSerStat;
        return jSerStat;
    });
}

function showRelated(URL, placeholder) {
    getStat().then(function (stat) {
        var jSerItem = stat.findItemWithURL(URL);
        var relatedItems = stat.findRelatedItems(jSerItem);
        return relatedItems.map(function (item) {
            var week = stat.findWeekWithItem(item);
            // 未来の記事候補の場合はまだ該当するweekはない
            if (week == null) {
                return null;
            }
            return {
                item: item,
                post: week.post
            };
        }).filter(object => object != null);// 空はfilter
    }).then(function (postWithItems) {
        var app = tree(
            <div class="RelatedItemBox">
                <RelatedItemList postWithItems={postWithItems}>Hello World!</RelatedItemList>
            </div>
        );
        render(app, placeholder);
    });
}
getStat().then(function () {
    var siteNodeList = document.querySelectorAll(".site-genre ~ hr + h2 + p");
    var siteList = Array.prototype.slice.call(siteNodeList);
    siteList.forEach(function (item) {
        var URL = item.firstElementChild.href;
        var button = document.createElement("button");
        button.textContent = "関連記事を表示";
        button.addEventListener("click", function (event) {
            var parentNode = event.target.parentNode;
            var box = parentNode.getElementsByClassName("RelatedItemBox");
            if(box.length > 0) {
                return;
            }
            var placeholder = document.createElement("div");
            parentNode.appendChild(placeholder);
            event.preventDefault();
            showRelated(URL, placeholder);
        });
        item.appendChild(button);
    });
}).catch(function (error) {
    console.error(error, error.stack);
});