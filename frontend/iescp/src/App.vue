<template>
  <div id="app">
    <nav>
      <router-link to="/">Register</router-link>
      <router-link to="/login/role">Login</router-link>
    </nav>
    <router-view></router-view>
  </div>
</template>

<style scoped>
router-link {
  font-size: 15px;
}
</style>
