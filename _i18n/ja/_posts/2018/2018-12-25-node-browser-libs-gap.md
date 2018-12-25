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

# Node.jsコアモジュールとBundlerによるpolyfillのギャップ

このレポートは、現在進行形で機能追加や仕様変更が行われているNode.jsコアモジュールとブラウザ向けpolyfillにおける挙動の違い(ギャップ)が広がってきている問題について調べたものです。

ここでは <https://nodejs.org/api/> に掲載されているうち `assert`のようにNode.jsにバンドルされているモジュールのことをNode.jsコアモジュールと呼びます。コアモジュールはNode.jsでの利用のみを想定しているため、Node.jsに依存した処理を多く含んでいます。そのため、コアモジュールのコードをコピーしてブラウザなどで動かすことは難しいです。

[webpack](https://github.com/webpack/webpack "webpack")や[browserify](https://github.com/substack/node-browserify "browserify")などのbundlerは、コード中にあるコアモジュールを代替モジュールへとすり替えます。この代替モジュールはブラウザ向けpolyfillライブラリとよび、このpolyfillライブラリはブラウザで動くようにNode.jsコアモジュールと同等また空のダミー実装をしています。

## Node.jsコアモジュールのpolyfillライブラリの例

webpackとbrowserifyは変換時に、コード中に現れる`assert`モジュールを[commonjs-assert](https://github.com/browserify/commonjs-assert "commonjs-assert")というpolyfillライブラリに自動的にすり替えられます。

```js
const assert = require("assert")
```

というコードはwebpackなどでbundleすると、次のように書いたのと同じようにモジュールの差し替えが行われる。

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


|    Node.js     |               Browser polyfill               |                  Issue                   | Link                                     |
| :------------: | :--------------------------------------: | :--------------------------------------: | ---------------------------------------- |
|     assert     | [browserify/commonjs-assert](https://github.com/browserify/commonjs-assert) | Error code and Error message are different | [Issue](https://github.com/nodejs/node/issues/13937), [Article](https://medium.com/the-node-js-collection/node-js-errors-changes-you-need-to-know-about-dc8c82417f65) |
|                |                                          | `assert.deepEqual` does't support `Map`, `Set`, `Iterator` etc... | [Issue](https://github.com/nodejs/node/issues/2309), [Document](https://nodejs.org/api/assert.html#assert_assert_deepequal_actual_expected_message), [Release](https://nodejs.org/en/blog/release/v8.0.0/) |
|                |                                          | `require("assert").strict` | [Docs](https://nodejs.org/api/assert.html#assert_strict_mode), [Release](https://nodejs.org/en/blog/release/v9.9.0/) |
|                |                                          | [`assert.rejects()`](https://nodejs.org/api/assert.html#assert_assert_rejects_block_error_message) | [Release](https://nodejs.org/en/blog/release/v10.0.0/) |
|                |                                          | [`assert.doesNotReject()`](https://nodejs.org/api/assert.html#assert_assert_doesnotreject_block_error_message) | [Release](https://nodejs.org/en/blog/release/v10.0.0/) |
|                |                                          | Compatible issue with `assert.fail()`, `assert.ok()`, and `assert.ifError()`|  No arguments behavior. [Release](https://nodejs.org/en/blog/release/v10.0.0/) |
|     buffer     | [feross/buffer](https://github.com/feross/buffer) |                   ---                    |                                          |
| child_process  |                   ---                    |                   ---                    |                                          |
|    cluster     |                   ---                    |                   ---                    |                                          |
|    console     | [Raynos/console-browserify](https://github.com/Raynos/console-browserify) |                   ---                    |                                          |
|   constants    | [juliangruber/constants-browserify](https://github.com/juliangruber/constants-browserify) |                   ---                    |                                          |
|     crypto     | [crypto-browserify/crypto-browserify](https://github.com/crypto-browserify/crypto-browserify) |                   ---                    |                                          |
|     dgram      |                   ---                    |                   ---                    |                                          |
|      dns       |                   ---                    |                   ---                    |                                          |
|     domain     | [bevry/domain-browser](https://github.com/bevry/domain-browser) |                   ---                    |                                          |
|     events     | [Gozala/events](https://github.com/Gozala/events) | [`eventNames`](https://nodejs.org/api/events.html#events_emitter_eventnames) | [Issue](https://github.com/Gozala/events/pull/32) |
|                |                                          | [`getMaxListeners`](https://nodejs.org/api/events.html#events_emitter_getmaxlisteners) | [Issue](https://github.com/Gozala/events/pull/32) |
|                |                                          | [`prependListener`](https://nodejs.org/api/events.html#events_emitter_prependlistener_eventname_listener) | [Issue](https://github.com/Gozala/events/pull/32) |
|                |                                          | [`prependOnceListener`](https://nodejs.org/api/events.html#events_emitter_prependoncelistener_eventname_listener) | [Issue](https://github.com/Gozala/events/pull/32) |
|                |                                          | `off` | [Issue](https://github.com/nodejs/node/pull/17156) |
|       fs       |                   ---                    |                   ---                    |                                          |
|      http      | [jhiesey/stream-http](https://github.com/jhiesey/stream-http) |                   ---                    |                                          |
|     https      | [substack/https-browserify](https://github.com/substack/https-browserify) |                   ---                    |                                          |
|     module     |                   ---                    |                   ---                    |                                          |
|      net       |                   ---                    |                   ---                    |                                          |
|       os       | [CoderPuppy/os-browserify](https://github.com/CoderPuppy/os-browserify) | [os.constants](https://nodejs.org/api/os.html#os_os_constants "os.constants") |                                          |
|      path      | [browserify/path-browserify](https://github.com/browserify/path-browserify) | [path.posix](https://nodejs.org/api/path.html#path_path_posix "path.posix") | [Issue](https://github.com/browserify/path-browserify/issues/11 "Update to use newer node path code · Issue #11 · substack/path-browserify") |
|                |                                          | [path.parse(path)](https://nodejs.org/docs/latest/api/path.html#path_path_parse_path "path.parse(path)") | [Issue](https://github.com/browserify/path-browserify/issues/2) |
|                |                                          | [path.win32](https://nodejs.org/api/path.html#path_path_posix "path.win32") |                                          |
|                |                                          | [path.format(pathObject)](https://nodejs.org/api/path.html#path_path_posix "path.format(pathObject)") |                                          |
|    process     | [defunctzombie/node-process](https://github.com/defunctzombie/node-process) | [process.channel](https://nodejs.org/api/process.html#process_process_channel "process.channel") |                                          |
|                |                                          | [process.platform](https://nodejs.org/api/process.html#process_process_platform "process.platform") | [Issue](https://github.com/defunctzombie/node-process/issues/55) |
|                |                                          | [process.execArgv](https://nodejs.org/api/process.html#process_process_execargv "process.execArgv") | [Issue](https://github.com/defunctzombie/node-process/issues/75) |
|                |                                          | [process.cpuUsage([previousValue])](https://nodejs.org/api/process.html#process_process_cpuusage_previousvalue "process.cpuUsage([previousValue])") |                                          |
|                |                                          | [process.emitWarning(warning[, options])](https://nodejs.org/api/process.html#process_process_emitwarning_warning_options "process.emitWarning(warning[, options])") |                                          |
|    punycode    | [bestiejs/punycode.js](https://github.com/bestiejs/punycode.js) |                   ---                    |                                          |
|  querystring   | [mike-spainhower/querystring](https://github.com/mike-spainhower/querystring) |                   ---                    |                                          |
|    readline    |                   ---                    |                   ---                    |                                          |
|      repl      |                   ---                    |                   ---                    |                                          |
|     stream     | [browserify/stream-browserify](https://github.com/browserify/stream-browserify) |                   ---                    |                                          |
| string_decoder | [rvagg/string_decoder](https://github.com/rvagg/archived-string_decoder) |                   TODO                   | [Repository](https://github.com/nodejs/string_decoder) |
|      sys       | [defunctzombie/node-util](https://github.com/defunctzombie/node-util) |                   TODO                   |                                          |
|     timers     | [browserify/timers-browserify](https://github.com/browserify/timers-browserify) |                   ---                    |                                          |
|      tls       |                   ---                    |                   ---                    |                                          |
|      tty       | [browserify/tty-browserify](https://github.com/browserify/tty-browserify) |                   ---                    |                                          |
|      url       | [defunctzombie/node-url](https://github.com/defunctzombie/node-url) |          `url.URL`(WHATWG URL)           | [Release](https://nodejs.org/en/blog/release/v8.0.0/#say-hello-to-the-whatwg-url-parser), [Document](https://nodejs.org/api/url.html#url_the_whatwg_url_api), [Issue](https://github.com/defunctzombie/node-url/issues/33) |
|                |                                          | `url.format` does't support  WHATWG URL  | [Release](https://nodejs.org/en/blog/release/v7.6.0/), [Document](https://nodejs.org/api/url.html#url_url_format_url_options) |
|      util      | [defunctzombie/node-util](https://github.com/defunctzombie/node-util) | [util.callbackify(original)](https://nodejs.org/api/util.html#util_util_callbackify_original "util.callbackify(original)") |                                          |
|                |                                          | [util.inspect.custom](https://nodejs.org/api/util.html#util_util_inspect_custom "util.inspect.custom") |                                          |
|                |                                          | [util.inspect.defaultOptions](https://nodejs.org/api/util.html#util_util_inspect_defaultoptions "util.inspect.defaultOptions") |                                          |
|                |                                          | [util.promisify(original)](https://nodejs.org/api/util.html#util_util_promisify_original "util.promisify(original)") |                                          |
|                |                                          | [util.promisify.custom](https://nodejs.org/api/util.html#util_util_promisify_custom "util.promisify.custom") |                                          |
|                |                                          | [util.inspect() options maxArrayLength, breakLength](https://github.com/defunctzombie/node-util/issues/15 "util.inspect() options maxArrayLength, breakLength") |                                          |
|                |                                          | [util.isDeepStrictEqual](https://nodejs.org/api/util.html#util_util_isdeepstrictequal_val1_val2) |                                          |
|                |                                          | [util.isDeepStrictEqual](https://nodejs.org/api/util.html#util_util_isdeepstrictequal_val1_val2) |                                          |
|       vm       | [browserify/vm-browserify](https://github.com/browserify/vm-browserify) | [vm.isContext(sandbox)](https://nodejs.org/api/vm.html#vm_vm_runincontext_code_contextifiedsandbox_options "vm.isContext(sandbox)") |                                          |
|      zlib      | [devongovett/browserify-zlib](https://github.com/devongovett/browserify-zlib) | [zlib.bytesRead](https://nodejs.org/api/zlib.html#zlib_zlib_bytesread "zlib.bytesRead#") |                                          |

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

0/24のテストをパス。
Gapリストに載っているものは未実装となっているpolyfillが使わrています。

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


## おわりに

このレポートは、webpackやbrowserifyを使っているとあまり意識されないpolyfillライブラリに潜在的な問題があることを調べる目的で書きました。この問題の難しさは各polyfillライブラリの管理者やバランスが異なるにもかかわらず、polyfillライブラリ群として暗黙的に参照されている点です。

多くのコアモジュールにおいては、問題が表面化しない可能性もあります。
しかし、`assert`、`events`、`url`はブラウザ向けとしてよく使われているにもかかわらず、差異が分かる程度にはあります。
また、これらの問題が解決できた場合にも、webpackやbrowserifyには暗黙的にpolyfillライブラリを差し替える仕組み上は、バージョン違いといった互換性の問題が発生するかもしれません。

- [Node.js Errors — Changes you need to know about – Node.js Collection – Medium](https://medium.com/the-node-js-collection/node-js-errors-changes-you-need-to-know-about-dc8c82417f65 "Node.js Errors — Changes you need to know about – Node.js Collection – Medium")
  - `assert`結果の`Error#name`などが異なるため、Node.jsでは通るがブラウザ(polyfill)では失敗するテストができる
  - MapやSetなどES2015以降のビルトインオブジェクトに対応していない
- [Node v7 で入った WHATWG URL 実装について | blog.jxck.io](https://blog.jxck.io/entries/2016-10-27/whatwg-url.html "Node v7 で入った WHATWG URL 実装について | blog.jxck.io")
  - Node.jsがブラウザのWHATWG URLをサポートしたが、ブラウザ(polyfill)ではサポートされていない

webpackなどにIssueで同様の問題を報告していましたが、このIssueについては特に進捗はありませんでした。

- [Incompatibility between Node.js core libs and webpack's lib · Issue #78 · webpack/node-libs-browser](https://github.com/webpack/node-libs-browser/issues/78)

最近になって、2018年12月21日に[webpack 5 alpha](https://github.com/webpack/webpack/issues/8537)が公開されました。
webpack 5では自動的にNode.jsコアモジュールのpolyfillを自動的に入れないようにする変更が予定されています。
(2018年12月25日時点ではただの予定であるため、[該当Issue](https://github.com/webpack/webpack/issues/8537)においてフィードバックを求めています。)

> In the early days, webpack's aim was to allow running most node.js modules in the browser, but the module landscape changed and many module uses are now written mainly for frontend purposes.
> -- <https://github.com/webpack/changelog-v5/blob/master/README.md#automatic-nodejs-polyfills-removed>

CHANGELOGにこのように書かれているのように、webpackはNode.jsモジュールをブラウザ向けにpack(polyfill)する役割から、フロントエンド向けに書かれたモジュールをbundleする役割へ変わってきています。

今までは`Buffer`など[Node.jsのコアAPI](https://nodejs.org/api/index.html)に対応するモジュールを自動的にbundleすることで、Node.js向けに書かれたモジュールをブラウザでも動かせるようにしていました。
一方で、現在ではブラウザ向けに書かれたは多くのモジュールがあるため、webpackが自動的にpolyfillを入れる必然性が小さくなってきています。

また、`Buffer`のpolyfillなどはファイルサイズがほどほどに大きいため、パフォーマンス面においては自動的にpolyfillを行わないメリットもあります。(polyfillを行うかどうかは、webpack 4でも[node](https://webpack.js.org/configuration/node/)オプションによって設定が可能です)

少しブラウザとは異なりますが、React Nativeの[Bundler](https://facebook.github.io/metro/)もNode.jsのコアモジュールのpolyfillを自動的にbundleはしない仕組みになっています。

- [Unable to resolve module `assert` `buffer` `events` · Issue #21405 · facebook/react-native](https://github.com/facebook/react-native/issues/21405)

このように、BundlerがNode.jsコアモジュールのpolyfillを暗黙的に入れるという挙動の状況は少し変わりつつあります。
これは、[webpack 5の変更予定](https://github.com/webpack/changelog-v5/blob/master/README.md#automatic-nodejs-polyfills-removed)にも書かれていたように、Bundlerの目的の1つがNode.js向けに書かれたモジュールをブラウザ向けに変換することでした。
しかし、現在は多くのブラウザ向けに書かれたモジュールがあり、Bundlerはそれを効率的に扱うという目的に変わってきている点も関係しているのかもしれません。

## [jser/report](https://github.com/jser/report) バックナンバー

- [JSerレポート #1 Bundlerの未来、テスティングフレームワークの現状 - JSer.info](https://jser.info/2017/01/31/bundler-testing-framework-report/)