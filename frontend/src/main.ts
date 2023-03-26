import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import Toasted from "vue-toasted";

createApp(App).use(Toasted).use(store).use(router).mount("#app");
