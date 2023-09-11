// Alert.stories.ts

import type { Meta, StoryObj } from '@storybook/vue3';

import Alert from './alert.vue';

const meta: Meta<typeof Alert> = {
	component: Alert,
};

export default meta;
type Story = StoryObj<typeof Alert>;


export const Info: Story = {
	render: (args: any) => ({
		components: { Alert },
		setup() {
			return { args };
		},
		template: '<Alert v-bind="args" />',
	}),
	args: {
		label: "Alert",
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
		label: 'This is a Secondy Alert',
		primary: false,
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
		label: 'Primary Small',
		primary: true,
		size: 'small',
	},
};