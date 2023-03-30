import endPoints from "@/ressources/constants";
import { Product, Result, StockMove, User } from "@/types";
import { createStore } from "vuex";

export default createStore({
  state: {
    products: [] as Product[],
    user: {} as User,
    stock: [] as StockMove[],
  },
  getters: {
    products(state) {
      return state.products;
    },
    user(state) {
      return state.user;
    },
    stock(state) {
      return state.stock;
    },
  },
  mutations: {
    setProducts(state, products) {
      state.products = products;
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
    fetchProducts(context) {
      console.log("loading products...");
      return fetch(endPoints.products)
        .then((response) => response.json())
        .then((data) => {
          context.commit("setProducts", data);
          console.log(data.length + " products loaded");
          return data;
        })
        .catch((err) => console.error(err));
    },

    // update a product in the backend
    updateProduct(context, product: Partial<Product>): Promise<Result> {
      console.log("updating product: ", product);
      return fetch(endPoints.product + product.id + "/", {
        method: "PATCH",
        headers: {
          "Content-Type": "application/json",
          Authorization: "Bearer " + localStorage.getItem("access"),
        },
        body: JSON.stringify({
          name: product.name,
          price: product.price,
          comments: product.comments,
          discount: product.discount,
          availability: product.availability,
        }),
      })
        .then((response) => {
          if (response.status === 200) {
            context.dispatch("fetchProducts");
            return {
              code: 200,
              message: "product updated",
              state: true,
            };
          } else {
            console.error(response.body);
            throw new Error("invalid credentials");
          }
        })
        .catch((err) => {
          console.error(err);
          return {
            code: 401,
            message: "Error updating product",
            state: false,
          };
        });
    },

    // get a product by id
    async getProduct(context, id: number): Promise<Product | undefined> {
      console.log("getting product with id: ", id);
      if (context.state.products.length === 0) {
        await context.dispatch("fetchProducts");
      }
      try {
        const prod = context.state.products.filter((product) => {
          // console.log("equal: ", product.id == id);
          return product.id == id;
        })[0];
        console.log("product: ", prod);
        return prod;
      } catch (err) {
        console.error(err);
        return undefined;
      }
    },
  },
  modules: {},
});
