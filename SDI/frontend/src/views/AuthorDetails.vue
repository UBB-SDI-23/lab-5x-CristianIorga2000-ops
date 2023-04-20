<template>
    <v-container>
      <v-row>
        <v-col>
          <h1>Author Details</h1>
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <author-form :author="author" @submit="updateAuthor" />
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <v-btn color="error" @click="deleteAuthor">Delete Author</v-btn>
        </v-col>
      </v-row>
    </v-container>
  </template>
  
  <script>
  import AuthorForm from '../components/AuthorForm.vue'
  import AuthorAPI from '@/api/AuthorAPI'

  const api = new AuthorAPI();

  export default {
    name: 'AuthorDetails',
    components: {
      AuthorForm,
    },
    props: {
      id: {
        type: String,
        required: true,
      },
    },
    data() {
      return {
        author: {},
      }
    },
    methods: {
      async updateAuthor(author) {
        await api.updateResourceById(this.id, author);
        this.$router.push({ name: 'Authors' });
      },
      async deleteAuthor() {
        await api.deleteResourceById(this.id);
        this.$router.push({ name: 'Authors' });
      },
    },
    async mounted() {
      this.author = await api.getResourceById(this.id);
    },
  }
  </script>
