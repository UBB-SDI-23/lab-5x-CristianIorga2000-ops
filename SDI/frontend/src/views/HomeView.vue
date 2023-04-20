<template>
    <v-container>
      <v-row class="text-center">
        <v-col>
          <h1>Welcome!</h1>
          <p>
            This is a simple application for managing authors and royalty statistics.
          </p>
        </v-col>
      </v-row>
      <v-row justify="center">
        <v-col cols="12" md="4">
          <v-card
            class="mx-auto"
            color="primary"
            dark
            max-width="400"
            @click="$router.push({ name: 'Authors' })"
          >
            <v-card-title>Authors</v-card-title>
            <v-card-text>Manage authors and their details</v-card-text>
          </v-card>
        </v-col>
        <v-col cols="12" md="4">
          <v-card
            class="mx-auto"
            color="secondary"
            dark
            max-width="400"
            @click="$router.push({ name: 'Statistics' })"
          >
            <v-card-title>Statistics</v-card-title>
            <v-card-text>View royalty statistics</v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </template>
  
  <script>
  export default {
    name: 'HomeView',
  }
  </script>
  