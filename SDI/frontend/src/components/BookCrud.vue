<template>
    <div>
      <h2>Books</h2>
      <!-- Add book form -->
      <div>
        <h3>Add Book</h3>
        <form @submit.prevent="createBook">
          <label>Title:</label>
          <input type="text" v-model="newBook.title" required />
          <label>Summary:</label>
          <textarea v-model="newBook.summary"></textarea>
          <label>Published Date:</label>
          <input type="date" v-model="newBook.published_date" required />
          <button type="submit">Add Book</button>
        </form>
      </div>
      <!-- Book list -->
      <table>
        <thead>
          <tr>
            <th>Title</th>
            <th>Summary</th>
            <th>Published Date</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="book in books" :key="book.id">
            <td>{{ book.title }}</td>
            <td>{{ book.summary }}</td>
            <td>{{ book.published_date }}</td>
            <td>
              <button @click="startEditBook(book)">Edit</button>
              <button @click="deleteBook(book.id)">Delete</button>
            </td>
          </tr>
        </tbody>
      </table>
      <!-- Edit book form -->
      <div v-if="editingBook">
        <h3>Edit Book</h3>
        <form @submit.prevent="updateBook">
          <input type="hidden" v-model="editingBook.id" />
          <label>Title:</label>
          <input type="text" v-model="editingBook.title" required />
          <label>Summary:</label>
          <textarea v-model="editingBook.summary"></textarea>
          <label>Published Date:</label>
          <input type="date" v-model="editingBook.published_date" required />
          <button type="submit">Save</button>
          <button @click="cancelEditBook">Cancel</button>
        </form>
      </div>
    </div>
  </template>
  
  <script>
  import BookApi from "@/api/book.js";
  
  export default {
    name: "BookCrud",
    data() {
      return {
        books: [],
        newBook: {
          title: "",
          summary: "",
          published_date: "",
        },
        editingBook: null,
      };
    },
    async created() {
      await this.fetchBooks();
    },
    methods: {
      async fetchBooks() {
        try {
          const response = await BookApi.list();
          this.books = response.data;
        } catch (error) {
          console.error("Error fetching books:", error);
        }
      },
      async createBook() {
        try {
          await BookApi.create(this.newBook);
          await this.fetchBooks();
          this.newBook = { title: "", summary: "", published_date: "" };
        } catch (error) {
          console.error("Error creating book:", error);
        }
      },
      startEditBook(book) {
        this.editingBook = { ...book };
      },
      async updateBook() {
          try {
            await BookApi.update(this.editingBook.id, this.editingBook);
            await this.fetchBooks();
            this.editingBook = null;
          } catch (error) {
            console.error("Error updating book:", error);
          }
        },
        async deleteBook(id) {
          try {
            await BookApi.delete(id);
            await this.fetchBooks();
          } catch (error) {
            console.error("Error deleting book:", error);
          }
        },
        cancelEditBook() {
          this.editingBook = null;
        },
      },
    };
</script>