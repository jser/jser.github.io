// LICENSE : MIT
"use strict";
import preact, { h, render } from 'preact';
import RelatedItemBox from "./component/RelatedItemBox";
import FeedbackToTwitter from "./container/FeedbackToTwitter"
import { getStat } from "./utils/get-stats";
import { getCurrentURL } from "./utils/get-current-url";
import { CommentCount } from 'disqus-react';

function addRelatedItemPlaceholder() {
    var siteNodeList = document.querySelectorAll(".site-genre ~ hr + h2 + p");
    var siteList = Array.prototype.slice.call(siteNodeList);
    siteList.forEach(function(item) {
        var parentNode = item;
        var URL = parentNode.firstElementChild.href;
        var placeholder = document.createElement("div");
        parentNode.appendChild(placeholder);
        render(<RelatedItemBox URL={URL}/>, placeholder);
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
    addFeedbackForm(stat);
}).catch(function(error) {
    console.error(error, error.stack);
});
