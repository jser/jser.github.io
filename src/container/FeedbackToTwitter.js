// MIT © 2017 azu
"use strict";
import {h, Component} from 'preact';
import SelectItemForm from "../component/SelectItemForm";
import TwitterButton from "../component/TwitterButton";
export default class FeedbackToTwitter extends Component {
    constructor() {
        super();
        this.state = {
            selectedItem: null
        };
        this.onSelectedItem = (selectedItem) => {
            this.setState({selectedItem});
        }
    }

    render() {
        const week = this.props.week;
        const selectedItem = this.state.selectedItem;
        if (!selectedItem) {
            return <div className="FeedbackToTwitter">
                <label>気になった記事を選んでTwitterに投稿する:</label>
                <SelectItemForm items={week.items} onSelectedItem={this.onSelectedItem}/>
                <TwitterButton text={document.title} url={location.url} via="jser_info"/>
            </div>
        }
        const title = `気になる: "${selectedItem.title}"`;
        return <div className="FeedbackToTwitter">
            <label>気になった記事を選んでTwitterに投稿する:</label>
            <SelectItemForm items={week.items} onSelectedItem={this.onSelectedItem}/>
            <TwitterButton text={title} url={selectedItem.url} via="jser_info"/>
        </div>
    }
}