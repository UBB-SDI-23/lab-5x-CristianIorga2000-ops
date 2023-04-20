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
                <v-text-field v-model="author.first_name" label="First Name"></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field v-model="author.last_name" label="Last Name"></v-text-field>
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
          first_name: '',
          last_name: '',
        },
      };
    },
    computed: {
      formTitle() {
        return this.authorId ? 'Edit Author' : 'Add Author';
      },
    },
    methods: {
      saveAuthor() {
        // Call API to save author
        this.$emit('close-dialog');
      },
    },
  };
  </script>
  