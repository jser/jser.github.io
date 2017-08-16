'use strict';
const fs =  require('fs');
const path = require('path');
const globby = require('globby');
const StructuredSource =require('structured-source');

const srcDir = path.join(__dirname, '../../_i18n/');
/**
 * 対象となるファイル一覧
 * @type {string[]}}
 */
const targetFiles = globby.sync([`${srcDir}/**/*.md`]);
/**
 * 利用してはいけない制御コードの一覧
 * @type {[string]}
 */
const invalidControlCharacters = ['\u0008'];
/**
 * \uXXXX 形式に文字列をエスケープする関数
 * @param {string} str
 * @return {string}
 */
const unicodeEscape = str => {
  return str.replace(/./g, c => {
    return `\\u${`000${c.charCodeAt(0).toString(16)}`.substr(-4)}`;
  });
};

describe('制御文字を含んでいるかのテスト', () => {
  targetFiles.forEach(filePath => {
    const fileName = path.basename(filePath);
    it(`${fileName} は制御文字を含んでいない`, () => {
      const content = fs.readFileSync(filePath, 'utf-8');
      invalidControlCharacters.forEach(controlChar => {
        const index = content.indexOf(controlChar);
        if (index === -1) {
          return; // ok
        }
        const source = new StructuredSource(content);
        const {line, column} = source.indexToPosition(index);
        throw new Error(`制御文字(${unicodeEscape(controlChar)})が含まれています。
  at ${filePath}:${line}:${column}
`);
      });
    });
  });
});
