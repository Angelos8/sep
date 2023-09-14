<template>
	<nav class="navbar navbar-expand-lg bg-body-tertiary">
	<div class="container-fluid">
		<a class="navbar-brand" href="#">Attack Flow 4</a> 
		<div class="navbar-text d-flex d-flex flex-row-reverse" v-if="loggedin">
			<div class="p-2">
				<a class="nav-link active" aria-current="page" href="#">{{username}}</a>
			</div>
			<div class="p-2">
				<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-bell-fill" viewBox="0 0 16 16">
				<path d="M8 16a2 2 0 0 0 2-2H6a2 2 0 0 0 2 2zm.995-14.901a1 1 0 1 0-1.99 0A5.002 5.002 0 0 0 3 6c0 1.098-.5 6-2 7h14c-1.5-1-2-5.902-2-7 0-2.42-1.72-4.44-4.005-4.901z"/>
				</svg>
			</div>
		</div>
		<div v-else>
			<a class="nav-link active" aria-current="page" href="#">Log In</a>
		</div>
    </div>
</nav>
</template>

<script>
export default {
	props: {
		loggedin: {
			type: Boolean,
			default: false,
			required: true,
		},
		username: {
			type: String,
		}

	},
	computed: {
		classes() {
			return {
				
			};
		},
	},
	methods: {
		onClick() {
			alert('Should take you back to home page!');
		},
	},
}
</script>