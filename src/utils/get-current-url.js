// MIT © 2017 azu
"use strict";
import {stripQuery} from "./strip-query";
export function getCurrentURL() {
    // localhostでもマッチするように
    if (process.env.NODE_ENV === 'development') {
        return stripQuery(`https://jser.info${location.pathname}`);
    }
    return stripQuery(location.href);
}