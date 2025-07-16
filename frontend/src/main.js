// frontend/src/main.js

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios' // 引入 axios

// 配置 Axios 实例
// 这将是所有API请求的基础URL
// 在开发环境中，vue.config.js 的 proxy 会处理 /api 到后端的转发
// 在生产环境中，需要配置实际的后端地址
axios.defaults.baseURL = '/api';

const app = createApp(App)

app.use(router)
app.mount('#app')

// 将 axios 挂载到全局属性，方便组件内使用
app.config.globalProperties.$axios = axios;