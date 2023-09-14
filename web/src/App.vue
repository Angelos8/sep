<!-- 
    TO RUN THIS APPLICATION:

    FISRT TIME
    cd web
    npm install vue-router@4
    npm install -g @vue/cli
    npm install @vue/cli-service --save-dev
    npm run serve

    ONWARDS
    cd web
    npm run serve
 -->

<!-- App.vue -->
<template>
    <div id="app">
      <router-link to="/">Search</router-link>
      <router-link to="/login">LoginSignup</router-link>
      <router-link to="/viewfile">ViewFile</router-link>
      <router-link to="/user">UserProfile</router-link>
      <router-link to="/admin">AdminProfile</router-link>
      <router-link to="/annotate">Annotator</router-link>
      <router-link to="/settings">Settings</router-link>
  
      <router-view></router-view>
    </div>
  </template>
  
  <script>
  export default {
    name: 'App',
  };
  </script>


<!-- Virtual script "/Users/emilymiller/Desktop/University/Operating Systems/a2/sep/web/src/App.vue.js" not found, may missing <script lang="ts"> / "allowJs": true / jsconfig.json. -->

<!-- OLD SETUP HERE FROM CHANGI
<script setup lang="ts">
</script>

<template></template>

<style scoped></style> -->
  