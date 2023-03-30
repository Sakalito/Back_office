<template>
  <td v-for="key in keys" v-bind:key="key" :class="{ expand: mayExpand(key) }">
    <span
      v-if="typeof get(key) == 'boolean'"
      class="badge"
      :class="{ good: get(key), bad: !get(key) }"
    >
      {{ get(key) }}
    </span>
    <span v-else>
      {{ get(key) }}
    </span>
  </td>
  <td class="action_td">
    <FlatButton :onTap="goToEdit" text="Editer" />
  </td>
</template>

<script lang="ts">
import { Product } from "@/types";
import { defineComponent, PropType } from "vue";
import FlatButton from "./FlatButton.vue";

export default defineComponent({
  name: "ProductTile",
  components: {
    FlatButton,
  },
  props: {
    keys: { type: Object as PropType<string[]>, requiered: true },
    product: { type: Object as PropType<Product>, requiered: true },
    mayExpand: {
      type: Function as PropType<(key: string) => boolean>,
      requiered: false,
      default: () => false,
    },
  },
  methods: {
    // : string | number | boolean
    get(key: string) {
      let field = this.product![key as keyof Product];
      return field;
    },
    async goToEdit() {
      console.log("go to edit");
      return this.$router.push({
        name: "edit",
        params: { id: this.product?.id },
      });
    },
  },
});
</script>

<style>
.fish_tile {
  display: inline-flex;
}

.badge {
  border-radius: 7.5px;
  text-align: center;
  padding-left: 7.5px;
  padding-top: 5px;
  padding-bottom: 2px;
  padding-right: 6px;
}

.bad {
  background-color: #f0e0cb;
}

.good {
  background-color: #c7eee5;
}

.expand {
  width: 30%;
}

.Editer {
  margin: 45%;
}

td {
  text-align: start;
}
</style>
