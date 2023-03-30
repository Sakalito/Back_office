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
  category: string;
  price: number;
  unit: string;
  availability: boolean;
  sale: boolean;
  discount?: number;
  comments: string;
  owner: string;
  images?: string[];
};

export type StockMoveItem = {
  id: number;
  product: number;
  amount: number;
};

export class StockMove {
  id: number;
  date: Date;
  products: StockMoveItem[];
  type: "IN" | "OUT";
  price: number;

  constructor(
    id: number,
    date: Date,
    products: StockMoveItem[],
    type: "IN" | "OUT",
    price: number
  ) {
    this.id = id;
    this.date = date;
    this.products = products;
    this.type = type;
    this.price = price;
  }

  static fromJson(json: any): StockMove {
    return new StockMove(
      json.id,
      new Date(json.date),
      json.products as StockMoveItem[],
      json.type,
      Number(json.price)
    );
  }
}

export type Result = {
  code: number;
  message: string;
  state: boolean;
};
