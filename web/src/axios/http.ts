import axios, {
  AxiosInstance,
  AxiosResponse,
  InternalAxiosRequestConfig
} from 'axios';
const axiosInstance: AxiosInstance = axios.create({
  baseURL: 'http://127.0.0.1:5000',
  timeout: 5000
});
// 添加请求拦截器
axiosInstance.interceptors.request.use(
  (config: InternalAxiosRequestConfig) => {
    // 在发送请求之前做些什么
    return config;
  },
  () => {
    // 处理请求错误
    return null;
  }
);
// 添加响应拦截器
axiosInstance.interceptors.response.use(
  (response: AxiosResponse) => {
    // 对响应数据做点什么
    return response;
  },
  () => {
    // 处理响应错误
    return null;
  }
);
export default axiosInstance;
