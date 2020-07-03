---
title: "2020-06-30: Angular 10, TypeScript 4.0 Beta, Safari 14 변경 사항(Tracking Prevention)"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2020-06-29T15:29:41.875Z
category: JSer
tags:
- Angular
- TypeScript
- Safari

---

JSer.info #494 - Angular 10이 릴리스됐습니다.

- [Version 10 of Angular Now Available - Angular Blog](https://blog.angular.io/tagged/release-notes)
- [angular/CHANGELOG.md at master · angular/angular](https://github.com/angular/angular/compare/10.0.0-rc.6...10.0.0)
- [What’s new in Angular 10 | InfoWorld](https://www.infoworld.com/article/3537449/whats-new-in-angular-10.html)

의존하는 타입스크립트 관련 환경이 [TypeScript 3.9](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-9.html), [TSLib 2.0](https://github.com/microsoft/tslib/releases/tag/2.0.0), [TSLint 6](https://github.com/palantir/tslint/releases/tag/6.0.0)으로 갱신됐습니다.

Angular Material에 Date Range Picker가 추가됐습니다.
CommonJS를 사용하면 경고가 출력되며 ES Modules 사용을 권장합니다.
`ng new`에 `--strict` 옵션이 추가돼 TypeScript 등의 빌드 시 `strict` 플래그를 모아서 활성화할 수 있습니다.
또, 새로운 프로젝트의 기본 browserlists에서 오래된 브라우저를 제거하고 ES5 버전 빌드를 생성하지 않도록 변경됐습니다. 

----

TypeScript 4.0 Beta가 릴리스됐습니다.

- [Announcing TypeScript 4.0 Beta | TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-4-0-beta/)

Variadic Tuple Types, Labeled Tuple Elements 등이 추가됐고 생성자를 토대로 Class Property 타입을 추론할 수 있도록 변경됐습니다.
또, `catch` 정의 변수(식별자)의 타입으로 `unknown`을 지정할 수 있게 됐습니다.
이 외에 Stage 3의 logical assignment, `jsxFragmentFactory` 옵션, VSCode에서의 동작 속도를 향상 시키기 위한 Partial Editing Mode를 지원합니다.

----

Safari 14 Beta가 공개돼 있으며 이와 동일한 변경 내용을 포함하는 Safari Technology Preview가 공개됐습니다.

- [Release Notes for Safari Technology Preview 109 with Safari 14 Features | WebKit](https://webkit.org/blog/10875/release-notes-for-safari-technology-preview-109-with-safari-14-features/)
- [Safari 14 Beta Release Notes | Apple Developer Documentation](https://developer.apple.com/documentation/safari-release-notes/safari-14-beta-release-notes)

또, [Tracking Prevention in WebKit | WebKit](https://webkit.org/tracking-prevention/) 문서에는 Safari의 트래킹 방지에 관한 용어 해설과 구체적으로 어떠한 것을 블록하는지 작성돼 있습니다.
Fingerprinting이 가능할 수 있기 때문에 다음 API를 구현할 예정이 없다는 내용도 작성돼 있습니다.

- Web Bluetooth
- Web MIDI API
- Magnetometer API
- Web NFC API
- Device Memory API
- Network Information API
- Battery Status API
- Ambient Light Sensor
- HDCP Policy Check extension for EME
- Proximity Sensor
- WebHID
- Serial API
- Web USB
- Geolocation Sensor (background geolocation)
- User Idle Detection

Firefox도 이 API 중 몇가지에 대해서는 `harmful`(해로운) 입장을 보이고 있습니다.

- [Mozilla Specification Positions](https://mozilla.github.io/standards-positions/)

----

<h1 class="site-genre">헤드라인</h1>

----

## Version 10 of Angular Now Available - Angular Blog
[blog.angular.io/version-10-of-angular-now-available-78960babd41](https://blog.angular.io/version-10-of-angular-now-available-78960babd41 "Version 10 of Angular Now Available - Angular Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Angular</span> <span class="jser-tag">ReleaseNote</span></p>

Angular 10.0.0이 릴리스 됐습니다.
Angular Material에 Date Range Picker가 추가됐고, CommonJS를 사용하면 경고가 출력되도록 변경됐습니다. 또 `ng new`에 `--strict` 옵션 추가, TypeScript 3.9 갱신, 기본 browserslists 갱신이 이뤄졌습니다.


----

## Announcing TypeScript 4.0 Beta | TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-4-0-beta/](https://devblogs.microsoft.com/typescript/announcing-typescript-4-0-beta/ "Announcing TypeScript 4.0 Beta | TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 4.0 Beta가 릴리스됐습니다.
Variadic Tuple Types, Labeled Tuple Elements가 추가됐고 생성자를 토대로 Class Property를 추론할 수 있도록 변경됐습니다.
또, `catch` 절의 변수가 `any`에서 `unknown`으로 변경됐고 Stage 3의 logical assignment, `jsxFragmentFactory` 옵션을 지원하며 VSCode에서 Partial Editing Mode를 지원합니다.


----

## Release Notes for Safari Technology Preview 109 with Safari 14 Features | WebKit
[webkit.org/blog/10875/release-notes-for-safari-technology-preview-109-with-safari-14-features/](https://webkit.org/blog/10875/release-notes-for-safari-technology-preview-109-with-safari-14-features/ "Release Notes for Safari Technology Preview 109 with Safari 14 Features | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology 109이 릴리스 됐습니다.
Safari 14의 변경 내용이 포함돼 있습니다.
WebExtensions, Private report, Web Authentication, private class fields를 지원하며 Flash 지원이 종료됐습니다.

- [Safari 14 Beta Release Notes | Apple Developer Documentation](https://developer.apple.com/documentation/safari-release-notes/safari-14-beta-release-notes "Safari 14 Beta Release Notes | Apple Developer Documentation")

----

## hapi.js on Twitter: "Some un-hapi and joi-less news..." / Twitter
[twitter.com/hapijs/status/1275887984114413569](https://twitter.com/hapijs/status/1275887984114413569 "hapi.js on Twitter: \"Some un-hapi and joi-less news...\" / Twitter")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">server</span> <span class="jser-tag">library</span> <span class="jser-tag">news</span></p>

Node.js 프레임워크인 hapi의 코어 개발자가 hapi 개발 종료를 선언했습니다.

- [Slack | end | hapi hour](https://app.slack.com/client/T6ATU7T16/C015JQPME23/thread/C015JQPME23-1593110366.302100 "Slack | end | hapi hour")
- [hapi.dev - The simple, secure framework developers trust](https://hapi.dev/ "hapi.dev - The simple, secure framework developers trust")

----
<h1 class="site-genre">아티클</h1>

----

## Async Clipboard API | WebKit
[webkit.org/blog/10855/async-clipboard-api/](https://webkit.org/blog/10855/async-clipboard-api/ "Async Clipboard API | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">article</span></p>

Safari 13.1에서 지원하는 Async Clipboard API를 소개합니다.
클립보드 읽고 쓰기, Security / Privacy 제한에 대해 작성돼 있습니다.


----

## What's New In DevTools (Chrome 85)  |  Web  |  Google Developers
[developers.google.com/web/updates/2020/06/devtools](https://developers.google.com/web/updates/2020/06/devtools "What's New In DevTools (Chrome 85)  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">article</span></p>

Chrome 85 개발자 도구의 변경 사항이 정리돼 있습니다.
CSSOM로 추가한 CSS를 편집할 수 있도록 지원하며 Lighthouse 6로 갱신됐고, App shortcuts에 대한 경고 대응, `respondWith` 이벤트가 Timing 탭에 표시되도록 변경됐습니다.
퍼포먼스 패널에 자바스크립트 컴파일 캐시 정보를 표시합니다.


----

## Refactoring optional chaining into a large codebase: lessons learned – Lea Verou
[lea.verou.me/2020/06/refactoring-optional-chaining-into-a-large-codebase-lessons-learned/](https://lea.verou.me/2020/06/refactoring-optional-chaining-into-a-large-codebase-lessons-learned/ "Refactoring optional chaining into a large codebase: lessons learned – Lea Verou")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span> <span class="jser-tag">refacoring</span></p>

ES2020에 들어간 Optional Chaining을 사용한 리팩터링 기법을 소개합니다.
Optional Chaining으로 수정할 수 있거나 수정할 수 없는 패턴에 대해서 작성돼 있습니다.


----

## React 렌더링 완벽 가이드 - Qiita(일본어)
[qiita.com/hellokenta/items/6b795501a0a8921bb6b5](https://qiita.com/hellokenta/items/6b795501a0a8921bb6b5 "Reactのレンダリングに関する完全ガイド - Qiita")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">article</span> <span class="jser-tag">translate</span></p>

Complete Guide to React Rendering Behavior의 일본어 번역 문서입니다.
렌더링과 커밋의 단계, 렌더링 동작, 성능 측정, 리렌더링 타이밍에 대해서 이야기합니다.

- [Blogged Answers: A (Mostly) Complete Guide to React Rendering Behavior · Mark's Dev Blog](https://blog.isquaredsoftware.com/2020/05/blogged-answers-a-mostly-complete-guide-to-react-rendering-behavior/ "Blogged Answers: A (Mostly) Complete Guide to React Rendering Behavior · Mark&#x27;s Dev Blog")

----

## Tracking Prevention in WebKit | WebKit
[webkit.org/tracking-prevention/](https://webkit.org/tracking-prevention/ "Tracking Prevention in WebKit | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">privacy</span> <span class="jser-tag">security</span></p>

Safari의 트래킹 방지에 대해 정리돼 있습니다.
First-Party, Third-Party에서의 Cookie, Storage 제한, Fingerprinting에 사용될 수 있어 구현하지 않는 Web API, ITP 등에 대해서 이야기합니다.

- [Tracking Prevention Policy | WebKit](https://webkit.org/tracking-prevention-policy/ "Tracking Prevention Policy | WebKit")

----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## webpack 5 Miniseries - Tobias Koppers, webpack - YouTube
[www.youtube.com/watch?v&#x3D;3c-RFpaiUT8&amp;list&#x3D;PLyspMSh4XhLP-mqulUMcaqTbLo-ZJxSX5&amp;index&#x3D;34&amp;t&#x3D;0s](https://www.youtube.com/watch?v=3c-RFpaiUT8&list=PLyspMSh4XhLP-mqulUMcaqTbLo-ZJxSX5&index=34&t=0s "webpack 5 Miniseries - Tobias Koppers, webpack - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">video</span></p>

webpack 5의 변경에 대해서 소개하는 영상입니다.
자동 Node.js 용 polyfill 삭제, 생성 코드의 ES 버전 선택, 빌드 성능 및 캐시 개선, 최적화 및 로그 개선, Module Federation을 소개합니다.


----

## OpenJS World 2020 - YouTube
[www.youtube.com/playlist?list&#x3D;PLyspMSh4XhLP-mqulUMcaqTbLo-ZJxSX5](https://www.youtube.com/playlist?list=PLyspMSh4XhLP-mqulUMcaqTbLo-ZJxSX5 "OpenJS World 2020 - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">video</span> <span class="jser-tag">Conference</span></p>

OpenJS World 2020의 영상 목록입니다.

- [OpenJS World | Linux Foundation Events](https://events.linuxfoundation.org/openjs-world/ "OpenJS World | Linux Foundation Events")

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## ealush/vest: Vest - effortless validations
[github.com/ealush/vest](https://github.com/ealush/vest "ealush/vest: Vest - effortless validations")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

검증(밸리데이션) 라이브러리입니다.


----

## nastyox/Rando.js: The world's easiest, most powerful random function.
[github.com/nastyox/Rando.js](https://github.com/nastyox/Rando.js "nastyox/Rando.js: The world's easiest, most powerful random function.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

지정한 범위 내에서 랜덤한 값을 생성하는 라이브러리입니다.


----
<h1 class="site-genre">도서</h1>

----

## Talking TypeScript with the engineer who leads the team - Stack Overflow Blog
[stackoverflow.blog/2020/06/15/talking-typescript-with-ryan-cavanaugh/](https://stackoverflow.blog/2020/06/15/talking-typescript-with-ryan-cavanaugh/ "Talking TypeScript with the engineer who leads the team - Stack Overflow Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">Interview</span> <span class="jser-tag">Microsoft</span></p>

TypeScript 프로젝트 리더인 Ryan Cavanaugh의 인터뷰 글입니다.
만들게 된 계기, Angular 채용이 끼친 영향, 팀 구성, 에디터와 컴파일러 서비스, 자바스크립트 에코 시스템에 대해서 이야기합니다.


----
