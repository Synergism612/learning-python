<template>
  <el-container>
    <el-aside width="200px">
      <h1>控制台</h1>
      <el-menu
        default-active="1"
        class="el-menu-vertical-demo"
        @select="handleSelect"
      >
        <el-sub-menu index="1">
          <template #title>
            <span>类型相关</span>
          </template>
          <el-menu-item index="1-1">词云</el-menu-item>
          <el-menu-item index="1-2">柱状图</el-menu-item>
        </el-sub-menu>
        <el-sub-menu index="2">
          <template #title>
            <span>年份相关</span>
          </template>
          <el-menu-item index="2-1">折线图</el-menu-item>
        </el-sub-menu>
        <el-sub-menu index="3">
          <template #title>
            <span>时长相关</span>
          </template>
          <el-menu-item index="3-1">柱状图</el-menu-item>
        </el-sub-menu>
        <el-sub-menu index="4">
          <template #title>
            <span>国家相关</span>
          </template>
          <el-menu-item index="4-1">饼图</el-menu-item>
        </el-sub-menu>
      </el-menu>
    </el-aside>
    <el-main>
      <div ref="chart" style="height: 600px"></div>
    </el-main>
  </el-container>
</template>

<script lang="ts">
import { ref, defineComponent, onMounted } from 'vue';
import * as echarts from 'echarts';
import 'echarts-wordcloud';

import { get } from '../axios/api';

interface key_value {
  key: string[];
  value: string[];
}

