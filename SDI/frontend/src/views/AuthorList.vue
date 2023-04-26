<template>
  <div>
    <h1>Authors</h1>
    <DataTable v-if="authors" :value="authors" :sortField="sortField" :sortOrder="sortOrder" @sort="onSort">
      <Column field="name" header="Name" sortable></Column>
      <Column field="email" header="Email" sortable></Column>
      <Column field="bio" header="Bio" sortable></Column>
      <Column field="created_at" header="Created at" sortable></Column>
      <Column field="updated_at" header="Updated at" sortable></Column>
      <Column header="Actions">
        <template #body="slotProps">
          <router-link :to="`/authors/${slotProps.data.id}/edit`">Edit</router-link>
          <button @click="deleteAuthor(slotProps.data.id)">Delete</button>
        </template>
      </Column>
    </DataTable>
    <p v-else>Loading authors...</p>
  </div>
</template>

<script>
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import api from '../services/api';

export default {
  name: 'AuthorList',
  components: {
    DataTable,
    Column,
  },
  data() {
    return {
      authors: [],
      sortField: '',
      sortOrder: 1,
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

    onSort(event) {
      this.sortField = event.sortField;
      this.sortOrder = event.sortOrder;
      this.authors.sort((a, b) => {
        let valueA = a[this.sortField];
        let valueB = b[this.sortField];

        if (typeof valueA === 'string') {
          valueA = valueA.toLowerCase();
          valueB = valueB.toLowerCase();
        }

        if (valueA < valueB) {
          return -1 * this.sortOrder;
        } else if (valueA > valueB) {
          return 1 * this.sortOrder;
        } else {
          return 0;
        }
      });
    },
  },
  mounted() {
    console.log('Mounted');
    this.fetchAuthors();
  },
};
</script>
