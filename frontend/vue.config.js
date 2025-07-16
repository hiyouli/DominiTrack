// frontend/vue.config.js

module.exports = {
  devServer: {
    proxy: {
      '/api': { // 当前端请求以 /api 开头时
        target: 'http://backend:8000', // 转发到后端 Docker 容器的地址
        changeOrigin: true, // 改变源，使其看起来像是从后端发出的请求
        ws: true, // 启用 websocket 代理
        pathRewrite: { '^/api': '' } // 重写路径，将 /api 去掉再转发
      }
    },
    // 确保开发服务器在容器内可以通过 0.0.0.0 访问
    host: '0.0.0.0',
    port: 8080, // 确保与 docker-compose.yml 中定义的端口一致
    client: {
      webSocketURL: 'ws://0.0.0.0:8080/ws', // Vue CLI 5.x 及更高版本
    },
    allowedHosts: ['all'], // 允许所有主机访问
  }
};