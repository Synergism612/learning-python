<template>
  <el-table
    :data="tableData"
    style="width: 100%"
    stripe
    size="small"
  >
    <el-table-column prop="id" label="排名" />
    <el-table-column fixed prop="movie" label="电影名" width="250" />
    <el-table-column prop="year" label="年份" />
    <el-table-column prop="directors" label="导演" />
    <el-table-column prop="types" label="类型" />
    <el-table-column prop="grade" label="评分" />
    <el-table-column prop="votes" label="评分人数" />
    <el-table-column fixed="right" label="简介" width="120">
      <template #default="scope">
        <el-button
          link
          type="primary"
          size="small"
          @click="click(scope.row.summary)"
        >
          查看
        </el-button>
      </template>
    </el-table-column>
  </el-table>
  <div class="example-pagination-block">
    <el-pagination
      layout="prev, pager, next"
      :total="total"
      @current-change="change"
    />
  </div>
  <el-drawer v-model="drawer" title="简介" :with-header="true">
    <br />
    <span style="font-size: 20px">{{ data }}</span>
  </el-drawer>
</template>

<script lang="ts">
import { defineComponent, onMounted, ref } from 'vue';
import { get } from '../axios/api';

interface DataType {
  total: number;
  data: TableType[];
}

interface TableType {
  id: string;
  movie: string;
  year: string;
  directors: string;
  types: string;
  grade: string;
  votes: string;
  summary: string;
}

export default defineComponent({
  name: 'CutlineComponents',
  props: {},
  setup: () => {
    const drawer = ref(false);
    const data = ref<string>('');
    const total = ref(1);
    const tableData = ref<TableType[]>([
      {
        id: '1',
        movie: '2',
        year: '3',
        directors: '',
        types: '',
        grade: '',
        votes: '',
        summary: ''
      }
    ]);
    onMounted(() => {
      getData(1);
    });
    const getData = (n: number) => {
      get('/all/' + n)
        .then(res => {
          tableData.value = (res as unknown as DataType).data;
          total.value = (res as unknown as DataType).total;
        })
        .catch(() => {
          console.log('错误');
        });
    };
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    const click = (summary: string) => {
      data.value = summary;
      drawer.value = true;
    };
    const change = (value: number) => {
      getData(value);
    };
    return { total, drawer, tableData, click, data, change };
  },
  components: {}
});
</script>

<style scoped>
.demo-tabs {
  width: 100%;
}
</style>
