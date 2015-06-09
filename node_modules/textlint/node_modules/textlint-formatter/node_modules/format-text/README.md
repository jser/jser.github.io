## format-text

String formatting library inspired from Python

### Install

```bash
$ npm install new-format
```

### Usage

```js
format = require('format-text')

format('Hello {0}. The weather is currently {1}°.', 'Kitty', '67')
// => Hello Kitty. The weather is currently 67°.

format('Hello {name}, The weather is currently {degree}°', { name:'Kitty', degree: 67 })
// => Hello Kitty. The weather is currently 67°.
```

![](https://dl.dropbox.com/s/9q2p5mrqnajys22/npmel.jpg?token_hash=AAHqttN9DiGl63ma8KRw-G0cdalaiMzrvrOPGnOfDslDjw)
