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
          style="width: 300px; height: 40px"
        />
      </div>
      <div class="mb-3">
        <label for="exampleFormControlInput2" class="form-label">Username</label><br />
        <input
          class="form-control"
          id="exampleFormControlInput2"
          placeholder="username"
          style="width: 300px; height: 40px"
        />
      </div>
      <div class="mb-3">
        <label for="inputPassword5" class="form-label">Password</label><br />
        <input
          type="password"
          id="inputPassword5"
          class="form-control"
          aria-describedby="passwordHelpBlock"
          style="width: 300px; height: 40px"
        />
        <div id="passwordHelpBlock" class="form-text">
          Your password must be 8-20 characters long, contain letters and numbers, and must not
          contain spaces, special characters, or emoji.
        </div>
      </div>
      <div class="col-auto">
        <button type="submit" class="btn btn-primary mb-3">Submit</button>
      </div>
    </form>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  computed: {
    ...mapGetters(['role'])
  },
  methods: {
    ...mapActions(['clearRole']),
    async onSubmit(event) {
      event.preventDefault()
      const email = document.getElementById('exampleFormControlInput1').value
      const username = document.getElementById('exampleFormControlInput2').value
      const password = document.getElementById('inputPassword5').value
      const role = this.role

      const userData = {
        email,
        username,
        password,
        role
      }

      try {
        const response = await fetch('http://localhost:8085/auth/register', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(userData)
        })

        if (!response.ok) {
          throw new Error(`An error has occurred: ${response.status}`)
        }

        this.$router.push('/login')

        this.clearRole()

        const data = await response.json()
        console.log(data)
      } catch (error) {
        console.error(error)
      }
    }
  }
}
</script>

<style>
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}
.something {
  cursor: pointer;
}
</style>
