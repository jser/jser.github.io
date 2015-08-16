// LICENSE : MIT
"use strict";
import element from 'virtual-element'
export function render(component) {
    let {props, state, id} = component;
    return <a href={props.url} title={props.content}>{props.title}</a>
}
export default {
    render
}