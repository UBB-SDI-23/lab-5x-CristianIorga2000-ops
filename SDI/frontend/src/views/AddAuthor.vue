<template>
  <v-container>
    <v-row>
      <v-col>
        <h1>Add Author</h1>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <author-form  v-if="dialog" @submit="createAuthor" @close-dialog="closeDialog" />
      </v-col>
    </v-row>
  </v-container>
</template>
<script>
import AuthorForm from '../components/AuthorForm.vue';
import AuthorAPI from '@/api/AuthorAPI';

export default {
  name: 'AddAuthor',
  components: {
    AuthorForm,
  },
  data() {
    return {
      dialog: true,
    };
  },
  methods: {
    async createAuthor(author) {
      const api = new AuthorAPI();
      await api.createResource(author);
      this.closeDialog();
    },
    closeDialog() {
      this.dialog = false;
      this.$router.push({ name: 'Authors' });
    },
  },
};
</script>



