// LICENSE : MIT
"use strict";
import element from 'virtual-element'
export function render(component) {
    let {props, state, id} = component;
    return <a className="RelatedItem" href={props.url}>{props.title}</a>
}
export default {
    render
}