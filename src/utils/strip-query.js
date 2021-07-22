// MIT © 2017 azu
"use strict";
/**
 * urlから?や#を取り除く
 * @param {string} url
 * @returns {string}
 */
export function stripQuery(url) {
    return url.split(/[?#]/)[0];
}