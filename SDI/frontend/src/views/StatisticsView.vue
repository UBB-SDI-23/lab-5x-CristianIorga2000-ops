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
            <!-- Add more statistics options here -->
          </v-container>
        </v-card-text>
      </v-card>
    </div>
  </template>
  
  <script>
  import AuthorAPI from '@/api/AuthorAPI';
  
  export default {
    data() {
      return {
        totalRoyalty: null,
      };
    },
    methods: {
      async getTotalRoyalty() {
        try {
          const response = await AuthorAPI.getTotalRoyalty();
          this.totalRoyalty = response.data.total_royalty;
        } catch (error) {
          console.error('Error fetching total royalty:', error);
          this.totalRoyalty = 'Error fetching total royalty';
        }
      },
    },
  };
  </script>
  
  