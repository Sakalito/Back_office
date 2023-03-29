<template>
  <meta charset="UTF-8" />
  <!--<title> Responsive Sidebar Menu  | CodingLab </title>-->
  <!-- Boxicons CDN Link -->
  <link
    href="https://unpkg.com/boxicons@2.0.7/css/boxicons.min.css"
    rel="stylesheet"
  />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />

  <div class="parent">
    <header>
      <nav>
        <ul>
          <li><router-link to="/">Home</router-link></li>
          <li><router-link to="/products">Produit</router-link></li>
          <li><router-link to="/about">À propos</router-link></li>
        </ul>
      </nav>
    </header>
    <section class="parent">
      <div class="glass">
        <img src="" />
      </div>
      <div class="glass">
        <h1>{{ product }}</h1>
        <h1>{{ product.name }}</h1>
        <p>{{ product.price }}€</p>
        <br />
        <div style="text-align: center">
          <h2>Modification du stock</h2>
          <input style="display: block; margin: auto" type="text" />
          <button>Ajouter</button>
          <button>Supprimer</button>
        </div>

        <br />
        <br />

        <div style="text-align: center">
          <h2>Gestion de la promotion</h2>
          <input type="text" style="display: block; margin: auto" />
          <button>Enregistrer</button>
        </div>
        <br />
        <br />
        <p>
          {{ product.description }}
        </p>
      </div>
    </section>
  </div>
</template>

<style>
<style > .home {
  font-family: Arial, sans-serif;
  color: #333;
  margin: 0;
  padding: 0;
}

header {
  top: 0;
  position: sticky;
  min-height: 50px;
  background: hwb(190 5% 13% / 0.927);
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 20px;
}

nav ul {
  display: flex;
  list-style-type: none;
}

nav li {
  margin-right: 20px;
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

<script>
import { URLSearchParams } from "url";
import { reactive, onMounted } from "vue";

export default {
  props: ["id"],

  name: "ProductPage",
  data() {
    return {
      products: [],
      product: [],
      ID: Number(this.$router.currentRoute.value.params.id),
      images: [],
    };
  },

  mounted() {
    // Load product details from API using $route.params.id
    fetch("http://127.0.0.1:8000/products/")
      .then((res) => res.json())
      .then((data) => {
        this.products = data;
        this.product = data.find((item) => item.id === this.ID);
      })
      .catch((err) => console.log(err.message));
  },
};
</script>
