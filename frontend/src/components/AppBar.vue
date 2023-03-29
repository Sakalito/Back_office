<template>
  <div class="app_bar">
    <h2 class="title">{{ title }}</h2>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "AppBarView",
  props: {
    title: {
      type: String,
      required: true,
    },
  },
  components: {},
  methods: {},
});
</script>

<style>
.app_bar {
}
</style>
