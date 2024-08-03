<template>
  <div class="container">
    <form @submit="onSubmit">
      <div class="mb-3">
        <label for="exampleFormControlInput1" class="form-label">Email address</label><br />
        <input
          type="email"
          class="form-control"
          id="exampleFormControlInput1"
          placeholder="name@example.com"
          style="width: 300px; height: 40px;"
        />
      </div>
      <div class="mb-3">
        <label for="exampleFormControlInput2" class="form-label">Username</label><br />
        <input class="form-control" id="exampleFormControlInput2" placeholder="username" style="width: 300px; height: 40px;"/>
      </div>
      <div class="mb-3">
        <label for="inputPassword5" class="form-label">Password</label><br />
        <input
          type="password"
          id="inputPassword5"
          class="form-control"
          aria-describedby="passwordHelpBlock"
          style="width: 300px; height: 40px;"
        />
        <div id="passwordHelpBlock" class="form-text">
          Your password must be 8-20 characters long, contain letters and numbers, and must not
          contain spaces, special characters, or emoji.
        </div>
      </div>
      <div class="col-auto">
        <button type="submit" class="btn btn-primary mb-3" :class="text">Submit</button>
      </div>
    </form>
  </div>
</template>

<style>
.container {
  display: flex;
  flex-direction: column;
}

.something {
  cursor: pointer;
}
</style>

<script>
import { mapActions } from 'vuex';

export default {
  data() {
    return {
      text: 'something'
    }
  },
  methods: {
    ...mapActions(['clearRole']),
    async onSubmit(event) {
      event.preventDefault()
      // const email = document.getElementById('exampleFormControlInput1').value
      const username = document.getElementById('exampleFormControlInput2').value
      const password = document.getElementById('inputPassword5').value
      
      this.clearRole()
      // console.log(roles);
      const userData = {
        username,
        password,
        // roles
      }

      const response = await fetch('http://localhost:8085/auth/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        credentials: 'include',
        body: JSON.stringify(userData)
      })

      if (!response.ok) {
        const message = `An error has occurred: ${response.status}`
        throw new Error(message)
      }
      const data = await response.json()

      if (data.role === "Admin") {
        this.$router.push('/admin/dashboard')
      } else if (data.role === "Influencer") {
        this.$router.push('/influencer/dashboard')
      } else if (data.role === "Sponsor") {
        this.$router.push('/sponsor/dashboard')
      }
      console.log(data)
      // console.log(roles);      
    }
  }
}
</script>
