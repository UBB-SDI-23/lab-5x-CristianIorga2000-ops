<template>
  <div>
    <v-card>
      <v-card-title>
        <span class="text-h4">Statistics</span>
      </v-card-title>
      <v-card-text>
        <v-container>
          <v-row>
            <v-col cols="12">
              <v-btn color="primary" @click="getTotalRoyalty">Get Total Royalty</v-btn>
            </v-col>
            <v-col cols="12">
              <v-data-table
                :headers="headers"
                :items="formattedRoyalty"
                :loading="formattedRoyalty === null"
                :no-results-text="formattedRoyalty === null ? '' : 'No results found'"
              >
              </v-data-table>
            </v-col>
          </v-row>
          <!-- Add more statistics options here -->
        </v-container>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
import AuthorAPI from '@/api/AuthorAPI';
const api = new AuthorAPI();

export default {
  data() {
  return {
    formattedRoyalty: null,
    headers: [
      { text: 'Name', value: 'name' },
      { text: 'Email', value: 'email' },
      { text: 'Bio', value: 'bio' },
      { text: 'Created At', value: 'created_at' },
      { text: 'Updated At', value: 'updated_at' },
      { text: 'Total Royalty', value: 'total_royalty' },
    ],
  };
},

  methods: {
    async getTotalRoyalty() {
  try {
    const data = await api.getTotalRoyalty();
    console.log("Fetched data:", data);

    this.formattedRoyalty = data.map(author => ({
      name: author.name,
      email: author.email,
      bio: author.bio,
      created_at: author.created_at,
      updated_at: author.updated_at,
      total_royalty: author.total_royalty,
    }));

    console.log("Formatted data:", this.formattedRoyalty);
  } catch (error) {
    console.error("Error fetching total royalty:", error);
    this.formattedRoyalty = [];
  }
},
  },
};
</script>
