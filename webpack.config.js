// webpack.config.js
const path = require('path');

module.exports = {
  entry: './index.tsx',
  mode: 'development',
  output: {
    filename: 'static/main.js',
    path: path.resolve(__dirname, './'),
  },
  module: {
    rules: [
      {
        test: /\.(ts|tsx)?$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
        },
      },
    ],
  },
};
