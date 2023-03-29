import endPoints from "@/ressources/constants";
import { Result, StockMove, User } from "@/types";
import { createStore } from "vuex";

export default createStore({
  state: {
    fishes: [],
    user: {} as User,
    stock: [] as StockMove[],
  },
  getters: {
    fishes(state) {
      return state.fishes;
    },
    user(state) {
      return state.user;
    },
    stock(state) {
      return state.stock;
    },
  },
  mutations: {
    setFishes(state, fishes) {
      state.fishes = fishes;
    },
    setUser(state, user) {
      state.user = user;
    },
  },
  actions: {
    // login user and store access and refresh tokens in local storage
    login(
      context,
      credentials: { username: string; password: string }
    ): Promise<Result> {
      return fetch(endPoints.login, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(credentials),
      })
        .then((response) => {
          if (response.status === 200) {
            return response.json();
          } else {
            throw new Error("invalid credentials");
          }
        })
        .then((data) => {
          console.log("data: ", data);
          console.log("login successful");
          localStorage.setItem("access", data.access);
          localStorage.setItem("refresh", data.refresh);
          context.dispatch("fetchUser");
          return {
            code: 200,
            message: "login successful",
            state: true,
          };
        })
        .catch((err) => {
          console.error(err);
          return {
            code: 401,
            message: "invalid credentials",
            state: false,
          };
        });
    },

    isAuthenticated(): boolean {
      // console.log("token: ", localStorage.getItem("access"));
      return localStorage.getItem("access") !== null;
      // return false;
    },

    // fetch user info from backend and store it in local storage
    fetchUser(context): Promise<Result> {
      return fetch(endPoints.user, {
        headers: {
          Authorization: "Bearer " + localStorage.getItem("access"),
        },
      })
        .then((response) => {
          if (response.status === 200) {
            response.json().then((data) => {
              context.commit("setUser", data);
            });
            return {
              code: 200,
              message: "user fetched",
              state: true,
            };
          } else {
            throw new Error("invalid credentials");
          }
        })
        .catch((err) => {
          console.error(err);
          return {
            code: 401,
            message: "invalid credentials",
            state: false,
          };
        });
    },

    // fetch stock movements from backend and store them in local storage
    fetchStock(context): Promise<StockMove[]> {
      console.log("loading stock...");
      return fetch(endPoints.stock, {
        headers: {
          Authorization: "Bearer " + localStorage.getItem("access"),
        },
      })
        .then((response) => {
          console.log("responsed status: ", response.status);
          if (response.status === 200) {
            console.log("setting stock");
            return response.json().then((data) => {
              return (context.state.stock = data.map((item: any) => {
                return StockMove.fromJson(item);
              }));
            });
          } else {
            throw new Error("invalid credentials");
          }
        })
        .catch((err) => {
          console.error(err);
          return [];
        });
    },

    // fetch fishes from backend and store them in local storage
    fetchFishes(context) {
      console.log("loading fishes...");
      return fetch(endPoints.products)
        .then((response) => response.json())
        .then((data) => {
          context.commit("setFishes", data);
          console.log(data.length + " fishes loaded");
          return data;
        })
        .catch((err) => console.error(err));
    },
  },
  modules: {},
});
