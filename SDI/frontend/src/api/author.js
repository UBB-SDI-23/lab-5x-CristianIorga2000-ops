import BaseApi from "./base";

export default {
  list() {
    return BaseApi.get("authors/");
  },
  create(data) {
    return BaseApi.post("authors/", data);
  },
  get(id) {
    return BaseApi.get(`authors/${id}/`);
  },
  update(id, data) {
    return BaseApi.put(`authors/${id}/`, data);
  },
  delete(id) {
    return BaseApi.delete(`authors/${id}/`);
  },
  addBooks(id, data) {
    return BaseApi.post(`authors/${id}/books/`, data);
  },
  getTotalRoyalty() {
    return BaseApi.get("authors/total_royalty/");
  },
};
