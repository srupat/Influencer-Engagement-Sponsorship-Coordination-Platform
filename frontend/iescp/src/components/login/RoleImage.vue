<template>
  <div class="round-image">
    <img :src="imageUrl" alt="Profile Image" />
  </div>
</template>

<script>
export default {
  props: {
    imageUrl: {
      type: String,
      required: true
    }
  }
}
</script>

<style scoped>
.round-image {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  overflow: hidden;
}

.round-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
</style>
