// MIT © 2017 azu
"use strict";
import {h, Component} from 'preact';
/**
 *
 * @param {JSerItem[]} items
 * @param {function(event)} onSelectedItem
 */
export default class SelectItemForm extends Component {
    constructor() {
        super();
        this.onChangeSelect = (event) => {
            const value = event.target.value;
            const selectedItem = this.props.items.find(item => {
                return item.url === value;
            });
            this.props.onSelectedItem(selectedItem);
        };
        this.onSubmit = (event) => {
            event.preventDefault();
        }
    }

    render() {
        const options = this.props.items.map(item => {
            return <option className="SelectItemForm-option" value={item.url}>{item.title}</option>
        });
        return <form onSubmit={this.onSubmit} className="SelectItemForm">
            <select name="SelectItem" onChange={this.onChangeSelect}>
                <option selected disabled>気になった記事を選んでください</option>
                {options}
            </select>
        </form>;
    }
};