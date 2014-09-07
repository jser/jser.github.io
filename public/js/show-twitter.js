/**
 * Created by azu on 2014/09/07.
 * LICENSE : MIT
 */
"use strict";
(function () {
    var siteNodeList = document.querySelectorAll(".site-genre ~ hr + h2 + p");
    var siteList = Array.prototype.slice.call(siteNodeList);
    var divList = siteList.map(function (pTag) {
        var aTag = pTag.firstElementChild;
        var siteTitle = aTag.title,
            siteURL = aTag.href;
        var instA = document.createElement("a");
        instA.href = "http://twitter.com/share";
        instA.dataset.text = siteTitle;
        instA.dataset.url = siteURL;
        instA.dataset.counturl = siteURL;
        instA.dataset.via = "jser_info";
        instA.dataset.dnt = "true";
        instA.className = "socialite twitter-share";
        instA.appendChild(document.createTextNode("Share on Twitter"));
        var div = document.createElement("div");
        div.className = "site-twitter";
        div.appendChild(instA);
        pTag.previousElementSibling.appendChild(div);
        return div;
    });
    // ヘッダとフッタのは自動で読み込む
    Socialite.load(document, Socialite.getElements(document, 'socialite-auto-loading'));
    // まずは自動では読みこないようにする + 隠す
    Socialite.process(document, Socialite.getElements(document, 'socialite'));

    var screenHeight = window.parent.screen.height;
    // 画面に表示されたら読み込みを開始する
    function updateTwitterButton() {
        // 現在の位置
        var wScrollTop = document.documentElement.scrollTop || document.body.scrollTop;
        wScrollTop += screenHeight;
        var overLappedElement = divList.filter(function (div) {
            var originY = div.offsetTop;
            return wScrollTop >= (originY - 1000);
        });
        overLappedElement.forEach(function (div) {
            var index = divList.indexOf(div);
            Socialite.load(div);
            // 処理済みは対象から外していく
            divList.splice(index, 1);
        });
        // 全てが処理済みになったらハンドラを解除する
        if (divList.length === 0) {
            window.removeEventListener("scroll", onScroll);
        }
    }

    function onScroll() {
        requestAnimationFrame && requestAnimationFrame(updateTwitterButton);
    }

    window.addEventListener("scroll", onScroll);


})();