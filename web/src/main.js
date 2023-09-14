// main.js

import { createApp } from 'vue';
import App from './App.vue'; 
import router from './router'; 

const app = createApp(App);
app.use(router); // Use the router plugin
app.mount('#app');



// import Vue from 'vue';
// import App from './App.vue';
// import router from './router';

// new Vue({
//   el: '#app',
//   router, // Inject the router into the Vue instance
//   render: (h) => h(App),
// });
