<template>
    <div>
      <h2>Authors</h2>
      <!-- Add author form -->
      <div>
        <h3>Add Author</h3>
        <form @submit.prevent="createAuthor">
          <label>Name:</label>
          <input type="text" v-model="newAuthor.name" required />
          <label>Email:</label>
          <input type="email" v-model="newAuthor.email" required />
          <label>Bio:</label>
          <textarea v-model="newAuthor.bio"></textarea>
          <button type="submit">Add Author</button>
        </form>
      </div>
      <!-- Author list -->
      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Email</th>
            <th>Bio</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="author in authors" :key="author.id">
            <td>{{ author.name }}</td>
            <td>{{ author.email }}</td>
            <td>{{ author.bio }}</td>
            <td>
              <button @click="startEditAuthor(author)">Edit</button>
              <button @click="deleteAuthor(author.id)">Delete</button>
            </td>
          </tr>
        </tbody>
      </table>
      <!-- Edit author form -->
      <div v-if="editingAuthor">
        <h3>Edit Author</h3>
        <form @submit.prevent="updateAuthor">
          <input type="hidden" v-model="editingAuthor.id" />
          <label>Name:</label>
          <input type="text" v-model="editingAuthor.name" required />
          <label>Email:</label>
          <input type="email" v-model="editingAuthor.email" required />
          <label>Bio:</label>
          <textarea v-model="editingAuthor.bio"></textarea>
          <button type="submit">Save</button>
          <button @click="cancelEditAuthor">Cancel</button>
        </form>
      </div>
    </div>
  </template>
  
  <script>
  import AuthorApi from "@/api/author.js";
  
  export default {
    name: "AuthorCrud",
    data() {
      return {
        authors: [],
        newAuthor: {
          name: "",
          email: "",
          bio: "",
        },
        editingAuthor: null,
      };
    },
    async created() {
      await this.fetchAuthors();
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
      async createAuthor() {
        try {
          await AuthorApi.create(this.newAuthor);
          await this.fetchAuthors();
          this.newAuthor = { name: "", email: "", bio: "" };
        } catch (error) {
          console.error("Error creating author:", error);
        }
      },
      startEditAuthor(author) {
        this.editingAuthor = { ...author };
      },
      async updateAuthor() {
        try {
          await AuthorApi.update(this.editingAuthor.id, this.editingAuthor);
          await this.fetchAuthors();
          this.editingAuthor = null;
        } catch (error) {
          console.error("Error updating author:", error);
        }
      },
      async deleteAuthor(id) {
      try {
        await AuthorApi.delete(id);
        await this.fetchAuthors();
      } catch (error) {
        console.error("Error deleting author:", error);
      }
    },
    cancelEditAuthor() {
      this.editingAuthor = null;
    },
  },
};
</script>