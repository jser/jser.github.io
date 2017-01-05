const path = require("path");

module.exports = {
    entry: {
        "related-item": "./src/related-item.js"
    },
    devtool: process.env.WEBPACK_DEVTOOL || "source-map",
    output: {
        path: path.join(__dirname, "public", "build"),
        publicPath: "/build/",
        filename: "[name].js"
    },
    node: {
        fs: "empty"
    },
    module: {
        loaders: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                loader: "babel-loader",
                query: {
                    cacheDirectory: true
                }
            }
        ]
    },
    performance: {hints: false}
};
