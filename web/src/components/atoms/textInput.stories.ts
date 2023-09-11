// textInput.stories.ts

import type { Meta, StoryObj } from '@storybook/vue3';

import textInput from './textInput.vue';

const meta: Meta<typeof textInput> = {
	component: textInput,
};

export default meta;
type Story = StoryObj<typeof textInput>;


export const Visible: Story = {
	render: (args: any) => ({
		components: { textInput },
		setup() {
			return { args };
		},
		template: '<textInput v-bind="args" />',
	}),
	args: {
		label: "Visible text Input",
		visible: true,
	},
};

export const Hidden: Story = {
	render: (args: any) => ({
		components: { textInput },
		setup() {
			return { args };
		},
		template: '<textInput v-bind="args" />',
	}),
	args: {
		...Visible.args,
		label: 'Hidden text Input',
		visible: false,
	},
};