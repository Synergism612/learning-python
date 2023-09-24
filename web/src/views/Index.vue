<template>
  <div class="common-layout">
    <el-container>
      <el-aside width="200px">
        <h1>控制台</h1>
        <el-menu
          default-active="2"
          class="el-menu-vertical-demo"
          @open="handleOpen"
          @close="handleClose"
        >
          <el-menu-item index="1">
            <span>Navigator Two</span>
          </el-menu-item>
        </el-menu>
      </el-aside>
      <el-main>
        <div ref="chart" style="height: 600px"></div>
      </el-main>
    </el-container>
  </div>
</template>

<script lang="ts">
import { ref, defineComponent, onMounted } from 'vue';
import * as echarts from 'echarts';

export default defineComponent({
  name: 'IndexView',
  props: {},
  setup: () => {
    const chart = ref(null);
    onMounted(() => {
      const myChart = echarts.init(chart.value);
      const option = {
        title: {
          text: 'ECharts 入门示例'
        },
        tooltip: {},
        legend: {
          data: ['销量']
        },
        xAxis: {
          data: ['衬衫', '羊毛衫', '雪纺衫', '裤子', '高跟鞋', '袜子'] // 你需要的数据
        },
        yAxis: {},
        series: [
          {
            name: '销量',
            type: 'bar',
            data: [5, 20, 36, 10, 10, 20] // 你需要的数据
          }
        ]
      };
      myChart.setOption(option);
    });
    const handleOpen = (key: string, keyPath: string[]) => {
      console.log(key, keyPath);
    };
    const handleClose = (key: string, keyPath: string[]) => {
      console.log(key, keyPath);
    };
    return { chart, handleOpen, handleClose };
  },
  components: {}
});
</script>

<style scoped></style>
