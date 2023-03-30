<template>
  <div>
    <h3>Detail Produit</h3>
    <div class="detail-wrapper">
      <div v-if="data.id" class="container detail">
        <div v-if="data.images" class="prod_images">
          <img
            v-for="image of data.images"
            :key="image"
            :src="imageUrl(image)"
            alt="product"
          />
        </div>

        <div class="line">
          <span class="field"> Nom: </span>
          <span class="value">
            <TextFieldView
              :onChange="updateName"
              hint="Nom"
              :value="data.name"
            />
          </span>
        </div>

        <div class="line">
          <span class="field"> Prix: </span>
          <span class="value">
            <TextFieldView
              :onChange="(value) => updatePrice(parseFloat(value))"
              hint="Price"
              :value="data.price?.toString()"
            />
          </span>
        </div>

        <div class="line">
          <span class="field"> Commentaires: </span>
          <span class="value">
            <TextFieldView
              :onChange="updateComments"
              hint="Commentaires"
              :value="data.comments"
            />
          </span>
        </div>

        <div class="line">
          <span class="field"> Categorie: </span>
          <span class="value">
            <select v-model="category" @change="updateCategory(category)">
              <option value="Poisson">Poisson</option>
              <option value="Crustassé">Crustassé</option>
              <option value="Coquillage">Coquillage</option>
            </select>
          </span>
        </div>

        <div class="line">
          <span class="field"> Disponible: </span>
          <span class="value">
            <input
              type="checkbox"
              v-model="availability"
              @change="updateAvailability(availability)"
            />
          </span>
        </div>
      </div>
      <FlatButton v-if="data.id" text="Enregistrer" :onTap="update" />
    </div>
  </div>
  <div
    class="error container"
    :class="{ toast: error.length > 0 }"
    v-if="error"
  >
    {{ error }}
  </div>
</template>

<script lang="ts">
import { Product, Result } from "@/types";
import { defineComponent } from "vue";
import { useRoute } from "vue-router";
import { mapActions } from "vuex";
import TextFieldView from "../components/TextField.vue";
import endPoints from "@/ressources/constants";
import FlatButton from "../components/FlatButton.vue";

export default defineComponent({
  name: "ProductDetails",
  components: {
    TextFieldView,
    FlatButton,
  },
  async created(): Promise<void> {
    console.log("Deciding...", this.isAuthenticated());
    await this.verifyAuthentication();
  },
  mounted() {
    this.fetchProduct();
  },
  data() {
    return {
      product: {} as Product,
      // declare partial product
      data: {
        id: 0,
        name: "",
        comments: "",
        price: 0,
        images: [] as string[],
        category: "",
        discount: undefined,
      } as Partial<Product>,
      error: "",
      category: "",
      availability: false,
    };
  },
  methods: {
    imageUrl(image: string) {
      return `${endPoints.renderedImage}${image}`;
    },
    updateComments(comments: string) {
      this.data.comments = comments;
      console.log("Comments: ", comments);
    },
    updateName(name: string) {
      this.data.name = name;
      console.log("Name: ", name);
    },
    updatePrice(price: number) {
      this.data.price = price;
      console.log("Price: ", price);
    },
    updateImages(images: string[]) {
      this.data.images = images;
    },
    updateCategory(category: string) {
      this.data.category = category;
      console.log("Category: ", category);
    },
    updateAvailability(availability: boolean) {
      this.data.availability = availability;
      console.log("Availability: ", availability);
    },
    async update() {
      return this.$store
        .dispatch("updateProduct", this.data)
        .then((result: Result) => {
          if (result.state) {
            this.$router.push({ name: "products" });
          } else {
            this.error = result.message;
          }
        });
    },
    fetchProduct() {
      let route = useRoute();
      return this.$store
        .dispatch("getProduct", route.params.id)
        .then((product: Product | undefined) => {
          if (product) {
            this.data = Object.assign({}, product);
            console.log("Data: ", this.data);
            this.category = product.category;
            console.log("Category: ", this.category);
            this.availability = product.availability;
            this.product = product ?? ({} as Product);
          } else {
            this.$router.push({ name: "products" });
          }
        });
    },
    ...mapActions(["isAuthenticated"]),
    async verifyAuthentication() {
      console.log("Verifying authentication");
      if (await this.isAuthenticated()) {
        console.log("Authenticated");
      } else {
        console.log("Waiting for authentication");
        this.$router.push({ name: "login" });
      }
    },
  },
});
</script>

<style>
.detail-wrapper {
  align-content: center;
  align-items: center;
  display: block;
}
.detail {
  padding: 20px;
  padding-bottom: 5px;
}
.line {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  padding: 10px;
  margin: 15px 0;
  background: #f5f5fa;
  border-radius: 7px;
}
.field {
  font-weight: bold;
}
.prod_images {
  display: flexbox;
  flex-direction: row;
  justify-content: space-between;
}
.prod_images img {
  height: 125px;
  border-radius: 10px;
  padding: 5px;
}
</style>
