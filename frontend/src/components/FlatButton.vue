<template>
  <span
    class="flat_button"
    :class="{
      reacting: loading,
      elevated: elevate,
    }"
    @click="react"
  >
    <div v-if="loading" class="loading">
      <LottieAnimation
        :path="animationPath"
        :autoplay="true"
        :loop="true"
        :height="20"
      />
    </div>
    <span v-else>
      {{ text }}
    </span>
  </span>
</template>

<script lang="ts">
import { defineComponent, PropType } from "vue";
import LottieAnimation from "lottie-vuejs/src/LottieAnimation.vue";

export type OnTapFunction = () => Promise<any>;

export default defineComponent({
  name: "FlatButton",
  components: {
    LottieAnimation,
  },
  props: {
    onTap: { type: Function as PropType<OnTapFunction>, required: true },
    text: { type: String, required: true },
    elevate: { type: Boolean, default: true, required: false },
  },
  data() {
    return {
      loading: false,
      animationPath: "lotties/loading-dots.json",
    };
  },
  methods: {
    react() {
      if (this.loading) {
        console.log("Already reacting");
        return;
      } else {
        console.log("reacting");
        this.loading = true;
        this.onTap().then(() => {
          this.loading = false;
        });
      }
    },
  },
});
</script>

<style>
.flat_button {
  cursor: pointer;
  color: #fff;
  background-color: #7070ff;
  width: 250px;
  padding: 10px 15px;
  border-radius: 10px;
  margin: 10px 5px;
  display: block;
}

.flat_button:hover {
  color: #7070ff;
  background-color: #fff;
  border: 1px solid #7070ff;
  box-shadow: none;
}

.elevated {
  box-shadow: #8c7fac 0px 0px 2.5px;
}

.loading {
  transform: scale(5);
}

.reacting {
  cursor: default;
  color: #0051ff;
  background-color: #fff;
  border: 1px solid #7da6ff;
  box-shadow: none;
}
</style>
