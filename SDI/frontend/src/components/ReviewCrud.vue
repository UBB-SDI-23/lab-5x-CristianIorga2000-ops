<template>
    <div>
      <h2>Reviews</h2>
      <!-- Add review form -->
      <div>
        <h3>Add Review</h3>
        <form @submit.prevent="createReview">
          <label>Reviewer Name:</label>
          <input type="text" v-model="newReview.reviewer_name" required />
          <label>Rating:</label>
          <input type="number" min="1" max="5" v-model="newReview.rating" required />
          <label>Comment:</label>
          <textarea v-model="newReview.comment"></textarea>
          <button type="submit">Add Review</button>
        </form>
      </div>
      <!-- Review list -->
      <table>
        <thead>
          <tr>
            <th>Reviewer Name</th>
            <th>Rating</th>
            <th>Comment</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="review in reviews" :key="review.id">
            <td>{{ review.reviewer_name }}</td>
            <td>{{ review.rating }}</td>
            <td>{{ review.comment }}</td>
            <td>
              <button @click="startEditReview(review)">Edit</button>
              <button @click="deleteReview(review.id)">Delete</button>
            </td>
          </tr>
        </tbody>
      </table>
      <!-- Edit review form -->
      <div v-if="editingReview">
        <h3>Edit Review</h3>
        <form @submit.prevent="updateReview">
          <input type="hidden" v-model="editingReview.id" />
          <label>Reviewer Name:</label>
          <input type="text" v-model="editingReview.reviewer_name" required />
          <label>Rating:</label>
          <input type="number" min="1" max="5" v-model="editingReview.rating" required />
          <label>Comment:</label>
          <textarea v-model="editingReview.comment"></textarea>
          <button type="submit">Save</button>
          <button @click="cancelEditReview">Cancel</button>
        </form>
      </div>
    </div>
  </template>
  
  <script>
  import ReviewApi from "@/api/review.js";
  
  export default {
    name: "ReviewCrud",
    data() {
      return {
        reviews: [],
        newReview: {
          reviewer_name: "",
          rating: "",
          comment: "",
        },
        editingReview: null,
      };
    },
    async created() {
      await this.fetchReviews();
    },
    methods: {
      async fetchReviews() {
        try {
          const response = await ReviewApi.list();
          this.reviews = response.data;
        } catch (error) {
          console.error("Error fetching reviews:", error);
        }
      },
      async createReview() {
        try {
        await ReviewApi.create(this.newReview);
        await this.fetchReviews();
        this.newReview = { reviewer_name: "", rating: "", comment: "" };
      } catch (error) {
        console.error("Error creating review:", error);
      }
    },
    startEditReview(review) {
      this.editingReview = { ...review };
    },
    async updateReview() {
      try {
        await ReviewApi.update(this.editingReview.id, this.editingReview);
        await this.fetchReviews();
        this.editingReview = null;
      } catch (error) {
        console.error("Error updating review:", error);
      }
    },
    async deleteReview(id) {
      try {
        await ReviewApi.delete(id);
        await this.fetchReviews();
      } catch (error) {
        console.error("Error deleting review:", error);
      }
    },
    cancelEditReview() {
      this.editingReview = null;
    },
  },
};
</script>

  