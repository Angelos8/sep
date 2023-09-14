// Alert.stories.ts

import type { Meta, StoryObj } from '@storybook/vue3';

import Alert from './alert.vue';
import Button from '@/web/src/components/atoms/button.vue';

const meta: Meta<typeof Alert> = {
	component: Alert,
};

export default meta;
type Story = StoryObj<typeof Alert>;

// export default {
// 	title: 'Molecules/Alert',
// 	component: Alert,
// };

// const Template = (args, { argTypes }) => ({
// 	components: { Alert, Button },
// 	props: Object.keys(argTypes),
// 	template: `
// 	  <Alert v-bind="$props" @close="onClose">
// 		This is an alert message.
// 	  </Alert>
// 	`,
// 	methods: {
// 	  onClose() {
// 		console.log('Alert closed');
// 	  },
// 	},
// });

// export const Default = Template.bind({});
// Default.args = {};

export const Info: Story = {
	render: (args: any) => ({
		components: { Alert },
		setup() {
			return { args };
		},
		template: '<Alert v-bind="args" />',
	}),
	args: {
		label: "Information Alert",
		message: "Here is some important information",
	},
};

export const Failure: Story = {
	render: (args: any) => ({
		components: { Alert },
		setup() {
			return { args };
		},
		template: '<Alert v-bind="args" />',
	}),
	args: {
		...Info.args,
		label: 'Failure Alert',
		message: "Letting you know that you failed >:(",
	},
};

export const Success: Story = {
	render: (args: any) => ({
		components: { Alert },
		setup() {
			return { args };
		},
		template: '<Alert v-bind="args" />',
	}),
	args: {
		...Info.args,
		label: 'Success Alert',
		message: "Whoop whoop you passed :)"
	},
};