import BaseApi from "./base";

export default {
  list() {
    return BaseApi.get("reviews/");
  },
  create(data) {
    return BaseApi.post("reviews/", data);
  },
  get(id) {
    return BaseApi.get(`reviews/${id}/`);
  },
  update(id, data) {
    return BaseApi.put(`reviews/${id}/`, data);
  },
  delete(id) {
    return BaseApi.delete(`reviews/${id}/`);
  },
  filterByRating(rating) {
    return BaseApi.get(`reviews/filter_by_rating_gt?rating=${rating}`);
  },
};
