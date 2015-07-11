---
title: "JSHint: A Formal Commitment to New Language Features"
author: azu
layout: post
date : 2015-07-11T14:53
category: JavaScript
tags:
    - JSHint
    - ECMAScript
    - ES.next
    - community

---

[JSHint](http://jshint.com/ "JSHint, a JavaScript Code Quality Tool")のブログに投稿された

[A Formal Commitment to New Language Features](http://jshint.com/blog/new-lang-features/ "A Formal Commitment to New Language Features")

という記事の紹介です。


BabelなどによってES nextの機能を試せるようになっていますが、
JSHintがそれらの新しすぎる構文をサポートするのが難しい理由について。

理由の一つとしてメンテナンスが難しすぎるという問題があること。

もう一つの大きな理由としては、JSHintは常にコミュニティ駆動型のツールであるため、
エコシステムの破壊するかもしれないまだ不安定なものをファーストクラスとしては採用しない事が挙げられています。

JSHintがJSLintをforkして作られた経緯については、以下に作者のブログで書かれています。

- [Why I forked JSLint to JSHint — Medium](https://medium.com/@valueof/why-i-forked-jslint-to-jshint-73a72fd3612 "Why I forked JSLint to JSHint — Medium")
- [JSLint から JSHint をフォークした理由(翻訳) | 黒くないすべてのものはカラスではない](http://blog.node.ws/?p=1379 "JSLint から JSHint をフォークした理由(翻訳) | 黒くないすべてのものはカラスではない")

ES nextを一概に取り入れないという意味ではなく、その機能のプロポーサルがStage 2以上のものは、全く早すぎるというわけではないためexperimentalフラグで取り入れてとしています。

Note: Stage 2はECMAScriptのプロポーサルの段階を示すもので、
プロポーサルのドラフトができてブラウザがフラグ付きで実験的なサポートをしたりする段階です。

- [TC39 Process - Google ドキュメント](https://docs.google.com/document/d/1QbEE0BsO4lvl7NFTn5WXWeiEIBfaVUF7Dk0hpPpPDzU/edit?pli=1 "TC39 Process - Google ドキュメント")

JSHint 3ではこの方針に則り

- `esnext`というオプションは廃止
- `moz`オプションについてはそのまま
- ES6については`esversion: 6`オプションでサポート
- ES7についてはちゃんと標準化が完了してからサポート
- stage 2以上のプロポーサルについては`experimental`オプションでサポート

という形にしていくようです。

