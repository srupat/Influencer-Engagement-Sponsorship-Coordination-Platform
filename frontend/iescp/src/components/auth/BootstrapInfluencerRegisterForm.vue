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
      <div class="mb-3">
        <label for="exampleFormControlInput3" class="form-label">Category</label><br />
        <input
          class="form-control"
          id="exampleFormControlInput3"
          placeholder="Category"
          style="width: 300px; height: 40px"
        />
      </div>
      <div class="mb-3">
        <label for="exampleFormControlInput4" class="form-label">Niche</label><br />
        <input
          class="form-control"
          id="exampleFormControlInput4"
          placeholder="Niche"
          style="width: 300px; height: 40px"
        />
      </div>
      <div class="mb-3">
        <label for="exampleFormControlInput5" class="form-label">Followers</label><br />
        <input
          class="form-control"
          id="exampleFormControlInput5"
          placeholder="Followers"
          style="width: 300px; height: 40px"
        />
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
  data() {
    return {
      user: '',
    }
  },
  computed: {
    ...mapGetters(['role']),
    ...mapGetters(['influencerID'])
  },
  mounted() {
    this.clearInfluencerID()
  },
  methods: {
    ...mapActions(['clearRole']),
    ...mapActions(['setInfluencerID']),
    ...mapActions(['clearInfluencerID']),
    async onSubmit(event) {
      event.preventDefault()
      const email = document.getElementById('exampleFormControlInput1').value
      const username = document.getElementById('exampleFormControlInput2').value
      const password = document.getElementById('inputPassword5').value
      const category = document.getElementById('exampleFormControlInput3').value
      const niche = document.getElementById('exampleFormControlInput4').value
      const followers = document.getElementById('exampleFormControlInput5').value
      const role = this.role

      this.user = username
      
      const userData = {
        email,
        username,
        password,
        category,
        niche,
        followers,
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

        const data = await response.json()
        // console.log(data)

        this.$router.push('/login')
        // console.log(this.role)
        this.clearRole()
        await this.fetchAndSetInfluencerID()
        // console.log(this.influencerID)
        
      } catch (error) {
        console.error(error)
      }
    },
    async fetchAndSetInfluencerID() {
      try {
        console.log(this.user);
        const response = await fetch(`http://localhost:8085/influencer/${this.user}`);
        const data = await response.json();
        // console.log(data);
        this.setInfluencerID(data.id);
      } catch (error) {
        console.error(error);
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
