// LICENSE : MIT
"use strict";
import preact, {h, render} from 'preact';
import RelatedItemList from "./component/RelatedItemList"
import {getStat} from "./utils/get-stats";

function showRelated(URL, placeholder) {
    getStat().then(function(stat) {
        var jSerItem = stat.findItemWithURL(URL);
        var relatedItems = stat.findRelatedItems(jSerItem);
        return relatedItems.map(function(item) {
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
    }).then(function(postWithItems) {
        const app = <div class="RelatedItemBox">
            <RelatedItemList postWithItems={postWithItems}>Hello World!</RelatedItemList>
        </div>;
        render(app, placeholder);
    });
}
function removeRelated(box) {
    box.parentNode.removeChild(box);
}
getStat().then(function() {
    var siteNodeList = document.querySelectorAll(".site-genre ~ hr + h2 + p");
    var siteList = Array.prototype.slice.call(siteNodeList);
    siteList.forEach(function(item) {
        var URL = item.firstElementChild.href;
        var div = document.createElement("div");
        div.className = "RelatedItemAddition";
        var button = document.createElement("button");
        button.className = "RelatedItemAddition--button";
        button.textContent = "▼関連記事を表示";
        button.addEventListener("click", function(event) {
            event.preventDefault();
            button.textContent = "▲関連記事を非表示";
            var parentNode = item;
            var box = parentNode.querySelector(".RelatedItemBox");
            if (box) {
                removeRelated(box);
                button.textContent = "▼関連記事を表示";
                return;
            }
            var placeholder = document.createElement("div");
            parentNode.appendChild(placeholder);
            showRelated(URL, placeholder);
        });
        div.appendChild(button);
        item.appendChild(div);
    });
}).catch(function(error) {
    console.error(error, error.stack);
});