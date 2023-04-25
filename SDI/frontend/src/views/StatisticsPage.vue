<template>
    <div>
      <h1>Statistics</h1>
      <button @click="fetchTotalRoyalty">Get Total Royalty</button>
      <ul>
        <li v-for="author in totalRoyalty" :key="author.id">
          {{ author.name }}: {{ author.total_royalty }}%
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import api from '../services/api';
  
  export default {
    name: 'StatisticsPage',
    data() {
      return {
        totalRoyalty: [],
      };
    },
    methods: {
      async fetchTotalRoyalty() {
        try {
          const response = await api.getTotalRoyalty();
          this.totalRoyalty = response.data;
        } catch (error) {
          console.error('Error fetching total royalty:', error);
        }
      },
    },
  };
  </script>
  