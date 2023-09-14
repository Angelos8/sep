<template>
	<div class="alert">
		<p>{{ label }}</p>
		<p>{{ message }}</p>
		<Button @click="closeAlert">{{ buttonLabel }}</Button>
    </div>
</template>

<script>
export default {
	props: {
		label: {
			type: String,
			required: true,
		},
		message: {
			type: String,
			required: true,
		},
		buttonLabel: {
			type: String,
			default: "Done",
		}
	},
	computed: {
		classes() {
			return {
				'alt': true,
			};
		},
	},
	// methods: {
	// 	closeAlert() {
	// 	this.$emit('close');
	// 	},
    // },
}
</script>