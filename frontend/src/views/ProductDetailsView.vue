<template>
  <div>
    <AppBarView title="Detail Produit" />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { mapActions } from "vuex";
import AppBarView from "@/components/AppBar.vue";

export default defineComponent({
  name: "ProductDetails",
  components: {
    AppBarView,
  },
  async created(): Promise<void> {
    console.log("Deciding...", this.isAuthenticated());
    await this.verifyAuthentication();
  },
  computed: {
    product() {
      return this.$store.dispatch("getProduct", this.$route.params.id);
    },
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

<style></style>
