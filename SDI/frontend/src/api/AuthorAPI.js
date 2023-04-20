import BaseAPI from './BaseAPI';

export default class AuthorAPI extends BaseAPI {
  constructor() {
    super('authors');
  }

  async getTotalRoyalty() {
    const response = await this.getResource('total_royalty');
    return response;
  }
}
