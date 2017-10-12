const path = require('path')

module.exports = {
  entry: './src/index.js',
  output: {
    path: path.join(__dirname, 'dist'),
    filename: 'app.js'
  },
  devServer: {
    port: 9000,
    contentBase: path.join(__dirname, 'dist')
  },
  module: {
    rules: [
      { test: /\.js$/, exclude: /(node_modules)/, use: { loader: 'babel-loader' } }
    ]
  }
}
