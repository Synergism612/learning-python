import { createApp } from 'vue';
import App from './App.vue';
import dayjs from 'dayjs';
import 'dayjs/locale/zh-cn';
import { setupStore } from '@/stores';
import './styles/index.scss';
import router from './router';
import ElementPlus from 'element-plus';
import 'element-plus/dist/index.css';

const app = createApp(App);

dayjs.locale('zh-ch');
setupStore(app);
app.use(ElementPlus);
app.use(router);
app.mount('#app');
