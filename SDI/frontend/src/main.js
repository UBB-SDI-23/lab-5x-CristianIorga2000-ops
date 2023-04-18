import { createApp } from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import { loadFonts } from './plugins/webfontloader'
import axios from "axios";

axios.defaults.baseURL = "http://http://35.228.0.43/";
loadFonts()

createApp(App)
  .use(vuetify)
  .mount('#app')
