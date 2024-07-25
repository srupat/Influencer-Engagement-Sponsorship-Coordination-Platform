<template>
    <div class="horizontal-component">
        <div class="message">{{ message }}</div>
        <button class="btn btn-success">View</button>
    </div>
</template>

<script>
export default {
    props: {
        message: {
            type: String,
            required: true
        }
    }
}
</script>

<style scoped>
.horizontal-component {
    display: flex;
    align-items: center;
    justify-content: space-between;
    height: 50px;
    background-color: lightblue; 
    margin-bottom: 20px;
    margin-top: 20px;
    width: 80%;
    border-radius: 10px; 
}
    
.message {
    flex: 1;
    margin: 20px; 
    color: #333; 
    font-size: 20px;
    font-weight: bold;
}

.btn-success {
    height: 30px;
    margin: 30px;
}
</style>

        