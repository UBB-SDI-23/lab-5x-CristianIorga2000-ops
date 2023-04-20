<template>
  <v-dialog v-model="dialog" persistent max-width="600px">
    <v-card>
      <v-card-title>
        <span class="text-h5">{{ formTitle }}</span>
      </v-card-title>
      <v-card-text>
        <v-container>
          <v-row>
            <v-col cols="12">
              <v-text-field v-model="author.name" label="Name"></v-text-field>
            </v-col>
            <v-col cols="12">
              <v-text-field v-model="author.email" label="Email"></v-text-field>
            </v-col>
            <v-col cols="12">
              <v-text-field v-model="author.bio" label="Bio"></v-text-field>
            </v-col>
          </v-row>
        </v-container>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="blue darken-1" text @click="$emit('close-dialog')">Cancel</v-btn>
        <v-btn color="blue darken-1" text @click="saveAuthor">Save</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
<script>
import AuthorAPI from '@/api/AuthorAPI';

export default {
  props: {
    authorId: {
      type: Number,
      default: null,
    },
  },
  data() {
    return {
      dialog: true,
      author: {
        name: '',
        email: '',
        bio: '',
      },
    };
  },
  computed: {
    formTitle() {
      return this.authorId ? 'Edit Author' : 'Add Author';
    },
  },
  methods: {
    async saveAuthor() {
      const authorAPI = new AuthorAPI();
      
      if (this.authorId) {
        // Call API to update author
        await authorAPI.updateResourceById(this.authorId, this.author);
      } else {
        // Call API to create author
        await authorAPI.createResource(this.author);
      }
      
      this.$emit('close-dialog');
    },
  },
};

</script>