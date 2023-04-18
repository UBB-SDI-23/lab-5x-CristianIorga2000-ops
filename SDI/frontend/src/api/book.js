import BaseApi from "./base";

export default {
  list() {
    return BaseApi.get("books/");
  },
  create(data) {
    return BaseApi.post("books/", data);
  },
  get(id) {
    return BaseApi.get(`books/${id}/`);
  },
  update(id, data) {
    return BaseApi.put(`books/${id}/`, data);
  },
  delete(id) {
    return BaseApi.delete(`books/${id}/`);
  },
  getAverageRating() {
    return BaseApi.get("books/average_rating/");
  },
};
