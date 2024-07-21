<script>
import BootstrapForm from '@/components/login/BootstrapForm.vue'

export default {
  components: {
    BootstrapForm
  }
}
</script>
<style scoped>
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}
</style>
<template>
  <h2 class="green">Login</h2>
  <BootstrapForm />
</template>
