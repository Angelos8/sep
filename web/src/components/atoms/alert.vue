<template>
	<div>{{ label }}</div>
</template>

<script>
export default {
	props: {
		label: {
			type: String,
			required: true,
		},
	},
	computed: {
		classes() {
			return {
				'btn': true,
			};
		},
	},
	methods: {
		onClick() {
			alert('clicked');
		},
	},
}
</script>