---
title: "2015-02-16のJS: Babel(6to5)、BrowserSync 2.0"
author: azu
layout: post
date : 2015-02-15T22:46
category: JSer
tags:
    - Tools

---
JSer.info #215 - ES6+のコードをES5に変換するツールである [6to5](https://6to5.org/) が [Babel](https://babeljs.io/ "Babel · The transpiler for writing next generation JavaScript") にリネームされてリリースされました。

- [Not Born to Die · Babel](http://babeljs.io/blog/2015/02/15/not-born-to-die/ "Not Born to Die · Babel")

また、BabelはAcornをベースにしたパーサーを利用していて、そのASTの元になっている[SpiderMonkey parser](https://developer.mozilla.org/en-US/docs/Mozilla/Projects/SpiderMonkey/Parser_API "SpiderMonkey parser")のASTはES6以降についての仕様が曖昧になっていてその部分を各パーサがそれぞれ実装していました。

最近になってjQuery FoundationにEsprimaが移管されたのが契機となって、Esprima、Acorn、Mozilla、Shift ASTの人たちが中心となってASTの仕様を定義していく[ESTree](https://github.com/estree/estree "ESTree")が始まりました。(基本的には現行のASTと互換性を重視しています)

Babelとしても[@sebmck](https://github.com/sebmck "sebmck")氏が[ESTree](https://github.com/estree/estree "ESTree")でのASTの策定に関わっていくようです。

-----


[BrowserSync 2.0 - JH](http://www.wearejh.com/news/browsersync-2-0/ "BrowserSync 2.0 - JH")
