const API_URL = "http://localhost:8000/";
const endPoints = {
  login: API_URL + "api/token/",
  user: API_URL + "user/",
  product: API_URL + "product/",
  productCreate: API_URL + "product/create/",
  products: API_URL + "products/",
  stock: API_URL + "stock/",
  renderedImage: API_URL + "image/rendered/",
};

export default endPoints;
