---
title: "2015-10-25 JS: ESLint입문, ECMAScript은 무엇인가?, rollup와 ES6 modules"
author: azu
translator: U-Yeong Ju
layout: post
date : 2015-10-25T20:20
category: JSer
tags:
    - ESLint
    - ECMAScript
    - Bundle
    - Browserify
    - rollup
---

JSer.info #250 - [ESLint v1.7.0](http://eslint.org/blog/2015/10/eslint-v1.7.0-released/ "ESLint v1.7.0")가 릴리즈됐습니다.
`.eslintrc`내에 `"extends": "./foo.js"`를 작성하여 자바스크립트 파일을 상속하여 옵션을 확장할 수 있도록 됐습니다.

또, [JavaScript - ESLint 첫걸음 - Qiita](http://qiita.com/mysticatea/items/f523dab04a25f617c87d "JavaScript - ESLint 첫걸음 - Qiita")(일본어)라는 글에서 ESLint의 사용 방법, 설정 방법, 에디터, ES6 관련 규칙 등 다양한 기능을 소개하고 있습니다.
ESLint를 처음 사용할 때 도움이 될 것 같습니다.

----

[ECMAScript의 사양 책정에 관한 컨닝페이퍼 | Web Scratch](http://efcl.info/2015/10/18/ecmascript-paper/ "ECMAScript의 사양 책정에 관한 컨닝페이퍼 | Web Scratch")(일본어)에서는 ECMAScript를 Q&A 형식으로 소개하고 있습니다.

ECMAScript에서 자주 언급되는 TC39 부터 시작해 ES6와 ES.next의 사양 책정 프로세스 그리고 어떤 사양이 제안되고 있는지 등에 관해 작성돼 있습니다.

평소 사양 책정에 관해 궁금했을 부분에 관해 어느정도 작성돼 있어 흥미있는 사람이 보면 재미있을 것 같습니다.

-----

[rollup.js](http://rollupjs.org/ "rollup.js")는 Browserify, RequireJS, Webpack과 같이 모듈을 하나로 결합하는 번들 도구 입니다.
기본적으로 ES6 modules로 작성한 파일을 결합하지만 [플러그인](https://github.com/rollup/rollup/pull/207 "plugin")으로 CommonJS 등도 대응하고 있는 것 같습니다.

[공식 사이트](http://rollupjs.org)에서 결합을 실제로 시험해볼 수 있습니다. 다른 번들 도구와 다르게 각각의 모듈을 랩핑한 함수 등이 없이 깨끗하게 결합됩니다.
또, 모듈 자체를 로드하고 있어도 사용하고 있지 않은 함수는 자동으로 제거하는 등 결과물의 최적화도 행하고 있습니다.

이 도구는 ES6 modules가 CommonJS의 'require' 처럼 동적으로 모듈을 로드되지 않고, [정적으로 의존 관계가 결정된다는 점](https://hacks.mozilla.org/2015/08/es6-in-depth-modules/)을 잘 활용하고 있습니다.

- [Cycles · rollup/rollup Wiki](https://github.com/rollup/rollup/wiki/Cycles "Cycles · rollup/rollup Wiki")
- [ES6 modules · rollup/rollup Wiki](https://github.com/rollup/rollup/wiki/ES6-modules "ES6 modules · rollup/rollup Wiki")
- [Bindings · rollup/rollup Wiki](https://github.com/rollup/rollup/wiki/Bindings "Bindings · rollup/rollup Wiki")
- [JavaScript - ES6 Modules 에서 export/import한 변수는 변할 수 있다 - Qiita](http://qiita.com/shuhei/items/f74e1f7478839e829b16 "JavaScript - ES6 Modules 에서 export/import한 변수는 변할 수 있다 - Qiita")(일본어)

다른 번들 도구와의 차이점에 관해 더 자세히 알고 싶다면 아래의 문서를 참고하세요.

- [Yet another module bundler · Issue #219 · rollup/rollup](https://github.com/rollup/rollup/issues/219 "Yet another module bundler · Issue #219 · rollup/rollup")

웹팩과 롤업을 사용해 번들한 소스를 [nolanlawson/rollup-comparison](https://github.com/nolanlawson/rollup-comparison "nolanlawson/rollup-comparison")에서 공개하고 있습니다(Webpack2에서도 [ES6 Modules를 기반으로 하고, 사용하고 있지 않은 함수 코드 삭제](https://github.com/webpack/webpack/pull/861#issuecomment-149997270)를 예정하고 있습니다)

이처럼 rollup.js는 ES6Modules에 최적화된 디자인입니다. ES6로 작성한 코드를 npm 등에 공개하는 규칙 등은 아직 다듬어지지 않은 상태입니다.

[The struggles of publishing a JavaScript library | Read the Tea Leaves](http://nolanlawson.com/2015/10/19/the-struggles-of-publishing-a-javascript-library/ "The struggles of publishing a JavaScript library | Read the Tea Leaves")에는 npm이나 Bower, jspm에 라이브러리를 어떻게 공개할 수 있는지 작성돼 있습니다.

문서를 보면 npm의 `"main"` 필드에 지정하는 엔트리포인트는 기본적으로 ES5 환경 용으로 빌드한 것 이어야 한다는 사실을 알 수 있습니다. 이처럼 공개한 라이브러리에 ES6의 코드를 어떻게 포함해야 하는지는 아무것도 정해져 있지 않습니다.

그 때문에 롤업은, ES6 Modules의 코드(라이브러리의 코드도 포함)를 참조하고자 `jsnext:main`이라는 필드에 ES6의 엔트리포인트를 지정하도록 하는 규약을 마련하고 있습니다.

[rollup.js](http://rollupjs.org/ "rollup.js")의해 공개된 패키지에 ES6 코드가 포함돼 있는 것도 장점으로 거론돼 왔기 때문에 향후 npm이나 bundle 도구에서 ES6 코드를 어떻게 다룰 것인지 이야기가 진행될지도 모르겠습니다.

추가로, 브라우저의 ES6 Modules를 불러오는 방식에 관한 사양은 [whatwg/loader](https://github.com/whatwg/loader "whatwg/loader")에서 논의되고 있습니다.

## 공지

이번 회는 250번째 회 이며, 내년 1월 16일은 JSer.info를 시작한지 꼬박 5년이 되는 날입니다.
따라서, 2016년 1월 16일(토)나 17일(일) 경에 [200회 기념 이벤트](http://jser.info/2014/11/02/jser200/ "JSer.info 200회 기념 이벤트를 개최했습니다 - JSer.info")(일본어)와 비슷한 이벤트를 계획하고 있습니다.

아래 이슈를 생성하고 있으니 의견이 있는 사람은 코멘트를 작성해 주시면 좋겠습니다.

- [JSer.info 5주년 이벤트 · Issue #54 · jser/jser.info](https://github.com/jser/jser.info/issues/54 "JSer.info 5주년 이벤트 · Issue #54 · jser/jser.info")(일본어)

----
<h1 class="site-genre">헤드라인</h1>

----

## ESLint v1.7.0 released - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2015/10/eslint-v1.7.0-released/](http://eslint.org/blog/2015/10/eslint-v1.7.0-released/ "ESLint v1.7.0 released - ESLint - Pluggable JavaScript linter")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint v1.7.0가 릴리즈됐습니다.
eslintrc의 `extends` 속성에 자바스크립트의 파일 경로를 작성하여 설정을 상속할 수 있도록 됐습니다.

----

## jsdom/Changelog.md at 7.0.0 · tmpvar/jsdom
[github.com/tmpvar/jsdom/blob/7.0.0/Changelog.md](https://github.com/tmpvar/jsdom/blob/7.0.0/Changelog.md "jsdom/Changelog.md at 7.0.0 · tmpvar/jsdom")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

jsdom 7.0.0이 릴리즈됐습니다.
Node.js 4.0 이상의 환경에서 동작합니다.
XMLHttpRequest가 재구현 됐고, `HTMLTemplateElement.prototype.content` 등이 추가 됐습니다.

----

## esprima/ChangeLog at 2.7.0 · jquery/esprima
[github.com/jquery/esprima/blob/2.7.0/ChangeLog](https://github.com/jquery/esprima/blob/2.7.0/ChangeLog "esprima/ChangeLog at 2.7.0 · jquery/esprima")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">AST</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

esprima 2.7.0이 릴리즈 됐습니다.
`esprima.tokenize`에 delegator 옵션이 추가됐습니다.

- [API: Token delegator · Issue #1332 · jquery/esprima](https://github.com/jquery/esprima/issues/1332 "API: Token delegator · Issue #1332 · jquery/esprima")

----
<h1 class="site-genre">아티클</h1>

----

## JavaScript - ESLint 첫걸음 - Qiita(일본어)
[qiita.com/mysticatea/items/f523dab04a25f617c87d](http://qiita.com/mysticatea/items/f523dab04a25f617c87d "JavaScript - ESLint 最初の一歩 - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

ESLint의 사용법과 설정 방법, 그리고 ES6와 관련된 규칙에 관해 설명합니다.

----

## ECMAScript의 사양 책정에 관한 컨닝페이퍼 | Web Scratch(일본어)
[efcl.info/2015/10/18/ecmascript-paper/](http://efcl.info/2015/10/18/ecmascript-paper/ "ECMAScriptの仕様策定に関するカンニングペーパー | Web Scratch")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">まとめ</span></p>

ECMAScript란 무엇인지 부터 ES2016의 사양 책정 프로세스, 진척률을 확인하는 방법, 컨트리뷰트 방식, Transpiler나 Polyfill의 영할 등 사양 책정에 관해 평소 궁금할 수 있는 부분이 정리돼 있습니다.

----

## ecmascript-6-destructuring-gotcha
[www.nczonline.net/blog/2015/10/ecmascript-6-destructuring-gotcha/](https://www.nczonline.net/blog/2015/10/ecmascript-6-destructuring-gotcha/ "ecmascript-6-destructuring-gotcha")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">spec</span></p>

`let {} = {};`가 ES6에서 유효한 것은 혼란을 일으킨다는 이야기, 현재 ECMAScript 사양의 이슈로써 수정할 것인지 의논되고 있습니다.

- [Destructuring declarations that bind nothing should probably be an early error · Issue #97 · tc39/ecma262](https://github.com/tc39/ecma262/issues/97 "Destructuring declarations that bind nothing should probably be an early error · Issue #97 · tc39/ecma262")

----

## EventEmitter in ES6
[www.datchley.name/es6-eventemitter/](http://www.datchley.name/es6-eventemitter/ "EventEmitter in ES6")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span></p>

ES6에서 간단하게 EvantEmitter나 Observer를 구현하면서 ES6의 기능을 배우게된 이야기가 작성돼 있습니다.

----

## The struggles of publishing a JavaScript library | Read the Tea Leaves
[nolanlawson.com/2015/10/19/the-struggles-of-publishing-a-javascript-library/](http://nolanlawson.com/2015/10/19/the-struggles-of-publishing-a-javascript-library/ "The struggles of publishing a JavaScript library | Read the Tea Leaves")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

bower, npm, jspm에 대응하여 라이브러리를 공개하는 방법과 설정에 관해서 이야기합니다.
Browserify, Webpack, rollup.js에서의 라이브러리 빌드에 관해서도 작성돼 있습니다.

- [nolanlawson/hello-javascript](https://github.com/nolanlawson/hello-javascript "nolanlawson/hello-javascript")

----

## Experimenting with Object.observe in JavaScript
[www.sitepoint.com/experimenting-object-observe-javascript-found-useful/](http://www.sitepoint.com/experimenting-object-observe-javascript-found-useful/ "Experimenting with Object.observe in JavaScript")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span></p>

ES.next에 제안돼 있는 `Object.observe`의 현재 상태에 관해 이야기 합니다.
브라우저의 지원 상황과 Polyfill에 관해 작성돼 있습니다.

----

## StrongLoop | Moving toward Express 5
[strongloop.com/strongblog/moving-toward-express-5/](https://strongloop.com/strongblog/moving-toward-express-5/ "StrongLoop | Moving toward Express 5")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">library</span></p>

Express 5α에서 변경된 사항이 정리돼 있습니다.

----

## TypeScript 1.6 시대의 .d.ts 관리 방법에 관한 의견을 서술하다 - Qiita(일본어)
[qiita.com/vvakame/items/72d22e33632178f7db24](http://qiita.com/vvakame/items/72d22e33632178f7db24 "TypeScript 1.6時代の.d.ts管理について意見を述べておく - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">정리</span></p>

npm 패키지와 TypeScript d.ts의 관리 방법에 관해 이야기합니다.

----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## The Accessibility Project
[a11yproject.com/](http://a11yproject.com/ "The Accessibility Project")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">접근성</span> <span class="jser-tag">정리</span></p>

웹 개발자를 위한 접근성에 관한 정보가 정리돼 있는 사이트입니다.

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## rollup.js
[rollupjs.org/](http://rollupjs.org/ "rollup.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">Tools</span></p>

ES6 modules를 Browserify 같은 도구 처럼 bundle하는 도구입니다. 
사용하지 않는 함수는 무시하며, 부차적인 랩핑 함수 없이 코드를 결합합니다. 
기본적으로 ES6만 지원하지만 플러그인으로 CommonJS도 대응할 수 있습니다.

----

## Rich-Harris/magic-string
[github.com/Rich-Harris/magic-string](https://github.com/Rich-Harris/magic-string "Rich-Harris/magic-string")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">AST</span> <span class="jser-tag">library</span></p>

SourceMap을 지원하는 코드 변환 라이브러리입니다. 
코드를 문자열로 다루며, 메서드를 이용해 문자열을 덮어쓰거나 추가, 삭제하여 코드를 변경합니다.
특정 코드의 변수명을 바꾸거나, 랩핑 함수를 추가할 수 있으며 SourceMap을 지원하므로 브라우저에서 무엇이 어떻게 바뀌었는지 확인도 가능합니다.

----

## .eslintrc editor
[pirosikick.github.io/eslintrc-editor/](https://pirosikick.github.io/eslintrc-editor/ ".eslintrc editor")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">설정</span></p>

ESLint의 설정을 GUI로 쉽게 체크하면서 작성할 수 있는 도구입니다.

- [브라우저에서 쉽게 체크하면서 ESLint의 설정 파일을 만드는 도구를 만들었다 - Qiita](http://qiita.com/pirosikick/items/64cb38752fa252911501 "브라우저에서 쉽게 체크하면서 ESLint의 설정 파일을 만드는 도구를 만들었다 - Qiita")(일본어)

----

## cotejp/webmidi
[github.com/cotejp/webmidi](https://github.com/cotejp/webmidi "cotejp/webmidi")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">web</span> <span class="jser-tag">sound</span> <span class="jser-tag">library</span></p>

Web MIDI API를 랩핑한 라이브러리입니다.

----

## dleitee/valid.js
[github.com/dleitee/valid.js](https://github.com/dleitee/valid.js "dleitee/valid.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

검증 규칙을 조합하여 String, Number, Date, Bool에 관한 검증 함수를 작성할 수 있도록 하는 라이브러리입니다.

----

## rodrigogs/kairos
[github.com/rodrigogs/kairos](https://github.com/rodrigogs/kairos "rodrigogs/kairos")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

시간을 더하거나 빼고, 두 시간이 같거나 다른지 비교할 수 있는 라이브러리입니다.

----
<h1 class="site-genre">도서</h1>

----

## SVG Text Layout - O&#x27;Reilly Media
[shop.oreilly.com/product/0636920043072.do](http://shop.oreilly.com/product/0636920043072.do "SVG Text Layout - O'Reilly Media")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">SVG</span> <span class="jser-tag">book</span></p>

SVG를 활용한 텍스트 레이아웃에 관한 도서입니다.

----
