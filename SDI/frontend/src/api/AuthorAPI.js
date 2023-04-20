import BaseAPI from './BaseAPI';

export default class AuthorAPI extends BaseAPI {
  constructor() {
    super('authors');
  }

  async getTotalRoyalty() {
    const response = await fetch(`${this.baseURL}/${this.resource}/total_royalty`);
    const data = await response.json();
    return data;
  }
}