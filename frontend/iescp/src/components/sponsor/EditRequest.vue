<template>
  <div class="container">
    <form @submit.prevent="submitForm">
      <div class="form-group">
        <label for="desc">Description:</label>
        <input type="text" class="form-control" id="desc" v-model="desc" />
      </div>
      <div class="form-group">
        <label for="req">Requirements:</label>
        <input type="text" class="form-control" id="req" v-model="req" />
      </div>
      <div class="form-group">
        <label for="amount">Payment Amount:</label>
        <input type="number" class="form-control" id="amount" v-model="amount" />
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  data() {
    return {
      desc: '',
      req: '',
      amount: ''
    }
}
}
</script>