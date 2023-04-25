<template>
  <div>
    <h1>Authors</h1>
    <ul v-if="authors">
      <li v-for="(author, index) in authors" :key="author.id || index">
        {{ author.name }}
        <router-link :to="`/authors/${author.id}/edit`">Edit</router-link>
        <button @click="deleteAuthor(author.id)">Delete</button>
      </li>
    </ul>
    <p v-else>Loading authors...</p>
  </div>
</template>


  <script>
  import api from '../services/api';
  
  export default {
    name: 'AuthorList',
    data() {
      return {
        authors: [],
      };
    },
    methods: {
      async fetchAuthors() {
        try {
          const response = await api.getAuthors();
          this.authors = response.data.results;
          console.log('Authors fetched:', this.authors);
        } catch (error) {
          console.error('Error fetching authors:', error);
        }
      },
  
      editAuthor(id) {
        this.$router.push({ path: `/authors/edit/${id}` });
      },
  
      async deleteAuthor(id) {
        try {
          await api.deleteAuthor(id);
          this.fetchAuthors();
        } catch (error) {
          console.error('Error deleting author:', error);
        }
      },
    },
    mounted() {
      console.log("Real negro");
      this.fetchAuthors();
    },
  };
  </script>
  