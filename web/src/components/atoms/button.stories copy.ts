// Button.stories.ts

import type { Meta, StoryObj } from '@storybook/vue3';

import Button from './button.vue';

const meta: Meta<typeof Button> = {
	component: Button,
};

export default meta;
type Story = StoryObj<typeof Button>;


export const Primary: Story = {
	render: (args: any) => ({
		components: { Button },
		setup() {
			return { args };
		},
		template: '<Button v-bind="args" />',
	}),
	args: {
		label: "Button",
		primary: true,
		size: "normal",
	},
};

export const Secondary: Story = {
	render: (args: any) => ({
		components: { Button },
		setup() {
			return { args };
		},
		template: '<Button v-bind="args" />',
	}),
	args: {
		...Primary.args,
		label: 'This is a Secondy Button',
		primary: false,
	},
};

export const Primary_Small: Story = {
	render: (args: any) => ({
		components: { Button },
		setup() {
			return { args };
		},
		template: '<Button v-bind="args" />',
	}),
	args: {
		...Primary.args,
		label: 'Primary Small',
		primary: true,
		size: 'small',
	},
};

export const Secondary_Large: Story = {
	render: (args: any) => ({
		components: { Button },
		setup() {
			return { args };
		},
		template: '<Button v-bind="args" />',
	}),
	args: {
		...Primary.args,
		label: 'Secondy Button Large',
		primary: false,
		size: 'large',
	},
};