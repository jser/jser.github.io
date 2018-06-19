// LICENSE : MIT
"use strict";
import preact, {h, render} from 'preact';
import RelatedItemList from "./component/RelatedItemList"
import FeedbackToTwitter from "./container/FeedbackToTwitter"
import {getStat} from "./utils/get-stats";
import {getCurrentURL} from "./utils/get-current-url";

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
function addRelatedItemPlaceholder() {
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
}
/**
 * 気になる記事をTwitterに投稿するボタン
 * @param {JSerStat} stat
 */
function addFeedbackForm(stat) {
    const currentURL = getCurrentURL();
    const week = stat.findJSerWeekWithURL(currentURL);
    if (!week) {
        return;
    }
    const articleBody = document.querySelector(".post-content");
    const placeholder = document.createElement("div");
    placeholder.className = "FeedbackForm";
    articleBody.appendChild(placeholder);
    const app = <FeedbackToTwitter week={week}/>;
    render(app, placeholder);
}

getStat().then(function(stat) {
    addRelatedItemPlaceholder();
    // addFeedbackForm(stat);
}).catch(function(error) {
    console.error(error, error.stack);
});
