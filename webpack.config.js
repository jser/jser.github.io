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
        // to avoid warning by power-assert-formatter
        exprContextCritical: false,
        loaders: [
            {
                test: /\.json$/,
                loader: "json-loader"
            },
            {
                test: /\.js$/,
                exclude: /node_modules/,
                loader: "babel",
                query: {
                    cacheDirectory: true
                }
            }
        ]
    }
};
