<template>
  <div class="home">
    <!--<table class="table">
    
      <thead>
        <th>ID</th>
        <th>NAME</th>
        <th>CATEGORY</th>
        <th>PRICE</th>
        <th>UNIT</th>
        <th>AVAILABILITY</th>
        <th>SALE</th>
        <th>DISCOUNT</th>
        <th>COMMENTS</th>
        <th>OWNER</th>
      </thead>
    -->
    <table v-if="products > 0">
      <tr>
        <th v-for="title in Object.keys(products[0])" :key="title">
          {{ title }}
        </th>
      </tr>
      <tbody>
        <tr v-for="i in products" :key="i.id">
          <td v-for="x in Object.values(i)" :key="x + i.id">
            <RouterLink :to="'/product/' + i.id">
              {{ x }}
            </RouterLink>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      products: [],
    };
  },
  mounted() {
    fetch("http://127.0.0.1:8000/products/")
      .then((res) => res.json())
      .then((data) => (this.products = data))
      .catch((err) => console.log(err.message));
  },
};
</script>
