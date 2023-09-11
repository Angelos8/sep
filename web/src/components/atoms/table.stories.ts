// Table.stories.ts

import type { Meta, StoryObj } from '@storybook/vue3';

import Table from './table.vue';

const meta: Meta<typeof Table> = {
	component: Table,
};

export default meta;
type Story = StoryObj<typeof Table>;


export const general_user: Story = {
	render: (args: any) => ({
		components: { Table },
		setup() {
			return { args };
		},
		template: '<Table v-bind="args" />',
	}),
	args: {
		label: "Table for Users",
		admin: false,
	},
};

export const admin_user: Story = {
	render: (args: any) => ({
		components: { Table },
		setup() {
			return { args };
		},
		template: '<Table v-bind="args" />',
	}),
	args: {
		label: "Table for Admins",
		admin: true,
	},
};