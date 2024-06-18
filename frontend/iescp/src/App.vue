<template>
	<div id="app">
		<nav>
			<router-link to="/">Login</router-link>
			<router-link to="/register">Register</router-link>
		</nav>
		<router-view></router-view>
	</div>
</template>


<style scoped>
	router-link {
		font-size: 15px;
	}
</style>
