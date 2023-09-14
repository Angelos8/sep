// Nav.stories.ts

import type { Meta, StoryObj } from '@storybook/vue3';

import Navbar from './navbar.vue';

const meta: Meta<typeof Navbar> = {
	component: Navbar,
};

export default meta;
type Story = StoryObj<typeof Navbar>;


export const Primary: Story = {
	render: (args: any) => ({
		components: { Navbar},
		setup() {
			return { args };
		},
		template: '<Navbar v-bind="args" />',
	}),
	args: {
		
	},
};