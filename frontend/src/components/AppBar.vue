<template>
  <header>
    <nav>
      <ul>
        <li>
          <router-link to="/dashboard">Dashboard</router-link>
        </li>
        <li><router-link to="/products">Produit</router-link></li>
      </ul>
    </nav>
  </header>
</template>

<script lang="ts">
import { PropType, defineComponent } from "vue";

type Nav = {
  text: string;
  route: string;
};

export default defineComponent({
  name: "AppBarView",
  props: {
    title: {
      type: String,
      required: true,
    },
    navs: {
      type: Array as PropType<Nav[]>,
      required: false,
      default: [
        {
          text: "Dashboard",
          route: "dashboard",
        },
        {
          text: "Produits",
          route: "products",
        },
      ] as Nav[],
    },
  },
  components: {},
  methods: {},
});
</script>

<style>
.app_bar {
  display: flex;
  flex-direction: row;
}

header {
  top: 0;
  position: sticky;
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #f5f5fa;
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
</style>
