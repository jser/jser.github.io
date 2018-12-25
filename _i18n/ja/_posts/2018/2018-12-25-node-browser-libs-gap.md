---
title: "JSerレポート #2: Node.jsコアモジュールとBundler(webpackなど)によるpolyfillのギャップ"
author: azu
layout: post
date : 2018-12-25T12:14
category: レポート
tags:
    - webpack
    - browserify
    - node.js
    - polyfill

---

このレポートは、現在進行形で機能追加や仕様変更が行われているNode.jsコアモジュールとブラウザ向けpolyfillにおける挙動の違い(ギャップ)が広がってきている問題について調べたものです。

ここでは <https://nodejs.org/api/> に掲載されているうち `assert`のようにNode.jsにバンドルされているモジュールのことをNode.jsコアモジュールと呼びます。コアモジュールはNode.jsでの利用のみを想定しているため、Node.jsに依存した処理を多く含んでいます。そのため、コアモジュールのコードをコピーしてブラウザなどで動かすことは難しいです。

[webpack](https://github.com/webpack/webpack "webpack")や[browserify](https://github.com/substack/node-browserify "browserify")などのbundlerは、コード中にあるコアモジュールを代替モジュールへとすり替えます。この代替モジュールはブラウザ向けpolyfillライブラリとよび、このpolyfillライブラリはブラウザで動くようにNode.jsコアモジュールと同等また空のダミー実装をしています。

## Node.jsコアモジュールのpolyfillライブラリの例

webpackとbrowserifyは変換時に、コード中に現れる`assert`モジュールを[commonjs-assert](https://github.com/browserify/commonjs-assert "commonjs-assert")というpolyfillライブラリに自動的にすり替えます。

```js
const assert = require("assert")
```

というコードはwebpackなどでbundleすると、次のように書いたのと同じようにモジュールの差し替えが行われます。

```js
const assert = require("commonjs-assert")
```

webpackでは、このNode.jsコアモジュールへの差し替えを[node](https://webpack.js.org/configuration/node/)オプションによって設定が可能です。

## polyfill library

webpackとbrowserifyが利用するpolyfillライブラリは次の場所で管理されています。

- webpack:
  - [webpack/node-libs-browser: The node core libs for in browser usage.](https://github.com/webpack/node-libs-browser "webpack/node-libs-browser: The node core libs for in browser usage.")
- browserify:
  - [substack/browserify-handbook: how to build modular applications with browserify](https://github.com/substack/browserify-handbook#builtins)
  - [node-browserify/builtins.js at master · substack/node-browserify](https://github.com/substack/node-browserify/blob/master/lib/builtins.js)

どちらも基本的に利用しているpolyfill自体はほとんど同じです。  
  
## 機能のギャップ

このレポートの本題であるNode.jsコアモジュールとブラウザ向けpolyfillのギャップがあったものをまとめた表です。
ここでいうギャップというのは、次のようなケースを並べています。

- Node.jsコアモジュールで追加されたAPIがpolyfillライブラリには存在しない
- Node.jsコアモジュールとpolyfillライブラリで挙動が異なる
- 利用されているpolyfillライブラリがDeprecatedになっている

これらの調査結果については次のリポジトリで管理しています。最新の状況もこのリポジトリに反映しています。
そのため次の表は古くなっている可能性があります。

- [azu/node-browser-polyfill-gap: The gap issue between Node.js and Browser polyfills.](https://github.com/azu/node-browser-polyfill-gap "azu/node-browser-polyfill-gap: The gap issue between Node.js and Browser polyfills.")

注記: 依存しているpolyfillそのものはアップデートで解決されている場合があります。しかし、bundlerが古いバージョンを使っている場合があります。

<table border="1">
<thead>
<tr>
<th style="text-align:center">Node.js</th>
<th style="text-align:center">Browser polyfill</th>
<th style="text-align:center">Issue</th>
<th>Link</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center">assert</td>
<td style="text-align:center"><a href="https://github.com/browserify/commonjs-assert">browserify/commonjs-assert</a></td>
<td style="text-align:center">Error code and Error message are different</td>
<td><a href="https://github.com/nodejs/node/issues/13937">Issue</a>, <a href="https://medium.com/the-node-js-collection/node-js-errors-changes-you-need-to-know-about-dc8c82417f65">Article</a></td>
</tr>
<tr>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
<td style="text-align:center"><code>assert.deepEqual</code> does&#39;t support <code>Map</code>, <code>Set</code>, <code>Iterator</code> etc...</td>
<td><a href="https://github.com/nodejs/node/issues/2309">Issue</a>, <a href="https://nodejs.org/api/assert.html#assert_assert_deepequal_actual_expected_message">Document</a>, <a href="https://nodejs.org/en/blog/release/v8.0.0/">Release</a></td>
</tr>
<tr>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
<td style="text-align:center"><code>require(&quot;assert&quot;).strict</code></td>
<td><a href="https://nodejs.org/api/assert.html#assert_strict_mode">Docs</a>, <a href="https://nodejs.org/en/blog/release/v9.9.0/">Release</a></td>
</tr>
<tr>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
<td style="text-align:center"><a href="https://nodejs.org/api/assert.html#assert_assert_rejects_block_error_message"><code>assert.rejects()</code></a></td>
<td><a href="https://nodejs.org/en/blog/release/v10.0.0/">Release</a></td>
</tr>
<tr>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
<td style="text-align:center"><a href="https://nodejs.org/api/assert.html#assert_assert_doesnotreject_block_error_message"><code>assert.doesNotReject()</code></a></td>
<td><a href="https://nodejs.org/en/blog/release/v10.0.0/">Release</a></td>
</tr>
<tr>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
<td style="text-align:center">Compatible issue with <code>assert.fail()</code>, <code>assert.ok()</code>, and <code>assert.ifError()</code></td>
<td>No arguments behavior. <a href="https://nodejs.org/en/blog/release/v10.0.0/">Release</a></td>
</tr>
<tr>
<td style="text-align:center">buffer</td>
<td style="text-align:center"><a href="https://github.com/feross/buffer">feross/buffer</a></td>
<td style="text-align:center">---</td>
<td></td>
</tr>
<tr>
<td style="text-align:center">child_process</td>
<td style="text-align:center">---</td>
<td style="text-align:center">---</td>
<td></td>
</tr>
<tr>
<td style="text-align:center">cluster</td>
<td style="text-align:center">---</td>
<td style="text-align:center">---</td>
<td></td>
</tr>
<tr>
<td style="text-align:center">console</td>
<td style="text-align:center"><a href="https://github.com/Raynos/console-browserify">Raynos/console-browserify</a></td>
<td style="text-align:center">---</td>
<td></td>
</tr>
<tr>
<td style="text-align:center">constants</td>
<td style="text-align:center"><a href="https://github.com/juliangruber/constants-browserify">juliangruber/constants-browserify</a></td>
<td style="text-align:center">---</td>
<td></td>
</tr>
<tr>
<td style="text-align:center">crypto</td>
<td style="text-align:center"><a href="https://github.com/crypto-browserify/crypto-browserify">crypto-browserify/crypto-browserify</a></td>
<td style="text-align:center">---</td>
<td></td>
</tr>
<tr>
<td style="text-align:center">dgram</td>
<td style="text-align:center">---</td>
<td style="text-align:center">---</td>
<td></td>
</tr>
<tr>
<td style="text-align:center">dns</td>
<td style="text-align:center">---</td>
<td style="text-align:center">---</td>
<td></td>
</tr>
<tr>
<td style="text-align:center">domain</td>
<td style="text-align:center"><a href="https://github.com/bevry/domain-browser">bevry/domain-browser</a></td>
<td style="text-align:center">---</td>
<td></td>
</tr>
<tr>
<td style="text-align:center">events</td>
<td style="text-align:center"><a href="https://github.com/Gozala/events">Gozala/events</a></td>
<td style="text-align:center"><a href="https://nodejs.org/api/events.html#events_emitter_eventnames"><code>eventNames</code></a></td>
<td><a href="https://github.com/Gozala/events/pull/32">Issue</a></td>
</tr>
<tr>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
<td style="text-align:center"><a href="https://nodejs.org/api/events.html#events_emitter_getmaxlisteners"><code>getMaxListeners</code></a></td>
<td><a href="https://github.com/Gozala/events/pull/32">Issue</a></td>
</tr>
<tr>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
<td style="text-align:center"><a href="https://nodejs.org/api/events.html#events_emitter_prependlistener_eventname_listener"><code>prependListener</code></a></td>
<td><a href="https://github.com/Gozala/events/pull/32">Issue</a></td>
</tr>
<tr>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
<td style="text-align:center"><a href="https://nodejs.org/api/events.html#events_emitter_prependoncelistener_eventname_listener"><code>prependOnceListener</code></a></td>
<td><a href="https://github.com/Gozala/events/pull/32">Issue</a></td>
</tr>
<tr>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
<td style="text-align:center"><code>off</code></td>
<td><a href="https://github.com/nodejs/node/pull/17156">Issue</a></td>
</tr>
<tr>
<td style="text-align:center">fs</td>
<td style="text-align:center">---</td>
<td style="text-align:center">---</td>
<td></td>
</tr>
<tr>
<td style="text-align:center">http</td>
<td style="text-align:center"><a href="https://github.com/jhiesey/stream-http">jhiesey/stream-http</a></td>
<td style="text-align:center">---</td>
<td></td>
</tr>
<tr>
<td style="text-align:center">https</td>
<td style="text-align:center"><a href="https://github.com/substack/https-browserify">substack/https-browserify</a></td>
<td style="text-align:center">---</td>
<td></td>
</tr>
<tr>
<td style="text-align:center">module</td>
<td style="text-align:center">---</td>
<td style="text-align:center">---</td>
<td></td>
</tr>
<tr>
<td style="text-align:center">net</td>
<td style="text-align:center">---</td>
<td style="text-align:center">---</td>
<td></td>
</tr>
<tr>
<td style="text-align:center">os</td>
<td style="text-align:center"><a href="https://github.com/CoderPuppy/os-browserify">CoderPuppy/os-browserify</a></td>
<td style="text-align:center"><a href="https://nodejs.org/api/os.html#os_os_constants" title="os.constants">os.constants</a></td>
<td></td>
</tr>
<tr>
<td style="text-align:center">path</td>
<td style="text-align:center"><a href="https://github.com/browserify/path-browserify">browserify/path-browserify</a></td>
<td style="text-align:center"><a href="https://nodejs.org/api/path.html#path_path_posix" title="path.posix">path.posix</a></td>
<td><a href="https://github.com/browserify/path-browserify/issues/11" title="Update to use newer node path code · Issue #11 · substack/path-browserify">Issue</a></td>
</tr>
<tr>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
<td style="text-align:center"><a href="https://nodejs.org/docs/latest/api/path.html#path_path_parse_path" title="path.parse(path)">path.parse(path)</a></td>
<td><a href="https://github.com/browserify/path-browserify/issues/2">Issue</a></td>
</tr>
<tr>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
<td style="text-align:center"><a href="https://nodejs.org/api/path.html#path_path_posix" title="path.win32">path.win32</a></td>
<td></td>
</tr>
<tr>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
<td style="text-align:center"><a href="https://nodejs.org/api/path.html#path_path_posix" title="path.format(pathObject)">path.format(pathObject)</a></td>
<td></td>
</tr>
<tr>
<td style="text-align:center">process</td>
<td style="text-align:center"><a href="https://github.com/defunctzombie/node-process">defunctzombie/node-process</a></td>
<td style="text-align:center"><a href="https://nodejs.org/api/process.html#process_process_channel" title="process.channel">process.channel</a></td>
<td></td>
</tr>
<tr>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
<td style="text-align:center"><a href="https://nodejs.org/api/process.html#process_process_platform" title="process.platform">process.platform</a></td>
<td><a href="https://github.com/defunctzombie/node-process/issues/55">Issue</a></td>
</tr>
<tr>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
<td style="text-align:center"><a href="https://nodejs.org/api/process.html#process_process_execargv" title="process.execArgv">process.execArgv</a></td>
<td><a href="https://github.com/defunctzombie/node-process/issues/75">Issue</a></td>
</tr>
<tr>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
<td style="text-align:center"><a href="https://nodejs.org/api/process.html#process_process_cpuusage_previousvalue" title="process.cpuUsage([previousValue])">process.cpuUsage([previousValue])</a></td>
<td></td>
</tr>
<tr>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
<td style="text-align:center"><a href="https://nodejs.org/api/process.html#process_process_emitwarning_warning_options" title="process.emitWarning(warning[, options])">process.emitWarning(warning[, options])</a></td>
<td></td>
</tr>
<tr>
<td style="text-align:center">punycode</td>
<td style="text-align:center"><a href="https://github.com/bestiejs/punycode.js">bestiejs/punycode.js</a></td>
<td style="text-align:center">---</td>
<td></td>
</tr>
<tr>
<td style="text-align:center">querystring</td>
<td style="text-align:center"><a href="https://github.com/mike-spainhower/querystring">mike-spainhower/querystring</a></td>
<td style="text-align:center">---</td>
<td></td>
</tr>
<tr>
<td style="text-align:center">readline</td>
<td style="text-align:center">---</td>
<td style="text-align:center">---</td>
<td></td>
</tr>
<tr>
<td style="text-align:center">repl</td>
<td style="text-align:center">---</td>
<td style="text-align:center">---</td>
<td></td>
</tr>
<tr>
<td style="text-align:center">stream</td>
<td style="text-align:center"><a href="https://github.com/browserify/stream-browserify">browserify/stream-browserify</a></td>
<td style="text-align:center">---</td>
<td></td>
</tr>
<tr>
<td style="text-align:center">string_decoder</td>
<td style="text-align:center"><a href="https://github.com/rvagg/archived-string_decoder">rvagg/string_decoder</a></td>
<td style="text-align:center">TODO</td>
<td><a href="https://github.com/nodejs/string_decoder">Repository</a></td>
</tr>
<tr>
<td style="text-align:center">sys</td>
<td style="text-align:center"><a href="https://github.com/defunctzombie/node-util">defunctzombie/node-util</a></td>
<td style="text-align:center">TODO</td>
<td></td>
</tr>
<tr>
<td style="text-align:center">timers</td>
<td style="text-align:center"><a href="https://github.com/browserify/timers-browserify">browserify/timers-browserify</a></td>
<td style="text-align:center">---</td>
<td></td>
</tr>
<tr>
<td style="text-align:center">tls</td>
<td style="text-align:center">---</td>
<td style="text-align:center">---</td>
<td></td>
</tr>
<tr>
<td style="text-align:center">tty</td>
<td style="text-align:center"><a href="https://github.com/browserify/tty-browserify">browserify/tty-browserify</a></td>
<td style="text-align:center">---</td>
<td></td>
</tr>
<tr>
<td style="text-align:center">url</td>
<td style="text-align:center"><a href="https://github.com/defunctzombie/node-url">defunctzombie/node-url</a></td>
<td style="text-align:center"><code>url.URL</code>(WHATWG URL)</td>
<td><a href="https://nodejs.org/en/blog/release/v8.0.0/#say-hello-to-the-whatwg-url-parser">Release</a>, <a href="https://nodejs.org/api/url.html#url_the_whatwg_url_api">Document</a>, <a href="https://github.com/defunctzombie/node-url/issues/33">Issue</a></td>
</tr>
<tr>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
<td style="text-align:center"><code>url.format</code> does&#39;t support  WHATWG URL</td>
<td><a href="https://nodejs.org/en/blog/release/v7.6.0/">Release</a>, <a href="https://nodejs.org/api/url.html#url_url_format_url_options">Document</a></td>
</tr>
<tr>
<td style="text-align:center">util</td>
<td style="text-align:center"><a href="https://github.com/defunctzombie/node-util">defunctzombie/node-util</a></td>
<td style="text-align:center"><a href="https://nodejs.org/api/util.html#util_util_callbackify_original" title="util.callbackify(original)">util.callbackify(original)</a></td>
<td></td>
</tr>
<tr>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
<td style="text-align:center"><a href="https://nodejs.org/api/util.html#util_util_inspect_custom" title="util.inspect.custom">util.inspect.custom</a></td>
<td></td>
</tr>
<tr>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
<td style="text-align:center"><a href="https://nodejs.org/api/util.html#util_util_inspect_defaultoptions" title="util.inspect.defaultOptions">util.inspect.defaultOptions</a></td>
<td></td>
</tr>
<tr>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
<td style="text-align:center"><a href="https://nodejs.org/api/util.html#util_util_promisify_original" title="util.promisify(original)">util.promisify(original)</a></td>
<td></td>
</tr>
<tr>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
<td style="text-align:center"><a href="https://nodejs.org/api/util.html#util_util_promisify_custom" title="util.promisify.custom">util.promisify.custom</a></td>
<td></td>
</tr>
<tr>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
<td style="text-align:center"><a href="https://github.com/defunctzombie/node-util/issues/15" title="util.inspect() options maxArrayLength, breakLength">util.inspect() options maxArrayLength, breakLength</a></td>
<td></td>
</tr>
<tr>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
<td style="text-align:center"><a href="https://nodejs.org/api/util.html#util_util_isdeepstrictequal_val1_val2">util.isDeepStrictEqual</a></td>
<td></td>
</tr>
<tr>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
<td style="text-align:center"><a href="https://nodejs.org/api/util.html#util_util_isdeepstrictequal_val1_val2">util.isDeepStrictEqual</a></td>
<td></td>
</tr>
<tr>
<td style="text-align:center">vm</td>
<td style="text-align:center"><a href="https://github.com/browserify/vm-browserify">browserify/vm-browserify</a></td>
<td style="text-align:center"><a href="https://nodejs.org/api/vm.html#vm_vm_runincontext_code_contextifiedsandbox_options" title="vm.isContext(sandbox)">vm.isContext(sandbox)</a></td>
<td></td>
</tr>
<tr>
<td style="text-align:center">zlib</td>
<td style="text-align:center"><a href="https://github.com/devongovett/browserify-zlib">devongovett/browserify-zlib</a></td>
<td style="text-align:center"><a href="https://nodejs.org/api/zlib.html#zlib_zlib_bytesread" title="zlib.bytesRead#">zlib.bytesRead</a></td>
</tr>
</tbody>
</table>


## 実装状況

この[調査リポジトリ](https://github.com/azu/node-browser-polyfill-gap)には簡単な機能テストも実装されています。

- [node-browser-polyfill-gap/test at master · azu/node-browser-polyfill-gap](https://github.com/azu/node-browser-polyfill-gap/tree/master/test)

次にそれぞれでのテスト結果を示します。

### Node v11.5.0

24コのテストをすべてパス(これがpolyfillの元なので当然ですが…)

```
  24 passing (146ms)
```


### Browserify 16.2.3

4/24のテストをパス。

```
  gap-test
    assert
      1) Error#code
      2) assert.deepEqual
      3) assert.strict
      4) assert.rejects
      5) assert.doesNotReject
    events
      6) off
      ✓ eventNames
      ✓ getMaxListeners()
      ✓ prependListener()
      ✓ prependOnceListener()
    os
      7) constants
    path
      8) posix
      9) win32
      10) parse
      11) format
    process
      12) platform
      13) execArgv
      14) cpuUsage()
      15) emitWarning()
    url
      16) URL
    util
      17) inspect.defaultOptions
      18) callbackify()
      19) promisify()
    vm
      20) isContext


  4 passing (293ms)
  20 failing
```

### webpack 4.82.2

すべてのテストが失敗しました。
Gapリスト通りのpolyfillが使われています。

```
  gap-test
    assert
      1) Error#code
      2) assert.deepEqual
      3) assert.strict
      4) assert.rejects
      5) assert.doesNotReject
    events
      6) off
      7) eventNames
      8) getMaxListeners()
      9) prependListener()
      10) prependOnceListener()
    os
      11) constants
    path
      12) posix
      13) win32
      14) parse
      15) format
    process
      16) platform
      17) execArgv
      18) cpuUsage()
      19) emitWarning()
    url
      20) URL
    util
      21) inspect.defaultOptions
      22) callbackify()
      23) promisify()
    vm
      24) isContext


  0 passing (134ms)
  24 failing
```  


## Node.jsコアモジュールのpolyfillの今後

このレポートは、webpackやbrowserifyを使っているとあまり意識されないpolyfillライブラリに潜在的な問題があることを調べる目的で書きました。
この問題の難しさは各polyfillライブラリの管理者やバランスが異なるにもかかわらず、polyfillライブラリ群として暗黙的に参照されている点です。

多くのコアモジュールにおいては、問題が表面化しない可能性もあります。
しかし、`assert`、`events`、`url`はブラウザ向けとしてよく使われているにもかかわらず、差異が分かる程度にはあります。
また、ギャップの問題が解決できた場合にも、バージョンを指定できずに暗黙的なpolyfillライブラリを差し替える仕組みは、互換性の問題が発生するかもしれません。

- [Node.js Errors — Changes you need to know about – Node.js Collection – Medium](https://medium.com/the-node-js-collection/node-js-errors-changes-you-need-to-know-about-dc8c82417f65 "Node.js Errors — Changes you need to know about – Node.js Collection – Medium")
  - `assert`結果の`Error#name`などが異なるため、Node.jsでは通るがブラウザ(polyfill)では失敗するテストができる
  - MapやSetなどES2015以降のビルトインオブジェクトに対応していない
- [Node v7 で入った WHATWG URL 実装について | blog.jxck.io](https://blog.jxck.io/entries/2016-10-27/whatwg-url.html "Node v7 で入った WHATWG URL 実装について | blog.jxck.io")
  - Node.jsがブラウザのWHATWG URLをサポートしたが、ブラウザ(polyfill)ではサポートされていない

webpackなどにIssueで同様の問題を報告していましたが、このIssueについては特に進捗はありませんでした。

- [Incompatibility between Node.js core libs and webpack's lib · Issue #78 · webpack/node-libs-browser](https://github.com/webpack/node-libs-browser/issues/78)

最近(2018年12月21日)になって[webpack 5 alpha](https://github.com/webpack/webpack/issues/8537)が公開されました。
webpack 5では自動的にNode.jsコアモジュールのpolyfillを自動的に入れないようにする変更が予定されています。
(2018年12月25日時点ではただの予定であるため、[該当Issue](https://github.com/webpack/webpack/issues/8537)においてフィードバックを求めています。)

> In the early days, webpack's aim was to allow running most node.js modules in the browser, but the module landscape changed and many module uses are now written mainly for frontend purposes.
> -- <https://github.com/webpack/changelog-v5/blob/master/README.md#automatic-nodejs-polyfills-removed>

変更理由としてこのように書かれているのように、webpackはNode.jsモジュールをブラウザ向けにpack(polyfill)する役割から、フロントエンド向けに書かれたモジュールをbundleする役割へ変わってきています。

今までは`Buffer`など[Node.jsのコアAPI](https://nodejs.org/api/index.html)に対応するモジュールを自動的にbundleすることで、Node.js向けに書かれたモジュールをブラウザでも動かせるようにしていました。
一方で、現在ではブラウザ向けに書かれた多くのモジュールがあるため、webpackが自動的にpolyfillを入れる必然性が少なくなってきています。

また、`Buffer`のpolyfillなどはファイルサイズがほどほどに大きいため、パフォーマンス面においては自動的にpolyfillを行わないメリットもあります。(polyfillを行うかどうかは、webpack 4でも[node](https://webpack.js.org/configuration/node/)オプションによって設定が可能です)

少しブラウザとは異なりますが、React Nativeの[Bundler](https://facebook.github.io/metro/)もNode.jsコアモジュールのpolyfillを自動的に差し替えない仕組みとなっています。

- [Unable to resolve module `assert` `buffer` `events` · Issue #21405 · facebook/react-native](https://github.com/facebook/react-native/issues/21405)

このように、BundlerがNode.jsコアモジュールのpolyfillを暗黙的に入れるという挙動の状況は少し変わりつつあります。
これは[webpack 5の変更予定](https://github.com/webpack/changelog-v5/blob/master/README.md#automatic-nodejs-polyfills-removed)にも書かれていたように、Bundlerの目的の1つがNode.js向けに書かれたモジュールをブラウザ向けに変換することでした。
しかし、現在は多くのブラウザ向けに書かれたモジュールがあり、Bundlerはそれを効率的に扱うという目的に変わってきている点も関係しているのかもしれません。

今回の調査で感じたのは、Node.jsのコアモジュールとブラウザ向けのPolyfillといった一種の互換レイヤーに対して関心を持っている人の絶対数が少ないという印象です。Node.jsもコアAPIとしてブラウザと同じ[WHATWG URL API](https://nodejs.org/api/url.html#url_the_whatwg_url_api)を実装するなどいった[ブラウザとの相互運用性](https://github.com/nodejs/node/pull/18281)に関する取り組みも行われています。
しかし、このNode.jsコアモジュールのpolyfillという互換レイヤーに関しては暗黙的に扱われていることが多く、その互換性に問題があることについてはあまり言及されていません。

W3C TAGの[Polyfills and the evolution of the Web](https://w3ctag.github.io/polyfills/)というドキュメントでpolyfillがどうあるべきかということについて書かれています。
このNode.jsコアモジュールのpolfyillの問題も[Node.jsとpolyfillのライフサイクルの違い](https://w3ctag.github.io/polyfills/#life-cycle)からきている面があると思います。
ブラウザにおける壊れたpolyfillの場合は仕様策定の際に問題となることがありましたが、幸いにもNode.jsのコアモジュールのpolyfillの多くはモジュールやBundlerという仕組みの上に作られたものです。

しかしながら、このNode.jsコアモジュールのpolfyillも一定数利用者がいるため互換性という問題からは切り離すことが難しいです。(polyfillの1つである[events](https://www.npmjs.com/package/events)モジュールは500万/weekダウンロードされています)
この問題に深く関係しているのはwebpackやbrowserifyなどのbundlerであるため、bundlerの動きがそのままNode.jsコアモジュールのpolfyillの今後に影響する可能性は高いと思います。

## [jser/report](https://github.com/jser/report) バックナンバー

- [JSerレポート #1 Bundlerの未来、テスティングフレームワークの現状 - JSer.info](https://jser.info/2017/01/31/bundler-testing-framework-report/)
