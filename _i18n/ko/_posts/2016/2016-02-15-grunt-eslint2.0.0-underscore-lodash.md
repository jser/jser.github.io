---
title: "2016-02-15 JS: Grunt 1.0.0 RC1, ESLint 2.0.0, Underscore/Lodash"
author: azu
translator: U-Yeong Ju
layout: post
date : 2016-02-15T20:07
category: JSer
tags:
    - JavaScript
    - Grunt
    - ESLint
    - underscore
    - lodash
    - Vanilla

---

JSer.info #266 - Grunt 1.0.0 RC1가 릴리즈됐습니다.

- [Grunt 1.0.0 rc1 released - Grunt: The JavaScript Task Runner](http://gruntjs.com/blog/2016-02-11-grunt-1.0.0-rc1-released)

Grunt는 개발이 멈춰있었지만, 근래 jQuery Foundation과 협력하여 다시 프로젝트가 시작됐습니다.

- [Grunt, Rebooted](http://blog.jquery.com/2015/11/19/grunt-rebooted/ "Grunt, Rebooted")

1.0.0 RC1에서는, [npm 3에서 동작이 변경](https://github.com/npm/npm/releases/tag/v3.0.0)된 `peerDependencies`를 대응하고, 의존하고 있는 모듈을 최신으로 업데이트 하는 등의 작업이 진행됐습니다.

지금까지는 명령줄에서 `grunt` 명령어를 사용하고자 할 때는 `grunt-cli` 설치가 필요했습니다.
1.0.0부터는 `grunt`의 dependencies에 `grunt-cli`가 포함되기 때문에 `npm install grunt` 하는 것 만으로 `grunt` 명령어를 사용할 수 있습니다.

이것은 npm run-script에서 명령어를 이용하는 상황을 고려한 구성으로 볼 수 있습니다.

```
$ npm info grunt@1.0.0-rc1 | grep grunt-cli -B 10
  engines: { node: '>=0.10.0' },
  scripts: { test: 'grunt test', 'test-tap': 'grunt test:tap' },
  main: 'lib/grunt',
  dependencies:
   { 'coffee-script': '~1.10.0',
     dateformat: '~1.0.12',
     eventemitter2: '~0.4.13',
     exit: '~0.1.1',
     'findup-sync': '~0.3.0',
     glob: '~6.0.4',
     'grunt-cli': '1.0.0-rc1',
```

전역적으로 `grunt` 명령어를 사용하고자 할때엔, 기존처럼 `npm install grunt-cli -g`으로 설치하여 사용할 수 있습니다.

또, [gruntjs/rfcs](https://github.com/gruntjs/rfcs "gruntjs/rfcs: RFCs for changes to Grunt")라는 저장소를 공개하여, RFC(Request for Comments)를 접수할 수 있는 시스템 구축도 진행하고 있습니다.

----

JavaScript Lint 도구인 [ESLint](http://eslint.org/ "ESLint") 2.0.0이 릴리즈됐습니다.

- [ESLint v2.0.0 released - ESLint - Pluggable JavaScript linter](http://eslint.org/blog/2016/02/eslint-v2.0.0-released)
- [ESLint v2.0.0 의 변경사항 정리 - Qiita](http://qiita.com/mysticatea/items/8bcecd821cca9e849078 "ESLint v2.0.0 의 변경사항 정리 - Qiita")(일본어)

도구를 설정하는 방법이나 플러그인 작성과 관련한 API가 변경되는 등 인터페이스가 바뀌는 부분이 있어 마이그레이션 가이드도 함께 공개하고 있습니다.

- [Migrating to v2.0.0](http://eslint.org/docs/user-guide/migrating-to-2.0.0 "Documentation - ESLint - Pluggable JavaScript linter")

----

[cht8687/You-Dont-Need-Lodash-Underscore: Lists of Javascript methods which you can use natively](https://github.com/cht8687/You-Dont-Need-Lodash-Underscore)에는 ECMAScript에서도 존재하는 Lodash/Underscore의 기능이 정리돼 있습니다.

또, 위 글의 답변하는 [stevemao/You-Dont-Know-About-Lodash-Underscore: In response to You-Dont-Need-Lodash-Underscore](https://github.com/stevemao/You-Dont-Know-About-Lodash-Underscore)라는 정리 글도 공개돼 있습니다.
Lodash/Underscore이 메서드는 단순하게 대체할 수 있는 기능 이외의 기능도 가지고 있다는 의견을 말하고 있습니다.

위 두 글과는 관계 없지만, Underscore와 Lodash를 합치는 프로젝트가 [Underdash](https://github.com/underdash/underdash "Underdash")에서 진행되고 있습니다.

- [Merge update. · Issue #14 · underdash/underdash](https://github.com/underdash/underdash/issues/14 "Merge update. · Issue #14 · underdash/underdash")

> So as to the merge I think it's already happened as Lodash v4.

라고 Lodash를 개발한 사람이 이야기하고 있습니다.

----
<h1 class="site-genre">헤드라인</h1>

----

## Release 2.1.0 - 2016.02.09 · zloirock/core-js
[github.com/zloirock/core-js/releases/tag/v2.1.0](https://github.com/zloirock/core-js/releases/tag/v2.1.0 "Release 2.1.0 - 2016.02.09 · zloirock/core-js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

core-js 2.1.0이 릴리즈됐습니다.
ES5 polyfill을 분리하고 `Reflect.enumerate`를 삭제했으며, Metadata Reflection API를 추가하는 등의 다양한 변경 사항이 있습니다.

- [decorators/metadata.md at master · jonathandturner/decorators](https://github.com/jonathandturner/decorators/blob/master/specs/metadata.md "decorators/metadata.md at master · jonathandturner/decorators")

----

## February 2016 Security Release Summary | Node.js
[nodejs.org/en/blog/vulnerability/february-2016-security-releases/](https://nodejs.org/en/blog/vulnerability/february-2016-security-releases/ "February 2016 Security Release Summary | Node.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">보안</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js의 보안이 업데이트 됐습니다.
0.1x, 4.x, 5.x의 업데이트가 각각 공개됐습니다.

----

## Grunt 1.0.0 rc1 released - Grunt: The JavaScript Task Runner
[gruntjs.com/blog/2016-02-11-grunt-1.0.0-rc1-released](http://gruntjs.com/blog/2016-02-11-grunt-1.0.0-rc1-released "Grunt 1.0.0 rc1 released - Grunt: The JavaScript Task Runner")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Grunt</span> <span class="jser-tag">ReleaseNote</span></p>

Grunt 1.0.0 RC1이 릴리즈됐습니다.
메이저 업데이트이며 `peerDependencies`에 관해 주의할 점이 작성돼 있고 `grant` 모듈에 CLI 포함, 의존 모듈 업데이트 등이 진행됐습니다.

----

## ESLint v2.0.0 released - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2016/02/eslint-v2.0.0-released](http://eslint.org/blog/2016/02/eslint-v2.0.0-released "ESLint v2.0.0 released - ESLint - Pluggable JavaScript linter")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint 2.0.0이 릴리즈 됐습니다.
코드를 검증하는 규칙 설정을 대화형으로 생성할 수 있는 `eslint --init` 명령어 추가, `eslint:recommended`의 업데이트, 기존 규칙이 동작하는 방식이 변경되거나 몇몇 옵션이 비권장되는 등의 여러가지 변경 사항이 있습니다. 

- [ESLint v2.0.0의 변경 사항 정리 - Qiita](http://qiita.com/mysticatea/items/8bcecd821cca9e849078 "ESLint v2.0.0의 변경 사항 정리 - Qiita")(일본어)
- [Documentation - ESLint - Pluggable JavaScript linter](http://eslint.org/docs/user-guide/migrating-to-2.0.0 "Documentation - ESLint - Pluggable JavaScript linter")

----

## StrongLoop | A New Day for Express!
[strongloop.com/strongblog/a-new-day-for-express/](https://strongloop.com/strongblog/a-new-day-for-express/ "StrongLoop | A New Day for Express!")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">community</span></p>

express가 Node.js Foundation의 Top-Level Project가 되고, strongloop(IBM)에서  https://github.com/expressjs 로 이전됐습니다.

- [TSC/Express.md at master · nodejs/TSC](https://github.com/nodejs/TSC/blob/master/Applications/Express.md "TSC/Express.md at master · nodejs/TSC")

----
<h1 class="site-genre">아티클</h1>

----

## Introducing the Accessible Modal Dialog
[dev.edenspiekermann.com/2016/02/11/introducing-accessible-modal-dialog/](http://dev.edenspiekermann.com/2016/02/11/introducing-accessible-modal-dialog/ "Introducing the Accessible Modal Dialog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">UI</span> <span class="jser-tag">접근성</span> <span class="jser-tag">library</span> <span class="jser-tag">WAI-ARIA</span></p>

Accessible한 모달 UI 라이브러리를 소개하는 글입니다.

----

## timaschew/postcss-compare-packs: compare most popular postcss packs like cssnext, rucksack and precss
[github.com/timaschew/postcss-compare-packs](https://github.com/timaschew/postcss-compare-packs "timaschew/postcss-compare-packs: compare most popular postcss packs like cssnext, rucksack and precss")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">PostCSS</span> <span class="jser-tag">정리</span></p>

cssnext, rucksack, precss 등, PostCSS Pack이 비교 정리돼 있습니다.

----

## ECMAScript, TC39 Meeting Notes를 읽는 방법과 수정하는 방법 | Web Scratch(일본어)
[efcl.info/2016/02/12/tc39-meeting-notes/](http://efcl.info/2016/02/12/tc39-meeting-notes/ "ECMAScript, TC39 Meeting Notesの読み方と修正方法 | Web Scratch")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span></p>

ECMA TC39 미팅 노트를 읽는 방법과 이 미팅 노트에는 어떤 내용들이 작성돼 있는지 소개하고 있습니다.

----

## cht8687/You-Dont-Need-Lodash-Underscore: Lists of Javascript methods which you can use natively
[github.com/cht8687/You-Dont-Need-Lodash-Underscore](https://github.com/cht8687/You-Dont-Need-Lodash-Underscore "cht8687/You-Dont-Need-Lodash-Underscore: Lists of Javascript methods which you can use natively")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span></p>

underscore/lodash의 메서드를 네이티브로 동일하게 표현할 수 있는 코드 작성 방법을 설명하고 있습니다.

- [stevemao/You-Dont-Know-About-Lodash-Underscore: In response to You-Dont-Need-Lodash-Underscore](https://github.com/stevemao/You-Dont-Know-About-Lodash-Underscore "stevemao/You-Dont-Know-About-Lodash-Underscore: In response to You-Dont-Need-Lodash-Underscore")

----

## An update on strong mode - Google 그룹스
[groups.google.com/forum/#!msg/strengthen-js/ojj3TDxbHpQ/5ENNAiUzEgAJ](https://groups.google.com/forum/#!msg/strengthen-js/ojj3TDxbHpQ/5ENNAiUzEgAJ "An update on strong mode - Google グループ")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">V8</span> <span class="jser-tag">JavaScript</span></p>

V8의 strong mode 구현 상태와 결과에 관해 작성돼 있습니다.
성능이 생각했던 것 보다 안좋았고, ES6 사양의 성능에 문제가 되는 요소(blockers)가 있으며 구현이 복잡(Implementation complexity)하다는 등의 이야기를 하고 있습니다.
따라서 다음 버전의 V8에서 strong mode 지원이 삭제될 예정입니다.

----

## web-perf/react-worker-dom: Experiments to see the advantages of using Web Workers to Render React Virtual DOM
[github.com/web-perf/react-worker-dom](https://github.com/web-perf/react-worker-dom "web-perf/react-worker-dom: Experiments to see the advantages of using Web Workers to Render React Virtual DOM")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">webworker</span> <span class="jser-tag">React</span></p>

WebWorker에서 React의 작업을 실행하는 데모가 공개돼 있습니다.

----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## AriaFallah/WebpackTutorial: A simple webpack tutorial
[github.com/AriaFallah/WebpackTutorial](https://github.com/AriaFallah/WebpackTutorial "AriaFallah/WebpackTutorial: A simple webpack tutorial")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">tutorial</span></p>

webpack의 튜토리얼입니다.
여러가지 사용 패턴과 설정법 그리고 왜 그렇게 작성하는지 상세히 작성돼 있습니다.

----

## React Newsletter
[reactjsnewsletter.com/](http://reactjsnewsletter.com/ "React Newsletter")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">mail</span></p>

React의 Weekly 메일 메거진입니다.

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## marten-de-vries/kneden: Transpile ES7 async/await to vanilla ES6 Promise chains: a Babel plugin
[github.com/marten-de-vries/kneden](https://github.com/marten-de-vries/kneden "marten-de-vries/kneden: Transpile ES7 async/await to vanilla ES6 Promise chains: a Babel plugin")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">plugin</span> <span class="jser-tag">JavaScript</span></p>

Promise를 사용하여 readable하게 async/await 코드를 변환해주는 Babel 플러그인입니다.

----

## ruyadorno/ntl: Npm Task List: Interactive cli menu to list/run npm tasks
[github.com/ruyadorno/ntl](https://github.com/ruyadorno/ntl "ruyadorno/ntl: Npm Task List: Interactive cli menu to list/run npm tasks")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">console</span> <span class="jser-tag">Tools</span></p>

npm run-script를 인터렉티브하게 선택하여 실행할 수 있도록 하는 도구입니다.

----
<h1 class="site-genre">도서</h1>

----

## JavaScript glossary… by Andrea Giammarchi [PDF/iPad/Kindle]
[leanpub.com/jsglossary](https://leanpub.com/jsglossary "JavaScript glossary… by Andrea Giammarchi \[PDF/iPad/Kindle\]")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span></p>

JavaScript 개발에서 사용하는 용어를 알기 쉽게 설명하는 것에 목적을 둔 도서입니다.

- [My new JavaScript book](https://www.webreflection.co.uk/blog/2016/02/08/jsglossary "My new JavaScript book")

----
