import BaseApi from "./base";

export default {
  list() {
    return BaseApi.get("authorships/");
  },
  create(data) {
    return BaseApi.post("authorships/", data);
  },
  get(id) {
    return BaseApi.get(`authorships/${id}/`);
  },
  update(id, data) {
    return BaseApi.put(`authorships/${id}/`, data);
  },
  delete(id) {
    return BaseApi.delete(`authorships/${id}/`);
  },
};
