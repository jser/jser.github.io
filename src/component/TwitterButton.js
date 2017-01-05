// MIT © 2017 azu
"use strict";
import {h} from 'preact';
export default function TwitterButton({text, url, via}) {
    const src = `https://platform.twitter.com/widgets/tweet_button.html?size=l&url=${encodeURIComponent(url)}&via=${via}&text=${encodeURIComponent(text)}`
    return <iframe
        src={src}
        width="140"
        height="28"
        title="Twitter Tweet Button"
        scrolling="no"
        style="border: 0; overflow: hidden;">
    </iframe>
}