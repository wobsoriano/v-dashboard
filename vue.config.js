const devPort = 3000;
module.exports = {
  devServer: {
    host: '0.0.0.0',
    public: `0.0.0.0:${devPort}`,
    port: devPort,
    disableHostCheck: true,
    proxy: {
      '/api': {
        target: 'http://localhost:5000',
        changeOrigin: true,
        pathRewrite: { '^/api': '' }
      }
    }
  }
}
