<template>
  <div class="home">
    <!--header class="sticky top-0">
      <button class="button mr-auto mt-2 p-4" v-on:click="$router.push('/')">
        Home
      </button>
    </header-->
    <main>
      <h5 class="text-3xl m-8">Stats de ventes :</h5>
      <div class="m-8 cards">
        <div class="flex stat_container">
          <div class="title text-xl mr-5">Total des ventes</div>
          <div class="text-xl">{{ sumOut }} €</div>
        </div>
        <div class="flex stat_container">
          <div class="title text-xl mr-5">Total des achats</div>
          <div class="text-xl">{{ sumIn }} €</div>
        </div>
        <div class="flex stat_container">
          <div class="title text-xl mr-5">Chiffre d'affaire total</div>
          <div class="text-xl">{{ sumIn + sumOut }} €</div>
        </div>
      </div>
      <div class="m-8 stat_container">
        <div class="text-2xl pt-5">
          Ventes et achats par
          <select v-model="sumByType" @change="(event) => setSumByType()">
            <option v-for="type in sumByTypes" :key="type" :value="type">
              {{ type }}
            </option>
          </select>
        </div>
        <VueApexCharts
          type="area"
          height="350"
          ref="chart"
          :options="sumBy.chartOptions"
          :series="sumBy.series"
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

type SumByType = "Jour" | "Mois" | "Année";

export default defineComponent({
  name: "StatsView",
  components: {
    VueApexCharts,
  },
  mounted() {
    this.fetchStock().then((data) => {
      console.log("stock fetched");
      this.stock = data;
      this.sumByDay = this.getSumByDay();
      this.sumByMonth = this.getSumByMonth();
      this.sumByYear = this.getSumByYear();
      this.setSumByType();
    });
  },
  data() {
    return {
      stock: [] as StockMove[],
      sumByTypes: ["Jour", "Mois", "Année"] as SumByType[],
      sumByType: "Jour" as SumByType,
      sumBy: {
        chartOptions: {
          chart: {
            id: "vuechart-example",
          },
          xaxis: {
            categories: [],
          },
        },
        series: [],
      } as {
        chartOptions: {
          chart: {
            id: string;
          };
          xaxis: {
            categories: string[];
          };
        };
        series: {
          name: string;
          data: number[];
        }[];
      },
      sumByDay: {
        chartOptions: {
          chart: {
            id: "vuechart-example",
          },
          xaxis: {
            categories: [],
          },
        },
        series: [],
      } as {
        chartOptions: {
          chart: {
            id: string;
          };
          xaxis: {
            categories: string[];
          };
        };
        series: {
          name: string;
          data: number[];
        }[];
      },
      sumByMonth: {
        chartOptions: {
          chart: {
            id: "vuechart-example",
          },
          xaxis: {
            categories: [],
          },
        },
        series: [],
      } as {
        chartOptions: {
          chart: {
            id: string;
          };
          xaxis: {
            categories: string[];
          };
        };
        series: {
          name: string;
          data: number[];
        }[];
      },
      sumByYear: {
        chartOptions: {
          chart: {
            id: "vuechart-example",
          },
          xaxis: {
            categories: [],
          },
        },
        series: [],
      } as {
        chartOptions: {
          chart: {
            id: string;
          };
          xaxis: {
            categories: string[];
          };
        };
        series: {
          name: string;
          data: number[];
        }[];
      },
    };
  },
  methods: {
    ...mapActions(["fetchStock"]),
    setSumByType() {
      console.log("sumByType: ", this.sumByType);
      switch (this.sumByType) {
        case "Jour" as SumByType:
          this.sumBy = this.sumByDay;
          break;
        case "Mois" as SumByType:
          this.sumBy = this.sumByMonth;
          break;
        case "Année" as SumByType:
          this.sumBy = this.sumByYear;
          break;
      }
      console.log("sumBy: ", this.sumBy);
    },
    getSumByDay() {
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
    getSumByMonth() {
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
        let month = date.getMonth();
        let year = date.getFullYear();
        let localeMonth = month + 1 + "/" + year;
        if (label.includes(localeMonth)) {
          // console.log('include')
          //if amount is sell
          if (mainData[index].type == "OUT") {
            out[label.indexOf(localeMonth)] += mainData[index].price;
            expense[label.indexOf(localeMonth)] += 0;
          } else {
            expense[label.indexOf(localeMonth)] += mainData[index].price;
            out[label.indexOf(localeMonth)] += 0;
          }
        } else {
          // console.log('else include')
          label.push(localeMonth);
          if (mainData[index].type == "OUT") {
            out.push(mainData[index].price);
            expense.push(0);
          } else {
            expense.push(mainData[index].price);
            out.push(0);
          }
        }
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
    getSumByYear() {
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
        let year = date.getFullYear();
        let localeYear = year.toString();
        if (label.includes(localeYear)) {
          // console.log('include')
          //if amount is sell
          if (mainData[index].type == "OUT") {
            out[label.indexOf(localeYear)] += mainData[index].price;
            expense[label.indexOf(localeYear)] += 0;
          } else {
            expense[label.indexOf(localeYear)] += mainData[index].price;
            out[label.indexOf(localeYear)] += 0;
          }
        } else {
          // console.log('else include')
          label.push(localeYear);
          if (mainData[index].type == "OUT") {
            out.push(mainData[index].price);
            expense.push(0);
          } else {
            expense.push(mainData[index].price);
            out.push(0);
          }
        }
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

.stat_container {
  background-color: white;
  border-radius: 10px;
  box-shadow: #d4dfe0 0px 0px 5px;
  margin: 10px;
  padding: 15px;
}

.cards {
  display: inline-flex;
}

.title {
  font-weight: bold;
  font-size: 1rem;
  padding-bottom: 10px;
}
</style>
