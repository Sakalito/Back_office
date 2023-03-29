<template>
  <div class="home">
    <header class="sticky top-0">
      <button class="button mr-auto mt-2 p-4" v-on:click="$router.push('/')">
        Home
      </button>
    </header>
    <main>
      <div class="text-3xl m-8">Stats de ventes :</div>
      <div class="m-8">
        <div class="flex">
          <div class="text-xl mr-5">Total des ventes :</div>
          <div class="text-xl">{{ sumOut }} €</div>
        </div>
        <div class="flex">
          <div class="text-xl mr-5">Total des achats :</div>
          <div class="text-xl">{{ sumIn }} €</div>
        </div>
        <div class="flex">
          <div class="text-xl mr-5">Chiffre d'affaire total :</div>
          <div class="text-xl">{{ sumIn + sumOut }} €</div>
        </div>
      </div>
      <div class="m-8">
        <div class="text-2xl pt-5">Ventes et achats par jour :</div>
      </div>
      <div class="max-w-16">
        <VueApexCharts
          type="area"
          height="350"
          ref="chart"
          :options="sumByDay.chartOptions"
          :series="sumByDay.series"
        ></VueApexCharts>
      </div>
    </main>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import VueApexCharts from "vue3-apexcharts";
import { mapActions } from "vuex";
import { StockMove } from "@/types";

export default defineComponent({
  name: "StatsView",
  components: {
    VueApexCharts,
  },
  mounted() {
    this.fetchStock().then((data) => {
      console.log("stock fetched");
      this.stock = data;
    });
  },
  data() {
    return {
      stock: [] as StockMove[],
    };
  },
  methods: {
    ...mapActions(["fetchStock"]),
  },
  computed: {
    sumOut() {
      let sumOut = 0;
      for (let index = 0; index < this.stock.length; index++) {
        // console.log(new Date(store.state.data[index].date).toLocaleDateString())
        if (this.stock[index].type == "OUT") sumOut += this.stock[index].price;
      }
      return sumOut;
    },
    sumIn() {
      let sumIn = 0;
      for (let index = 0; index < this.stock.length; index++) {
        // console.log(new Date(store.state.data[index].date).toLocaleDateString())
        if (this.stock[index].type == "IN") {
          sumIn += this.stock[index].price;
          // let price = this.stock[index].price;
          // console.log("price: ", price, "type: ", typeof price);
        }
      }
      return sumIn;
    },
    sumByDay() {
      let out: number[] = [];
      let expense: number[] = [];
      let label: string[] = [];
      let mainData = this.stock;
      mainData = mainData.sort(
        (a: StockMove, b: StockMove) => a.date.getTime() - b.date.getTime()
      );
      // console.log(mainData.length)
      for (let index = 0; index < mainData.length; index++) {
        // console.log(index)
        let date = mainData[index].date;
        // console.log(date)
        let localeDate = date.toLocaleDateString();
        if (label.includes(localeDate)) {
          // console.log('include')
          //if amount is sell
          if (mainData[index].type == "OUT") {
            out[label.indexOf(localeDate)] += mainData[index].price;
            expense[label.indexOf(localeDate)] += 0;
          } else {
            expense[label.indexOf(localeDate)] += mainData[index].price;
            out[label.indexOf(localeDate)] += 0;
          }
        } else {
          // console.log('else include')
          label.push(localeDate);
          if (mainData[index].type == "OUT") {
            out.push(mainData[index].price);
            expense.push(0);
          } else {
            expense.push(mainData[index].price);
            out.push(0);
          }
        }
        // console.log(label.length == out.length)
        // this.$data.chartOptions.xaxis.categories= label
        // this.$data.series[0].data= out
      }
      return {
        chartOptions: {
          chart: {
            id: "vuechart-example",
          },
          xaxis: {
            categories: label,
          },
        },
        series: [
          {
            name: "ventes",
            data: out,
          },
          {
            name: "achats",
            data: expense,
          },
        ],
      };
    },
  },
});
</script>

<style>
.home {
}
header {
  min-height: 120px;
  background: #3c7a1f;
}
main {
  overflow-y: hidden;
  font-size: 20px;
}
</style>
