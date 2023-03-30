<template>
  <input
    class="text_field"
    :id="id ? id : hint"
    :type="type"
    :class="{ invalid: validator && !isValid() }"
    :placeholder="hint"
    v-bind:required="required"
    v-on:input="reactOnChange"
    v-model="input"
  />
  <div class="validation_text" v-if="validator && !isValid()">
    {{ validate(input) }}
  </div>
</template>

<script lang="ts">
import { defineComponent, PropType } from "vue";

export type OnChangeFunction = (value: string) => void;
export type ValidatorFunction = (value: string) => null | string;

export default defineComponent({
  name: "TextField",
  components: {},
  props: {
    onChange: { type: Function as PropType<OnChangeFunction>, required: true },
    validator: {
      type: Function as PropType<ValidatorFunction>,
      required: false,
    },
    hint: { type: String, required: false },
    type: { type: String, default: "text", required: false },
    required: { type: Boolean, default: false, required: false },
    id: { type: String, required: false },
  },
  data() {
    return {
      input: "",
    };
  },
  methods: {
    reactOnChange() {
      console.log("this.input: ", this.input);
      this.onChange(this.input);
    },
    validate(value: string): null | string {
      if (this.validator && this.input.length > 0) {
        console.log("validating");
        return this.validator(value);
      } else {
        return null;
      }
    },
    isValid(): boolean {
      return this.validate(this.input) === null;
    },
  },
});
</script>

<style>
.text_field {
  width: 250px;
  margin: 5px;
  padding: 10px 15px;
  font-size: 16px;
  border: 1px solid #d4dfe0;
  border-radius: 10px;
  display: block;
}

.invalid {
  border: 1px solid #ff0055;
}

.validation_text {
  color: #ff0055;
  font-size: 12px;
  padding: 0px 15px;
  text-align: start;
}

input[type="text"]:focus,
input[type="email"]:focus,
input[type="password"]:focus {
  outline: none;
}
</style>
