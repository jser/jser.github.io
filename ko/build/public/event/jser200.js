/**
 * Created by azu on 2014/10/04.
 * LICENSE : MIT
 */
"use strict";
var $posterArea = jQuery("#js-jser200");
var $posterDate = $posterArea.find("> .article-meta-date");
var $posterTitle = $posterArea.find("> .article-meta-title");
var drawState = {
    title: true,
    date: true
};
var currentMetaObject = null;
function isNotEmpty(object) {
    return object != null;
}
var articleMetaList = JSerMetaJSON.map(function (object) {
    var match = object.title.match(/(\d{4})-(\d{2})-(\d{2})/);
    if (match == null) {
        return;
    }
    return object;
}).filter(isNotEmpty).slice(0, 200 - 1);

function getNextText() {
    return articleMetaList.pop();
}

function typing() {
    if (!drawState.title || !drawState.date) {
        return;
    }
    drawState.date = false;
    drawState.title = false;
    if (articleMetaList.length > 0) {
        currentMetaObject = getNextText();
        setTimeout(function () {
            typoText(currentMetaObject);
        }, 500);
    }
}

function typoText(object) {
    var match = object.title.match(/^(.*?):(.*?)$/);
    var date = match[1].trim();
    var title = match[2].trim();
    console.log(date);
    console.log(title);
    $posterTitle.find('.texts li:first').text(title);
    $posterTitle.textillate('start');
    $posterDate.find('.texts li:first').text(date);
    $posterDate.textillate('start');
}

if ($(window).width() > 500) {
    $posterArea.on("click", function () {
        window.open(currentMetaObject.url, "_blank");
    });
}
$posterTitle.textillate({
    // ループのオンオフ、falseの場合、outは発動しない
    loop: false,
    // テキストが置き換えられるまでの表示時間
    minDisplayTime: 0,
    // 遅延時間
    initialDelay: 0,
    // アニメーションが自動的にスタートするかどうか
    autoStart: false,
    // フェードインのエフェクトの詳細設定
    in: {
        // エフェクトの名前（animate.cssをご参照下さい）
        effect: 'fadeIn',
        // 遅延時間の指数
        delayScale: 1.5,
        // 文字ごとの遅延時間
        delay: 100,
        // trueにすることでアニメーションをすべての文字に同時に適用される
        sync: false,
        // trueにすることで文字を順番にではなく、ランダムに入ってくるようにする
        // (注：syncがtrueの場合は無効になる)
        shuffle: false
    },
    callback: function () {
        drawState.title = true;
        typing();
    }
});
$posterDate.textillate({
    // ループのオンオフ、falseの場合、outは発動しない
    loop: false,
    // テキストが置き換えられるまでの表示時間
    minDisplayTime: 0,
    // 遅延時間
    initialDelay: 0,
    // アニメーションが自動的にスタートするかどうか
    autoStart: false,
    // フェードインのエフェクトの詳細設定
    in: {
        // エフェクトの名前（animate.cssをご参照下さい）
        effect: 'fadeInDownBig',
        // 遅延時間の指数
        delayScale: 1.5,
        // 文字ごとの遅延時間
        delay: 100,
        // trueにすることでアニメーションをすべての文字に同時に適用される
        sync: false,
        // trueにすることで文字を順番にではなく、ランダムに入ってくるようにする
        // (注：syncがtrueの場合は無効になる)
        shuffle: false
    },
    // フェードアウトのエフェクトの詳細設定(同上)
    out: {
        effect: 'rollOut',
        delayScale: 1.5,
        delay: 50,
        sync: true,
        shuffle: true
    },
    callback: function () {
        drawState.date = true;
        typing();
    }
});

typing();
