<template>
	<li class="nav-item">
	<a class="nav-link active" v-if="currentpage" aria-current="page" href="navlink">{{label}}</a>
	<a class="nav-link" v-else aria-current="page" href="#">{{label}}</a>
	</li>
</template>

<script>
export default {
	props: {
		label: {
			type: String,
			required: true,
		},
		currentpage: {
			type: Boolean,
			default: false	
		},
		navlink: {
			type: String,
			required: true,
		},
	},
	computed: {
		classes() {
			return {
			};
		},
	},
	methods: {
	},
}
</script>