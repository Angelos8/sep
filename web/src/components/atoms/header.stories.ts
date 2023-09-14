// Header.stories.ts

import type { Meta, StoryObj } from '@storybook/vue3';

import Header from './header.vue';

const meta: Meta<typeof Header> = {
	component: Header,
};

export default meta;
type Story = StoryObj<typeof Header>;


export const Primary: Story = {
	render: (args: any) => ({
		components: { Header },
		setup() {
			return { args };
		},
		template: '<Header v-bind="args" />',
	}),
	args: {
		loggedin: false,
		username: "John Doe",
	},
};
