<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { mapActions } from "vuex";

export default defineComponent({
  name: "DashboardView",
  components: {},
  async created(): Promise<void> {
    console.log("Redeciding...");
    if (!(await this.isAuthenticated())) {
      console.log("Waiting for authentication");
      this.$router.push({ name: "login" });
    }
    console.log("Authenticated");
  },
  methods: {
    ...mapActions(["isAuthenticated"]),
  },
});
</script>
