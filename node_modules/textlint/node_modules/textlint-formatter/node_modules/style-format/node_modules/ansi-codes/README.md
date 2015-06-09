## ansi-codes

ANSI Styling codes. Check out [styled](https://github.com/azer/styled) or [style-format](https://github.com/azer/style-format) if you're looking for an example usage of this library.

## Install

```bash
$ npm install ansi-codes
```

## Usage

```js
ansiCodes = require('ansi-codes')

ansiCodes.bold
// => \033[1m

ansiCodes.yellow
// => \033[31m

ansiCodes.greenBg
// => \033[42m
```

## Reference

**reset:**  \033[0m

**bold:**  \033[1m

**italic:**  \033[3m

**blink:**  \033[5m

**underline:**  \033[4m

**underlineOff:**  \033[24m

**inverse:**  \033[7m

**inverseOff:**  \033[27m

**strikethrough:**  \033[9m

**strikethroughOff:**  \033[29m

**def:**  \033[39m

**white:**  \033[37m

**black:**  \033[30m

**red:**  \033[31m

**green:**  \033[32m

**blue:**  \033[34m

**yellow:**  \033[33m

**magenta:**  \033[35m

**cyan:**  \033[36m

**defBg:**  \033[49m

**whiteBg:**  \033[47m

**blackBg:**  \033[40m

**redBg:**  \033[41m

**greenBg:**  \033[42m

**blueBg:**  \033[44m

**yellowBg:**  \033[43m

**magentaBg:**  \033[45m

**cyanBg:**  \033[46m

![](https://dl.dropboxusercontent.com/s/r19djuexd699h44/npmel_22.jpg)
