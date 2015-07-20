---
title: "JSHint: A Formal Commitment to New Language Features"
author: azu
translator: U-Yeong Ju
layout: post
date : 2015-07-11T14:53
category: JavaScript
tags:
    - JSHint
    - ECMAScript
    - ES.next
    - community

---


## A Formal Commitment to New Language Features

[JSHint](http://jshint.com/ "JSHint, a JavaScript Code Quality Tool") 블로그에 올라온 [A Formal Commitment to New Language Features](http://jshint.com/blog/new-lang-features/ "A Formal Commitment to New Language Features") 글을 소개하고자 합니다.

Babel와 같은 Transpiler를 이용해 ES.next의 기능을 사용해 볼 수 있습니다만, 
JSHint가 새로운 구문을 지원하기 어려운 이유에 대해 작성돼 있습니다.

그 이유 중 첫 번째로 소개한 것은 메인터넌스가 어렵다는 문제입니다.

또 하나의 대표적인 이유로는 JSHint는 커뮤니티 중심적 도구(community-driven tool) 이기 때문에,
비표준 코드를 지원하게 되면 생태계에 장기적인 영향을 미치게 됩니다. 따라서 아직 불완전한 기능 지원을 우선순위 높게 채용하지 않았음을 이야기합니다.

JSHint가 JSLint를 포크(fork)하여 만든 이유는 아래 개발자의 블로그에 작성돼 있습니다.

- [Why I forked JSLint to JSHint — Medium](https://medium.com/@valueof/why-i-forked-jslint-to-jshint-73a72fd3612 "Why I forked JSLint to JSHint — Medium")
- [JSLint에서 JSHint를 포크한 이유(일본어)](http://blog.node.ws/?p=1379 "JSLint에서 JSHint를 포크한 이유(일본어)")

ES.next를 일방적으로 지원하지 않겠다는 의미가 아니라 그 기능의 제안(proposal)의 상태가 Stage 2 이상인 것만 experimental 플래그를 사용해 지원한다고 합니다. Stage 2 이상을 지원하는 것은 지나치게 빠르지도 또 느리지도 않다고 이야기하고 있습니다.

Note: [TC39](http://www.ecma-international.org/memento/TC39.htm "TC39")(Technical Committee 39, 기술 위원회#39)에서는 표준을 재정하는 단계를 아래와 같이 나누고 있습니다.

* Stage 0(Strawman) : ECMAScript에 넣고 싶은 아이디어를 논의하는 단계
* Stage 1(Proposal) : Strawman을 구체화하고 데모를 작성하거나 분석하는 단계(브라우저가 플래그로 실험적으로 지원을 하는 단계이기도 합니다)
* Stage 2(Draft) : 정식 사양을 형식에 맞게 정의하고 작성하는 단계
* Stage 3(Candidate) : Draft를 구현하고 피드백을 받는 단계
* Stage 4(Finished) : ECMAScript에 정식으로 채용하고 [Test262](https://github.com/tc39/test262 "Test262")에 구현하는 단계

- [TC39 Process - Google 문서](https://docs.google.com/document/d/1QbEE0BsO4lvl7NFTn5WXWeiEIBfaVUF7Dk0hpPpPDzU/edit?pli=1 "TC39 Process - Google 문서")

JSHint 3는 이 지침에 따라 아래와 같은 규칙을 정하고 있는 것 같습니다.

- `esnext` 옵션 폐지
- `moz` 옵션 지속
- ES6는 `esversion: 6` 옵션으로 지원
- ES7은 제대로 표준화가 이루어지면 지원
- Stage 2 이상의 제안은 `experimental` 옵션으로 지원

----

JSHint의 경쟁 상대로 [ESLint](https://github.com/eslint/eslint "ESLint")나 이것을 이용한 [Babel이 지원하는 Stage n의 제안](http://babeljs.io/blog/2015/03/31/5.0.0/ "5.0.0 Released · Babel")도 검증할 수 있는 [babel-eslint](https://github.com/babel/babel-eslint "babel-eslint")가 있습니다.

ESLint는 유연한 지원을 하기 위해 플러그인 시스템을 채용하고 있지만,
플러그인은 플러그인만의 어려움이 있어 아래와 같은 것도 논의되고 있습니다.

<blockquote class="twitter-tweet" lang="en"><p lang="en" dir="ltr"><a href="https://twitter.com/mjackson">@mjackson</a> FWIW (roughly) over 1/3 of ESLint users use babel-eslint. In the future ESLint won&#39;t even be required as it&#39;ll be rolled into core</p>&mdash; Sebastian McKenzie (@sebmck) <a href="https://twitter.com/sebmck/status/619607489252880384">July 10, 2015</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

ESLint와 역할이 미묘하게 겹쳐 경쟁 상대이기도 한 [JSCS](https://github.com/jscs-dev/node-jscs "JSCS")の[@mikesherov](https://twitter.com/mikesherov "@mikesherov")가 말한 것 처럼,
경쟁이 있다는 것은 건강하다는 것이기 때문에 앞으로도 검증 도구가 서로의 방침에 있어서 발전하는 것은 좋은 일이라 생각합니다.

<blockquote class="twitter-tweet" data-conversation="none" lang="en"><p lang="en" dir="ltr"><a href="https://twitter.com/mikesherov">@mikesherov</a> <a href="https://twitter.com/sebmck">@sebmck</a> having 2 impls is fine. Better than monoculture. It&#39;s when 20 show up that sucks. Why I love Acorn AND Esprima.</p>&mdash; Mike Sherov (@mikesherov) <a href="https://twitter.com/mikesherov/status/619694583476322304">July 11, 2015</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>
