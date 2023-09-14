import type { Meta, StoryObj } from '@storybook/vue3';

import NavItem from './nav_item.vue';

const meta: Meta<typeof NavItem> = {
	component: NavItem,
};

export default meta;
type Story = StoryObj<typeof NavItem>;


export const Primary: Story = {
	render: (args: any) => ({
		components: { NavItem },
		setup() {
			return { args };
		},
		template: '<NavItem v-bind="args" />',
	}),
	args: {
		label: "My Page",
		currentpage: true,
		navlink: "#",
	},
};