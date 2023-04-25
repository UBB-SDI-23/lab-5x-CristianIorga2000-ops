<template>
  <div id="app">
    <nav>
      <ul>
        <li>
          <router-link to="/authors">Authors</router-link>
        </li>
        <li>
          <router-link to="/authors/create">Create Author</router-link>
        </li>
        <li>
          <router-link to="/statistics">Statistics</router-link>
        </li>
      </ul>
    </nav>
    <main>
      <router-view></router-view>
    </main>
  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>

<style>
nav {
  background-color: #f8f9fa;
  padding: 1rem;
}

nav ul {
  list-style-type: none;
  display: flex;
  gap: 1rem;
}

nav li {
  display: inline;
}

nav a {
  text-decoration: none;
  color: #333;
}

nav a:hover {
  color: #007bff;
}

main {
  padding: 2rem;
}
</style>
