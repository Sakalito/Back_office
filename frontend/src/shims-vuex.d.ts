import { Store } from "@/store"; // path to store file
import { Toasted } from "vue-toasted";

declare module "@vue/runtime-core" {
  interface ComponentCustomProperties {
    $store: Store;
    // $toasted: Toasted;
  }
}
