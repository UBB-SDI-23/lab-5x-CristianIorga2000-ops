<template>
    <div>
      <!-- Author form for creating and updating authors goes here -->
      <h1 v-if="isNew">Create Author</h1>
      <h1 v-else>Edit Author</h1>
      <form @submit.prevent="submitForm">
        <label for="name">Name:</label>
        <input id="name" v-model="author.name" required />
        <br />
        <label for="email">Email:</label>
        <input id="email" v-model="author.email" required />
        <br />
        <label for="bio">Bio:</label>
        <textarea id="bio" v-model="author.bio" required></textarea>
        <br />
        <button type="submit">Save</button>
      </form>
    </div>
  </template>
  
  <script>
  import api from '../services/api';
  
  export default {
    name: 'AuthorForm',
    data() {
      return {
        author: {
          id: null,
          name: '',
          email: '',
          bio: '',
        },
      };
    },
    computed: {
      isNew() {
        return this.$route.name === 'CreateAuthor';
    },
  },
  methods: {
    async fetchAuthor(id) {
      try {
        const response = await api.getAuthor(id);
        this.author = response.data;
      } catch (error) {
        console.error('Error fetching author:', error);
      }
    },

    async submitForm() {
      try {
        if (this.isNew) {
          await api.createAuthor(this.author);
          this.$router.push({ path: '/authors' });
        } else {
          await api.updateAuthor(this.author.id, this.author);
          this.$router.push({ path: '/authors' });
        }
      } catch (error) {
        console.error('Error submitting author form:', error);
      }
    },
  },
  mounted() {
    if (!this.isNew) {
      this.fetchAuthor(this.$route.params.id);
    }
  },
};
</script>

  