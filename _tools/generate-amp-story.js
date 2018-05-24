#!/usr/bin/env node
"use strict";
const glob = require("glob-all");
const parseDetails = require("@jser/post-parser").parse;
const fs = require("fs");
const raw = require('nanohtml/raw');
const html = require('nanohtml');
const markdown = require('markdown-it')();
const sanitizeHtml = require('sanitize-html');
const path = require("path");
const makeDir = require('make-dir');
const del = require('del');
const jaDir = path.normalize(path.join(__dirname, "..", "_i18n/ja/"));
const ampDir = path.normalize(path.join(__dirname, "..", "ampstory"));
const mdFiles = glob.sync([
    `${jaDir}/**/*.md`,
    `!${jaDir}/_posts/events/*.md`,
    `!${jaDir}/_posts/support/*.md`,
    `!${jaDir}/_posts/tumblr/*.md`,
    `!${jaDir}/_posts/about/*.md`,
]);
const markdownToHtml = (markdownBody) => {
    const html = markdown.render(markdownBody);
    return sanitizeHtml(html, {
        allowedTags: ['b', 'i', 'em', 'strong', "code", "ul", "li"],
    });
};
const template = (result, originalURL) => {
    if (result.items.length === 0) {
        return;
    }
    const meta = result.meta;
    const [_, titleDate, keyword] = meta.title.match(/((?:\d{4})-(?:\d{2})-(?:\d{2})のJS):(.*)/);
    const coverPage = html`
<amp-story-page id="cover">
    <amp-story-grid-layer template="fill">
      <amp-img class="cover-img" src="/public/img/logo-vertical.png" width="900" height="1600">
      </amp-img>
    </amp-story-grid-layer>
    <amp-story-grid-layer template="vertical">
        <div class="title-wrapper">
            <h2 class="story-title">${titleDate}</h2>
        </div>
    </amp-story-grid-layer>
</amp-story-page>
`;
    const pages = result.items.map(item => {
        return html`
<amp-story-page id="${item.url}">
    <amp-story-grid-layer template="vertical">
        <div class="item">
            <amp-fit-text width="200"
                          height="120"
                          layout="responsive"
                          max-font-size="28"
                          class="item-title">${item.title}</amp-fit-text>
            <p class="item-contents">${raw(markdownToHtml(item.content))}</p>
        </div>
    </amp-story-grid-layer>
    <amp-story-cta-layer>
        <div class="cta-layer-inner">
            <a class="view-button" title="${item.title}" href="${item.url}" target="_blank" rel="noopener">ページを見に行く</a>
        </div>
    </amp-story-cta-layer>
</amp-story-page>
`
    });
    return html`---
layout: null
---
<!doctype html>
<html amp lang="ja">
<head>
    <meta charset="utf-8">
    <script async src="https://cdn.ampproject.org/v0.js"></script>
    <script async custom-element="amp-story"
            src="https://cdn.ampproject.org/v0/amp-story-0.1.js"></script>
    <script async custom-element="amp-fit-text" src="https://cdn.ampproject.org/v0/amp-fit-text-0.1.js"></script>
    <title>${meta.title} - JSer.info</title>
    <link rel="canonical" href="${originalURL}">
    <meta name="viewport" content="width=device-width,minimum-scale=1,initial-scale=1">
    <style amp-custom>
        amp-story {
            color: #000;
        }

        amp-story-page {
            background-color: #fff;
        }

        h1 {
            font-weight: bold;
            font-size: 2.875em;
            line-height: 1.174;
        }

        p {
            font-weight: normal;
            font-size: 1.1em;
            line-height: 1.5em;
            color: #000;
        }

        .item {
            
        }
       
        q {
            font-weight: 300;
            font-size: 1em;
            color: #333;
        }

        .cover-img {
            background: #2a8d9b;
        }
        
        .title-wrapper {
        }
        
        .story-title {
            font-family: "Al Bayan",游明朝,"Yu Mincho",YuMincho,"Hiragino Mincho ProN",HGS明朝E,メイリオ,Meiryo,serif;
            text-align: center;
            font-weight:100;
            font-size:48px;
            padding: 0.5em 0.2em;
            color: #fff;
        }
        
        .item-title {
        
        }

        .cta-layer-inner {
            display: flex;
            width: 100%;
            height: 100%;
        }

        .view-button {
            display: flex;
            justify-content: center;
            align-items: center;
            width: 100%;
            margin: 24px 32px;
            padding: 4px;
            color: #2a8d9b;
            border: 2px solid #2a8d9b;
        }
    </style>
    <style amp-boilerplate>body{-webkit-animation:-amp-start 8s steps(1,end) 0s 1 normal both;-moz-animation:-amp-start 8s steps(1,end) 0s 1 normal both;-ms-animation:-amp-start 8s steps(1,end) 0s 1 normal both;animation:-amp-start 8s steps(1,end) 0s 1 normal both}@-webkit-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@-moz-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@-ms-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@-o-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}</style><noscript><style amp-boilerplate>body{-webkit-animation:none;-moz-animation:none;-ms-animation:none;animation:none}</style></noscript>
</head>
<body>
<amp-story standalone bookend-config-src="/ampstory/backend.json" 
title="${meta.title}"
publisher="JSer.info"
publisher-logo-src="/public/img/jser-icon.png"
poster-portrait-src="/public/img/logo-3x4.png">
    ${raw(coverPage.toString())}
    ${raw(pages.map(page => page.toString()).join("\n"))}
</amp-story>
</body>
</html>
`.toString();
};
/* urlとカテゴリ(記事中の分類)を関連付けたJSONを作る
    [{
        category: "ヘッドライン",
        url: "http://example.com"
    }]
 */
del.sync([ampDir], {
    force: true
});
mdFiles.forEach(mdFilePath => {
    const content = fs.readFileSync(mdFilePath, "utf-8");
    const fileName = path.basename(mdFilePath, ".md");
    const [_, year, month, day, slug] = fileName.match(/(\d{4})-(\d{2})-(\d{2})-(.*)/);
    const pathname = `${year}/${month}/${day}/${slug}`;
    const originalURL = `https://jser.info/${year}/${month}/${day}/${slug}/`;
    const ampPath = path.join(ampDir, pathname) + ".html";
    try {
        const result = parseDetails(content, {
            filePath: mdFilePath
        });
        const dirname = path.dirname(ampPath);
        const html = template(result, originalURL);
        if (!html) {
            return;
        }
        makeDir.sync(dirname);
        fs.writeFileSync(ampPath, html, "utf-8");
    } catch (error) {
        console.log(mdFilePath);
        console.error(error);
    }
    const backend = {
        "share-providers": {
            "twitter": true,
            "tumblr": true,
            "email": true
        }
    };
    fs.writeFileSync(path.join(ampDir, "backend.json"), JSON.stringify(backend), "utf-8");
});