export default defineComponent({
  name: 'CutlineComponents',
  props: {},
  setup: () => {
    const chart = ref<HTMLDivElement>(document.createElement('div'));
    let myChart: echarts.ECharts | null = null;
    onMounted(() => {
      myChart = echarts.init(chart.value);
      typeWordCloud();
    });
    const typeWordCloud = () => {
      const option = {
        //指定图表的配置项和数据
        backgroundColor: 'rgba(128, 128, 128, 0.1)', //rgba设置透明度0.1
        title: {
          //配置标题组件
          text: '豆瓣TOP250类型分析',
          subtext: '数据截至2023年9月',
          x: 'center',
          y: 10,
          textStyle: {
            color: 'green',
            fontSize: 22
          }
        },
        tooltip: { show: true }, //配置提示框组件
        series: [
          {
            //数据系列及其配置
            name: '豆瓣TOP250类型分析', //设置名称
            type: 'wordCloud', //设置图表类型为字云图
            sizeRange: [40, 120], //设置数据大小范围
            textRotation: [0, 45, 90, 135, -45, -90], //设置文字倾斜角度
            gridSize: 20, //设置文字之间的间距
            autoSize: { enable: true, minSize: 5 }, //设置文字的自动大小
            textStyle: {
              normal: {
                color: function () {
                  return (
                    'rgb(' +
                    [
                      Math.round(Math.random() * 255),
                      Math.round(Math.random() * 255),
                      Math.round(Math.random() * 255)
                    ].join(',') +
                    ')'
                  );
                }
              },
              emphasis: {
                shadowBlur: 26,
                color: '#333',
                shadowColor: '#ccc',
                fontSize: 20
              }
            },
            data: [] //data结束
          }
        ] //series结束
      };
      get('/types/cloud')
        .then(res => {
          if (myChart) {
            myChart.clear();
            option.series[0].data = res as unknown as [];
            myChart.setOption(option);
          }
        })
        .catch(() => {
          console.log('错误');
        });
    };
    const typeCategory = () => {
      if (myChart) {
        myChart.clear();
        get('/types/category')
          .then(res => {
            console.log(res);
            if (myChart) {
              myChart.clear();
              const option = {
                title: {
                  //配置标题组件
                  text: '豆瓣TOP250类型分析',
                  subtext: '数据截至2023年9月',
                  x: 'center',
                  y: 10,
                  textStyle: {
                    color: 'green',
                    fontSize: 22
                  }
                },
                tooltip: {
                  trigger: 'axis',
                  axisPointer: {
                    type: 'shadow'
                  }
                },
                grid: {
                  left: '3%',
                  right: '4%',
                  bottom: '3%',
                  containLabel: true
                },
                xAxis: [
                  {
                    type: 'category',
                    data: (res as unknown as key_value).key,
                    axisTick: {
                      alignWithLabel: true
                    }
                  }
                ],
                yAxis: [
                  {
                    type: 'value'
                  }
                ],
                series: [
                  {
                    name: '数量',
                    type: 'bar',
                    barWidth: '60%',
                    data: (res as unknown as key_value).value
                  }
                ]
              };
              myChart.setOption(option);
            }
          })
          .catch(() => {
            console.log('错误');
          });
      }
    };
    const year = () => {
      if (myChart) {
        myChart.clear();
        get('/year')
          .then(res => {
            console.log(res);
            if (myChart) {
              myChart.clear();
              const option = {
                title: {
                  //配置标题组件
                  text: '豆瓣TOP250年份分析',
                  subtext: '数据截至2023年9月',
                  x: 'center',
                  y: 10,
                  textStyle: {
                    color: 'green',
                    fontSize: 22
                  }
                },
                tooltip: {
                  trigger: 'axis',
                  axisPointer: {
                    type: 'cross'
                  }
                },
                xAxis: {
                  type: 'category',
                  boundaryGap: false,
                  // prettier-ignore
                  data: (res as unknown as key_value).key
                },
                yAxis: {
                  type: 'value',
                  axisLabel: {
                    formatter: '{value} '
                  },
                  axisPointer: {
                    snap: true
                  }
                },
                series: [
                  {
                    name: '数量',
                    type: 'line',
                    smooth: true,
                    // prettier-ignore
                    data: (res as unknown as key_value).value
                  }
                ]
              };

              myChart.setOption(option);
            }
          })
          .catch(() => {
            console.log('错误');
          });
      }
    };
    const duration = () => {
      if (myChart) {
        myChart.clear();
        get('/duration')
          .then(res => {
            console.log(res);
            if (myChart) {
              myChart.clear();
              const option = {
                title: {
                  //配置标题组件
                  text: '豆瓣TOP250时长分析',
                  subtext: '数据截至2023年9月',
                  x: 'center',
                  y: 10,
                  textStyle: {
                    color: 'green',
                    fontSize: 22
                  }
                },
                tooltip: {
                  trigger: 'axis',
                  axisPointer: {
                    type: 'shadow'
                  }
                },
                grid: {
                  left: '3%',
                  right: '4%',
                  bottom: '3%',
                  containLabel: true
                },
                xAxis: [
                  {
                    type: 'category',
                    data: (res as unknown as key_value).key,
                    axisTick: {
                      alignWithLabel: true
                    }
                  }
                ],
                yAxis: [
                  {
                    type: 'value'
                  }
                ],
                series: [
                  {
                    name: '数量',
                    type: 'bar',
                    barWidth: '60%',
                    data: (res as unknown as key_value).value
                  }
                ]
              };

              myChart.setOption(option);
            }
          })
          .catch(() => {
            console.log('错误');
          });
      }
    };
    const country = () => {
      if (myChart) {
        myChart.clear();
        get('/country')
          .then(res => {
            console.log(res);
            if (myChart) {
              myChart.clear();
              const option = {
                title: {
                  //配置标题组件
                  text: '豆瓣TOP250国别分析',
                  subtext: '数据截至2023年9月',
                  x: 'center',
                  y: 10,
                  textStyle: {
                    color: 'green',
                    fontSize: 22
                  }
                },
                tooltip: {
                  trigger: 'item'
                },
                legend: {
                  orient: 'vertical',
                  left: 'left'
                },
                series: [
                  {
                    name: '国别',
                    type: 'pie',
                    radius: '50%',
                    data: res,
                    emphasis: {
                      itemStyle: {
                        shadowBlur: 10,
                        shadowOffsetX: 0,
                        shadowColor: 'rgba(0, 0, 0, 0.5)'
                      }
                    }
                  }
                ]
              };

              myChart.setOption(option);
            }
          })
          .catch(() => {
            console.log('错误');
          });
      }
    };
    const handleSelect = (index: string) => {
      switch (index) {
        case '1-1':
          typeWordCloud();
          break;
        case '1-2':
          typeCategory();
          break;
        case '2-1':
          year();
          break;
        case '3-1':
          duration();
          break;

        case '4-1':
          country();
          break;

        default:
          break;
      }
    };
    return { chart, handleSelect };
  },
  components: {}
});
</script>

<style scoped>
.demo-tabs {
  width: 100%;
}
</style>
