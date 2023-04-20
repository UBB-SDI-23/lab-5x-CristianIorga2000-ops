<template>
  <v-container>
    <v-row>
      <v-col>
        <h1>Authors</h1>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-btn color="primary" @click="$router.push({ name: 'AddAuthor' })">
          Add Author
        </v-btn>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <authors-list />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import AuthorsList from '../components/AuthorsList.vue';

export default {
  name: 'AuthorsView',
  components: {
    AuthorsList,
  },
};
</script>
