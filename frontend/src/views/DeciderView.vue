<template>
  <div class="decider"></div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { mapActions, mapGetters } from "vuex";

export default defineComponent({
  name: "DeciderView",
  components: {},
  async created(): Promise<void> {
    console.log("Deciding...", this.isAuthenticated());
    await this.verifyAuthentication();
  },
  methods: {
    ...mapActions(["isAuthenticated"]),
    async verifyAuthentication() {
      console.log("Verifying authentication");
      if (await this.isAuthenticated()) {
        console.log("Authenticated");
        this.$router.push({ name: "dashboard" });
      } else {
        console.log("Waiting for authentication");
        this.$router.push({ name: "login" });
      }
    },
  },
});
</script>
