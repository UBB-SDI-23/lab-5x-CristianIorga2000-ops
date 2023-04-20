export default class BaseAPI {
    constructor(resource) {
      this.baseURL = 'http://35.228.0.43/api';
      this.resource = resource;
    }
  
    async getResource() {
      const response = await fetch(`${this.baseURL}/${this.resource}/`);
      return await response.json();
    }
  
    async createResource(resourceData) {
      const response = await fetch(`${this.baseURL}/${this.resource}/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(resourceData),
      });
      return await response.json();
    }
  
    async getResourceById(id) {
      const response = await fetch(`${this.baseURL}/${this.resource}/${id}/`);
      return await response.json();
    }
  
    async updateResourceById(id, resourceData) {
      const response = await fetch(`${this.baseURL}/${this.resource}/${id}/`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(resourceData),
      });
      return await response.json();
    }
  
    async deleteResourceById(id) {
      const response = await fetch(`${this.baseURL}/${this.resource}/${id}/`, {
        method: 'DELETE',
      });
      return await response.json();
    }
  }
  