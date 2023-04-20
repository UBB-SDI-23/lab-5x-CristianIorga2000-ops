<template>
    <div>
      <v-card>
        <v-card-title>
          <span class="text-h4">{{ author.first_name }} {{ author.last_name }}</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <!-- Display author details here -->
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-btn color="blue darken-1" text @click="editAuthor">Edit</v-btn>
          <v-btn color="red darken-1" text @click="deleteAuthor">Delete</v-btn>
        </v-card-actions>
      </v-card>
      <author-form v-if="dialog" :authorId="author.id" @close-dialog="dialog = false" />
    </div>
  </template>
  
  <script>
  import AuthorForm from './AuthorForm.vue';
  
  export default {
    components: {
      AuthorForm,
    },
    data() {
      return {
        author: {}, // Replace with fetched data from API
        dialog: false,
      };
    },
    methods: {
      editAuthor() {
        this.dialog = true;
      },
      deleteAuthor(){
      // Call API to delete the author and redirect to authors list
      this.$router.push('/authors');
    },
  },
};
</script>
  