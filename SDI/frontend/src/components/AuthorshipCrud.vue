<template>
    <div>
      <h2>Authorships</h2>
      <!-- Add authorship form -->
      <div>
        <h3>Add Authorship</h3>
        <form @submit.prevent="createAuthorship">
          <label>Author:</label>
          <select v-model="newAuthorship.author" required>
            <option v-for="author in authors" :key="author.id" :value="author.id">{{ author.name }}</option>
          </select>
          <label>Book:</label>
          <select v-model="newAuthorship.book" required>
            <option v-for="book in books" :key="book.id" :value="book.id">{{ book.title }}</option>
          </select>
          <label>Contribution:</label>
          <input type="text" v-model="newAuthorship.contribution" required />
          <label>Royalty Percentage:</label>
          <input type="number" min="0" max="100" step="0.01" v-model="newAuthorship.royalty_percentage" required />
          <button type="submit">Add Authorship</button>
        </form>
      </div>
      <!-- Authorship list -->
      <table>
        <thead>
          <tr>
            <th>Author</th>
            <th>Book</th>
            <th>Contribution</th>
            <th>Royalty Percentage</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="authorship in authorships" :key="authorship.id">
            <td>{{ authorship.author.name }}</td>
            <td>{{ authorship.book.title }}</td>
            <td>{{ authorship.contribution }}</td>
            <td>{{ authorship.royalty_percentage }}</td>
            <td>
              <button @click="startEditAuthorship(authorship)">Edit</button>
              <button @click="deleteAuthorship(authorship.id)">Delete</button>
            </td>
          </tr>
        </tbody>
      </table>
      <!-- Edit authorship form -->
      <div v-if="editingAuthorship">
        <h3>Edit Authorship</h3>
        <form @submit.prevent="updateAuthorship">
          <input type="hidden" v-model="editingAuthorship.id" />
          <label>Author:</label>
          <select v-model="editingAuthorship.author" required>
            <option v-for="author in authors" :key="author.id" :value="author.id">{{ author.name }}</option>
          </select>
          <label>Book:</label>
          <select v-model="editingAuthorship.book" required>
            <option v-for="book in books" :key="book.id" :value="book.id">{{ book.title }}</option>
          </select>
          <label>Contribution:</label>
          <input type="text" v-model="editingAuthorship.contribution" required />
          <label>Royalty Percentage:</label>
          <input type="number" min="0" max="100" step="0.01" v-model="editingAuthorship.royalty_percentage" required />
          <button type="submit">Save</button>
          <button @click="cancelEditAuthorship">Cancel</button>
        </form>
      </div>
    </div>
  </template>
  
  <script>
  import AuthorApi from "@/api/author.js";
  import BookApi from "@/api/book.js";
  import AuthorshipApi from "@/api/authorship.js";

export default {
  name: "AuthorshipCrud",
  data() {
    return {
      authors: [],
      books: [],
      authorships: [],
      newAuthorship: {
        author: "",
        book: "",
        contribution: "",
        royalty_percentage: "",
      },
      editingAuthorship: null,
    };
  },
  async created() {
    await this.fetchAuthors();
    await this.fetchBooks();
    await this.fetchAuthorships();
  },
  methods: {
    async fetchAuthors() {
      try {
        const response = await AuthorApi.list();
        this.authors = response.data;
      } catch (error) {
        console.error("Error fetching authors:", error);
      }
    },
    async fetchBooks() {
      try {
        const response = await BookApi.list();
        this.books = response.data;
      } catch (error) {
        console.error("Error fetching books:", error);
      }
    },
    async fetchAuthorships() {
      try {
        const response = await AuthorshipApi.list();
        this.authorships = response.data;
      } catch (error) {
        console.error("Error fetching authorships:", error);
      }
    },
    async createAuthorship() {
      try {
        await AuthorshipApi.create(this.newAuthorship);
        await this.fetchAuthorships();
        this.newAuthorship = {
          author: "",
          book: "",
          contribution: "",
          royalty_percentage: "",
        };
      } catch (error) {
        console.error("Error creating authorship:", error);
      }
    },
    startEditAuthorship(authorship) {
      this.editingAuthorship = { ...authorship };
    },
    async updateAuthorship() {
      try {
        await AuthorshipApi.update(this.editingAuthorship.id, this.editingAuthorship);
        await this.fetchAuthorships();
        this.editingAuthorship = null;
      } catch (error) {
        console.error("Error updating authorship:", error);
      }
    },
    async deleteAuthorship(id) {
      try {
        await AuthorshipApi.delete(id);
        await this.fetchAuthorships();
      } catch (error) {
        console.error("Error deleting authorship:", error);
      }
    },
    cancelEditAuthorship() {
      this.editingAuthorship = null;
    },
  },
};
</script>
