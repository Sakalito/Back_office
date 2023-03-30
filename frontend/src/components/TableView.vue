<template>
  <table id="v-for-object">
    <thead>
      <tr>
        <th
          scope="col"
          v-for="key in keys"
          v-bind:key="key"
          :class="{ action_td: key == 'action' }"
        >
          {{ key }}
        </th>
        <th class="action_td">action</th>
      </tr>
    </thead>
    <tbody>
      <tr
        v-for="product in products"
        v-bind:key="product.id"
        :class="{ selected: product.id == selected?.id }"
        v-on:click="($event) => (onSelect ? onSelect(product) : null)"
      >
        <ProductTile
          v-bind:keys="keys"
          v-bind:product="product"
          v-bind:mayExpand="(key: any) => expandFields.includes(key)"
        ></ProductTile>
      </tr>
    </tbody>
  </table>
  <div class="end_table">{{ products.length }} poissons.</div>
</template>

<script lang="ts">
import ProductTile from "../components/ProductTile.vue";
import { defineComponent, PropType } from "vue";
import { Product } from "@/types";

export default defineComponent({
  name: "TableView",
  components: {
    ProductTile,
  },
  props: {
    products: {
      type: Object as PropType<Product[]>,
      required: true,
    },
    keys: {
      type: Array as PropType<string[]>,
      required: true,
    },
    onSelect: {
      type: Function as PropType<(product: Product) => void>,
      required: false,
    },
    selected: {
      type: Object as PropType<Product>,
      required: false,
    },
    expandFields: {
      type: Array as PropType<string[]>,
      required: false,
      default: [] as string[],
    },
  },
  methods: {},
});
</script>

<style>
.end_table {
  padding: 0.5% 0.5%;
}

th {
  text-align: start;
  padding: 10px;
}

td {
  padding: 0 10px;
  border-top: 1px solid #d4dfe0;
  white-space: nowrap;
}

.action_td {
  text-align: center;
  width: 60px;
}

tr:hover {
  background-color: #f5f5f5;
}

thead > tr:hover {
  background-color: transparent;
  border-radius: 12.5px;
}

.selected {
  background-color: #f5f5f5;
}

table {
  table-layout: fixed;
  background-color: white;
  border-spacing: 0;
  border: 1px solid #d4dfe0;
  border-radius: 12.5px;
}
</style>
