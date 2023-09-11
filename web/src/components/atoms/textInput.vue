<template>
	<!-- <div> {{ label }}</div>
	<input v-model="text" placeholder="Type here" :class="classes" :style="style"> -->

	<div>
    <label for="textInput">{{ label }}</label>
	<br>
    <input
      type="text"
      id="textInput"
	  :value="visible ? inputValue : maskedValue"
      @input="updateValue"
      :placeholder="placeholder"
    />
  </div>
</template>

<script>
export default {
	props: {
		label: {
			type: String,
			required: true,
		},
		value: {
			type: String,
		},
		placeholder: {
			type: String,
		},
		visible: {
			type: Boolean,
			default: true,
		},
	},
	data() {
		return {
		inputValue: '', // Store the original input value
		};
	},
	computed: {
		classes() {
			return {
				'ipt': true,
				'ipt-visible': this.visible,
				'ipt-hidden': !this.visible,
			};
		},
		maskedValue() {
			// Replace the input value with bullet characters (•)
			return '•'.repeat(this.inputValue.length);
		},
	},
	methods: {
		updateValue(event) {
			// When the input value changes, update the original input value
			this.inputValue = event.target.value;

			// Emit the input event based on the maskInput prop
			if (this.maskInput) {
				this.$emit('input', this.inputValue);
			} else {
				this.$emit('input', this.maskedValue);
			}
		},
  	},
}
</script>