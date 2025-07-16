<template>
  <div class="home">
    <h1>欢迎来到 DominiTrack</h1>
    <p>您的域名管理和提醒助手。</p>
    </div>
</template>

<script>
// import DomainList from '@/components/DomainList.vue'; // 未来会导入
export default {
  name: 'HomeView',
  components: {
    // DomainList // 未来会注册
  }
}
</script>

<style scoped>
.home {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}
</style>