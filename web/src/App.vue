<template>
  <div id="app">
    <div class="common-layout">
      <el-container>
        <el-header>
          <el-menu
            :default-active="activeIndex"
            class="el-menu-demo"
            mode="horizontal"
            :ellipsis="false"
            router
          >
            <el-menu-item>Synergism</el-menu-item>
            <div class="flex-grow" />
            <el-menu-item index="/">首页</el-menu-item>
            <el-menu-item index="/graphic">图示</el-menu-item>
          </el-menu>
        </el-header>
        <el-main>
          <router-view></router-view>
        </el-main>
      </el-container>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';

export default defineComponent({
  name: 'App',
  setup: () => {
    const activeIndex = ref('/');

    return { activeIndex };
  },
  components: {}
});
</script>
