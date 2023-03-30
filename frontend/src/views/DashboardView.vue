<template>
  <div class="home">
    <header>
      <nav>
        <ul>
          <li>
            <router-link to="/" style="color: black"
              >Tableau de bord</router-link
            >
          </li>
          <li>
            <router-link to="/products" style="color: black"
              >Liste des produits</router-link
            >
          </li>
        </ul>
      </nav>
    </header>
    <h1>Tableau de bord</h1>
  </div>
</template>

<style>
.home {
  font-family: Arial, sans-serif;
  color: #333;
  margin: 0;
  padding: 0;
}

header {
  top: 0;
  position: sticky;
  min-height: 50px;
  background: white;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 20px;
}

.navigation {
  color: black;
}

nav ul {
  display: flex;
  list-style-type: none;
}

nav li {
  margin-right: 20px;
  color: black;
}

nav li:last-child {
  margin-right: 0;
}

nav a {
  color: #fff;
  text-decoration: none;
  font-size: 18px;
}

nav a:hover {
  text-decoration: underline;
}

main {
  padding: 20px;
}

h1 {
  font-size: 24px;
  margin-bottom: 20px;
}

.card-list {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  grid-gap: 20px;
}

body {
  height: 100vh;
  margin: 0;
  padding: 0;
  font-family: helvetica;
}

#app {
  height: 100%;
}

.card-list {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
}

.card {
  background-color: #ffffff;
  border-radius: 0.5rem;
  box-shadow: 0 0 0.5rem rgba(0, 0, 0, 0.1);
  margin-bottom: 1rem;
  width: calc(33.33% - 1rem);
}

.card-body {
  padding: 1rem;
}

.card-title {
  font-size: 1.5rem;
  margin-bottom: 0.5rem;
}

.card-text {
  font-size: 1rem;
  margin-bottom: 0.5rem;
}

p {
  margin: 0;
}
</style>
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
