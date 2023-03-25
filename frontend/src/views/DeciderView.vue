<template>
  <div class="decider"></div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { mapGetters } from "vuex";

export default defineComponent({
  name: "DeciderView",
  components: {},
  beforeCreate(): void {
    console.log("Deciding...");
    if (this.isAuthenticated) {
      console.log("Authenticated");
      this.$router.push({ name: "dashboard" });
    } else {
      console.log("Waiting for authentication");
      this.$router.push({ name: "login" });
    }
  },
  computed: {
    ...mapGetters(["isAuthenticated"]),
  },
});
</script>
