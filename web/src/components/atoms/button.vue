<template>
	<button type="button" :class="classes" @click="onClick" :style="style">{{ label }}</button>
</template>

<script>
export default {
	props: {
		label: {
			type: String,
			required: true,
		},
		primary: {
			type: Boolean,
			default: false,
		},
		size: {
			type: String,
		},
	},
	computed: {
		classes() {
			return {
				'btn': true,
				'btn-primary': this.primary,
				'btn-secondary': !this.primary,
				'btn-sm': this.size === "small",
				'btn-lg': this.size === "large",
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