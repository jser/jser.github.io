// MIT © 2017 azu
"use strict";
import { h, Component } from 'preact';
import { getStat } from "../utils/get-stats";
import { RelatedItemList } from "./RelatedItemList";
import { RelatedItemButton } from "./RelatedItemButton.js";

export default class RelatedItemBox extends Component {
    constructor() {
        super();
        this.state = {
            isOpen: false,
            isLoading: false,
            items: []
        };
        this.hasItems = () => this.state.items.length > 0;
        this.onOpen = () => {
            this.setState({
                isOpen: true
            });
            if (this.hasItems()) {
                return;
            }
            this.setState({
                isLoading: true
            });
            // display loading -> get data
            setTimeout(() => {
                const url = this.props.URL;
                getStat().then((stat) => {

                    var jSerItem = stat.findItemWithURL(url);
                    var relatedItems = stat.findRelatedItems(jSerItem);
                    return relatedItems.map(function(item) {
                        var week = stat.findWeekWithItem(item);
                        // 未来の記事候補の場合はまだ該当するweekはない
                        if (week == null) {
                            return null;
                        }
                        return {
                            item: item,
                            post: week.post
                        };
                    }).filter(object => object != null);// 空はfilter
                }).then((postWithItems) => {
                    this.setState({
                        items: postWithItems,
                        isLoading: false
                    });
                }).catch(error => {
                    console.error(error);
                });
            }, 100);
        };

        this.onClose = () => {
            this.setState({
                isOpen: false
            });
        }
    }


    render() {
        if (this.state.isLoading) {
            return <div className="RelatedItemBox">
                <RelatedItemButton isOpen={this.state.isOpen} onOpen={this.onOpen} onClose={this.onClose}/>
                <p>Loading...</p>
            </div>;
        }
        if (this.state.isOpen && this.hasItems()) {
            return <div className="RelatedItemBox">
                <RelatedItemButton isOpen={this.state.isOpen} onOpen={this.onOpen} onClose={this.onClose}/>
                <RelatedItemList postWithItems={this.state.items}/>
            </div>
        } else {
            return <div className="RelatedItemBox">
                <RelatedItemButton isOpen={this.state.isOpen} onOpen={this.onOpen} onClose={this.onClose}/>
            </div>
        }
    }
}
