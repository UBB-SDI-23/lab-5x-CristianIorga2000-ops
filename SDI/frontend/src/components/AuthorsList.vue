<template>
    <div>
      <v-data-table :headers="headers" :items="authors" class="elevation-1">
        <template v-slot:top>
          <v-toolbar flat>
            <v-toolbar-title>Authors</v-toolbar-title>
            <v-spacer></v-spacer>
            <v-dialog v-model="dialog" max-width="500px">
              <template v-slot:activator="{ on, attrs }">
                <v-btn color="primary" dark class="mb-2" v-bind="attrs" v-on="on">Add Author</v-btn>
              </template>
              <author-form @close-dialog="dialog = false" />
            </v-dialog>
          </v-toolbar>
        </template>
        <template v-slot:item="{ item }">
            <v-icon small @click="$router.push(`/authors/${item.id}`)">mdi-eye</v-icon>
        </template>
    </v-data-table>
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
      authors: [], // Replace with fetched data from API
      headers: [
        { text: 'First Name', value: 'first_name' },
        { text: 'Last Name', value: 'last_name' },
        { text: 'Actions', value: 'action', sortable: false },
      ],
      dialog: false,
    };
  },
};
</script>
  