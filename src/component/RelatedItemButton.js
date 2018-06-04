// MIT © 2017 azu
"use strict";
import { h, Component } from 'preact';

export class RelatedItemButton extends Component {
    constructor() {
        super();
        this.onClickButton = () => {
            const nextIsOpen = !this.props.isOpen;
            if (nextIsOpen) {
                this.props.onOpen();
            } else {
                this.props.onClose();
            }
        };
    }

    render() {
        return <div class="RelatedItemAddition">
            {
                this.props.isOpen ? <button class="RelatedItemAddition--button"
                                            onClick={this.onClickButton}>▲関連記事を非表示</button>
                                  : <button class="RelatedItemAddition--button"
                                            onClick={this.onClickButton}>▼関連記事を表示</button>
            }
        </div>
    }
}
