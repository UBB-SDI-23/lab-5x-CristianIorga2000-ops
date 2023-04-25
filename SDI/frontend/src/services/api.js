import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:8000/api'; 
const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export default {
  getAuthors() {
    return api.get('/authors/');
  },

  createAuthor(payload) {
    return api.post('/authors/', payload);
  },

  getAuthor(id) {
    return api.get(`/authors/${id}/`);
  },

  updateAuthor(id, payload) {
    return api.put(`/authors/${id}/`, payload);
  },

  deleteAuthor(id) {
    return api.delete(`/authors/${id}/`);
  },

  getTotalRoyalty() {
    return api.get('/authors/total_royalty/');
  },
};
