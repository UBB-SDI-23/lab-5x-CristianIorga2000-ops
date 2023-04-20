<template>
  <div>
    <v-card>
      <v-card-title>
        <span class="text-h4">{{ author.first_name }} {{ author.last_name }}</span>
      </v-card-title>
      <v-card-text>
        <v-container>
          <v-row>
            <v-col cols="12" sm="6">
              <p><strong>First Name:</strong> {{ author.first_name }}</p>
            </v-col>
            <v-col cols="12" sm="6">
              <p><strong>Last Name:</strong> {{ author.last_name }}</p>
            </v-col>
            <v-col cols="12">
              <p><strong>Bio:</strong> {{ author.bio }}</p>
            </v-col>
          </v-row>
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
import AuthorAPI from '@/api/AuthorAPI';

export default {
  components: {
    AuthorForm,
  },
  data() {
    return {
      author: {},
      dialog: false,
    };
  },
  async mounted() {
    const authorAPI = new AuthorAPI();
    const id = this.$route.params.id;
    this.author = await authorAPI.getResourceById(id);
  },
  methods: {
    editAuthor() {
      this.dialog = true;
    },
    async deleteAuthor() {
      const authorAPI = new AuthorAPI();
      await authorAPI.deleteResource(this.author.id);
      this.$router.push('/authors');
    },
  },
};
</script>