import endPoints from "@/ressources/constants";
import { createStore } from "vuex";

export type User = {
  id: number;
  username: string;
  email?: string;
  first_name?: string;
  last_name?: string;
};

export type ProductOwner = {
  id: number;
  name: string;
};

export type Category = {
  id: number;
  name: string;
  description?: string;
};

export type Discount = {
  id: number;
  name?: string;
  description?: string;
  rate: number;
  startDate: Date;
  endDate?: Date;
};

export type Product = {
  id: number;
  name: string;
  category: Category;
  price: number;
  unit: string;
  availability: boolean;
  sale: boolean;
  discount: Discount;
  comments: string;
  owner: ProductOwner;
};

export type Result = {
  code: number;
  message: string;
  state: boolean;
};

export default createStore({
  state: {
    fishes: [],
    user: {} as User,
  },
  getters: {
    fishes(state) {
      return state.fishes;
    },
    isAuthentified(state) {
      // return localStorage.getItem("access") !== null;
      return false;
    },
    user(state) {
      return state.user;
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

    // fetch user info from backend and store it in local storage
    fetchUser(context) {
      return fetch(endPoints.user, {
        headers: {
          Authorization: "Bearer " + localStorage.getItem("access"),
        },
      }).then((response) => {
        if (response.status === 200) {
          response.json().then((data) => {
            context.commit("setUser", data);
          });
        }
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
