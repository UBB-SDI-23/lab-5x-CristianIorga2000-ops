import axios from "axios";

const instance = axios.create({
  baseURL: "http://35.228.0.43/api/",
});

export default instance;
