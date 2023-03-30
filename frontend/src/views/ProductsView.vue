<template>
  <div class="home">
    <AppBarView title="Produits" />
    <div class="bar">
      <TextField
        id="search_text_field"
        v-bind:onChange="filter"
        hint="Recherche"
      ></TextField>
      <FlatButton text="Créer un produit" :onTap="goToStock"></FlatButton>
      <FlatButton text="Gérer le Stock" :onTap="goToStock"></FlatButton>
    </div>
    <!-- FilterBar></FilterBar -->
    <TableView
      v-bind:products="filteredProducts"
      v-bind:keys="keys"
      v-bind:onSelect="onSelect"
      v-bind:selected="selected"
      v-bind:expandFields="expandFields"
    ></TableView>
  </div>
</template>

<script lang="ts">
import TableView from "../components/TableView.vue";
import TextField from "../components/TextField.vue";
import AppBarView from "../components/AppBar.vue";
import FlatButton from "../components/FlatButton.vue";
import { defineComponent } from "vue";
import { mapActions, mapGetters } from "vuex";
import { Product } from "@/types";

export default defineComponent({
  name: "ProductsView",
  components: {
    FlatButton,
    TextField,
    TableView,
    AppBarView,
  },
  data() {
    return {
      // keys: Object.keys(store.state.fishes[0]),
      keys: [] as string[],
      // products: [] as Product[],
      filteredProducts: [] as Product[],
      selected: {} as Product,
      expandFields: ["comments", "name"],
    };
  },
  computed: {
    ...mapGetters(["products"]),
  },
  methods: {
    ...mapActions(["fetchProducts"]),
    filter(term: string) {
      this.filteredProducts = this.products.filter((product: Product) => {
        return product.name.toLowerCase().includes(term.toLowerCase());
      });
    },
    onSelect(product: Product) {
      this.selected = product;
    },
    async goToStock() {
      return this.$router.push({ name: "stock" });
    },
  },
  mounted() {
    this.fetchProducts().then((products) => {
      this.filteredProducts = [];
      products.forEach((val: Product) => {
        this.filteredProducts.push(Object.assign({}, val));
      });
      // this.keys = Object.keys(products[0]);
      this.keys = [
        "id",
        "name",
        "price",
        "availability",
        "comments",
        "category",
        "owner",
        "discount",
      ];
    });
  },
});
</script>

<style>
.home {
  margin: 1%;
}

.home {
  align-items: start;
}

.bar {
  display: flex;
  flex-direction: row;
  justify-content: space-evenly;
}

#edit_flat_button {
  width: 60px;
  margin: none;
  text-align: center;
}

#search_text_field {
  width: 50%;
  margin: 10px auto;
}

table {
  width: auto;
}
</style>
