'use strict';
var path = require('path');
var markdownExtensions = require('markdown-extensions');

module.exports = function (str) {
	if (typeof str !== 'string') {
		throw new TypeError('Expected a string');
	}

	return markdownExtensions.indexOf(path.extname(str).slice(1).toLowerCase()) !== -1;
};
