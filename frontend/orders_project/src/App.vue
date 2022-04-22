<template>
  <div id="app">
    <custom-header />
    <router-view />
  </div>
</template>

<script>
import customHeader from "./components/custom-header.vue";

// @ is an alias to /src

export default {
  components: {
    customHeader,
  },
};
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
a {
  text-decoration: none;
  color: black;
}
</style>
