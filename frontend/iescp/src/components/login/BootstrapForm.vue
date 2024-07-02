<template>
    <div class="container">
        <form @submit="onSubmit">
            <div class="mb-3">
                <label for="exampleFormControlInput1" class="form-label">Email address</label><br>
                <input type="email" class="form-control" id="exampleFormControlInput1" placeholder="name@example.com">
            </div>
            <div class="mb-3">
                <label for="inputPassword5" class="form-label">Password</label><br>
                <input type="password" id="inputPassword5" class="form-control" aria-describedby="passwordHelpBlock">
                <div id="passwordHelpBlock" class="form-text">
                    Your password must be 8-20 characters long, contain letters and numbers, and must not contain
                    spaces,
                    special characters, or emoji.
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
export default {
    data() {
        return {
            text: 'something'
        }
    },
    methods: {
        async onSubmit(event) {
            event.preventDefault();
            const response = await fetch("http://localhost:8085/login");
            if (!response.ok) {
                const message = `An error has occurred: ${response.status}`
                throw new Error(message)
            }
            const data = await response.json();
            return data;
        }
    }
}
</script>
