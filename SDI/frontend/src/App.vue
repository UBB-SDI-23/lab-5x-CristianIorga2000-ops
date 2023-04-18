<template>
<div id="app">
  <AuthorCrud />
  <BookCrud />
  <ReviewCrud />
  <AuthorshipCrud />
</div>
</template>

<script>

import AuthorCrud from "./components/AuthorCrud.vue";
import BookCrud from "./components/BookCrud.vue";
import ReviewCrud from "./components/ReviewCrud.vue";
import AuthorshipCrud from "./components/AuthorshipCrud.vue";


export default {
  name: 'App',

  components: {
  AuthorCrud,
  BookCrud,
  ReviewCrud,
  AuthorshipCrud,
},


  data: () => ({
    //
  }),
}
</script>
