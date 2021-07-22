// LICENSE : MIT
"use strict";
import {h} from 'preact';
export default function RelatedItem({url, title}) {
    return <a className="RelatedItem" href={url} target="_blank">{title}</a>
}