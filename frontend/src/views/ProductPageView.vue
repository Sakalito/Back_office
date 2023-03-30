<template>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <header>
    <nav>
      <ul>
        <li>
          <router-link to="/" style="color: black">Tableau de bord</router-link>
        </li>
        <li>
          <router-link to="/products" style="color: black"
            >Liste des produits</router-link
          >
        </li>
      </ul>
    </nav>
  </header>
  <div class="body">
    <h1 style="text-align: left">{{ product.category }}</h1>
    <h1 style="text-align: left">{{ product.name }}</h1>
    <h3 style="text-align: left">Prix : {{ product.price }}€</h3>
    <h3 style="text-align: left">
      Nombre d'articles disponible : {{ product.unit }}
    </h3>
    <h2 style="text-align: left">Modification du stock</h2>
    <input style="text-align: left" type="text" />
    <div class="stock">
      <button @click="addProduct(product.id)">Ajouter</button>
      <button @click="removeProduct(product.id)">Supprimer</button>
    </div>
    <h2 style="text-align: justify">Gestion de la promotion</h2>
    <input type="text" />
    <button class="save">Enregistrer</button>
    <h3 style="text-align: left">Commentaires:</h3>
    <p style="text-align: left">{{ product.comments }}</p>
  </div>
</template>

<script>
import { URLSearchParams } from "url";
import { reactive, onMounted, defineComponent } from "vue";

export default defineComponent({
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
    fetch("http://127.0.0.1:8000/products/")
      .then((res) => res.json())
      .then((data) => {
        this.products = data;
        this.product = data.find((item) => item.id === this.ID);
      })
      .catch((err) => console.log(err.message));
    fetch("http://127.0.0.1:8000/product/" + this.product.id);
  },
});
</script>

<style>
.body {
  background: white;
}
button {
  cursor: pointer;
  outline: 0;
  color: #fff;
  background-color: #0d6efd;
  border-color: #0d6efd;
  display: inline-block;
  font-weight: 400;
  line-height: 1.5;
  text-align: center;
  border: 1px solid transparent;
  padding: 6px 12px;
  font-size: 16px;
  border-radius: 0.25rem;
  transition: color 0.15s ease-in-out, background-color 0.15s ease-in-out,
    border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
}

button:hover {
  color: #fff;
  background-color: #0b5ed7;
  border-color: #0a58ca;
}

.stock {
  display: flex;
}

.save {
  display: flex;
}
</style>
