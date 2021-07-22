// LICENSE : MIT
"use strict";
import {h} from 'preact';
import RelatedItem from "./RelatedItem"
import removeMarkdown from "remove-markdown";
function ellipsis(text) {
    if (text.length > 200) {
        return text.slice(0, 200) + "…";
    }
    return text;
}
export default function RelatedItemList({postWithItems}) {
    var items = postWithItems.map((postWithItem, index) => {
        let {item, post} = postWithItem;
        // strip markdown
        var plainText = removeMarkdown(item.content, {stripListLeaders: false});

        return <div class="RelatedItem">
            <h4><RelatedItem title={item.title} url={item.url}/></h4>
            <cite><a href={post.url} title={post.title}
                     target="_blank">{post.title.replace(/(\d{4}-\d{2}-\d{2}のJS).*$/, "$1")}</a></cite>
            <p class="RelatedItem--description">{ellipsis(plainText)}</p>
        </div>

    });
    return <div class="RelatedItemList">
        <h3 class="RelatedItemList--title">関連する記事</h3>
        <dl>
            {items}
        </dl>
    </div>;
}