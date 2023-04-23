const path = require("path");
const glob = require('glob');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const devMode = process.env.NODE_ENV !== "production";

module.exports = {
  entry: glob.sync(
    path.resolve(__dirname, "./front/js/*.js")
  ).reduce(function (obj, el) {
    obj[path.parse(el).name] = el;
    return obj
  }, {}),
  output: {
    filename: "js/[name].js",
    path: path.resolve(__dirname, "./static/build"),
  },
  optimization: {
    moduleIds: 'deterministic', //Added this to retain hash of vendor chunks. 
    runtimeChunk: 'single',
    splitChunks: {
      cacheGroups: {
        vendor: {
          test: /[\\/]node_modules[\\/]/,
          name: 'vendors',
          chunks: 'all',
        },
      },
    },
    minimize: true,
  },
  plugins: [
    new MiniCssExtractPlugin({
      filename: "css/[name].css",
    }),
  ],
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: ["babel-loader"],
      },
      {
        test: /\.(sc|sa|c)ss$/i,
        use: [
          // devMode ? "style-loader" : MiniCssExtractPlugin.loader,
          MiniCssExtractPlugin.loader,
          {
            loader: "css-loader",
            options: {
              sourceMap: true,
              importLoaders: 1
            }
          },
          'postcss-loader',
          {
            loader: 'sass-loader',
            options: {
              sourceMap: true,
              implementation: require("sass"),
            }
          },
        ]
      },
    ],
  },
  resolve: {
    extensions: ["*", ".js", ".jsx"],
  }
};