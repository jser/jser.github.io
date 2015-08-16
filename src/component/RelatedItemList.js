// LICENSE : MIT
"use strict";
import element from 'virtual-element'
import RelatedItem from "./RelatedItem"
export function render(component) {
    let {props, state, id} = component;
    var items = props.postWithItems.map((postWithItem, index) => {
        let {item, post} = postWithItem;
        return (
            <div>
                <dt><RelatedItem title={item.title} url={ item.url } content={item.content}></RelatedItem></dt>
                <dd>via <a href={post.url}>{post.title}</a></dd>
            </div>
        );

    });
    return <div className="RelatedItemList">
        <h1>関連する記事</h1>
        <dl>
            {items}
        </dl>
    </div>;
}
export default {render}