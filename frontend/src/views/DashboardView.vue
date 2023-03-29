<template>
  <div class="home">
    <AppBarView title="Dashboard" />
    <div class="content">
      <div class="subtitle">Bienvenue sur la page d'accueil</div>
      <StatsView />
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { mapActions } from "vuex";
import AppBarView from "@/components/AppBar.vue";
import StatsView from "@/components/Stats.vue";

export default defineComponent({
  name: "DashboardView",
  components: {
    AppBarView,
    StatsView,
  },
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

<style>
body {
  background-color: #f5f5fa;
}
</style>
