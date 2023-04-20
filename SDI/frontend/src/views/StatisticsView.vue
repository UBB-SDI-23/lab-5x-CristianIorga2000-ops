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
              <div v-if="totalRoyalty !== null">
                <h3>Total Royalty: {{ totalRoyalty }}</h3>
              </div>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12">
              <v-data-table
                :headers="headers"
                :items="totalRoyalty"
                :loading="totalRoyalty === null"
                :no-results-text="totalRoyalty === null ? '' : 'No results found'"
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
      totalRoyalty: null,
      headers: [
        { text: 'Name', value: 'name' },
        { text: 'Email', value: 'email' },
        { text: 'Total Royalty', value: 'total_royalty' },
      ],
    };
  },
  methods: {
    async getTotalRoyalty() {
      try {
        const response = await api.getTotalRoyalty();
        console.log(response);
        this.totalRoyalty = response;
      } catch (error) {
        console.error('Error fetching total royalty:', error);
        this.totalRoyalty = 'Error fetching total royalty';
      }
    },
  },
};
</script>