import type { Meta, StoryObj } from '@storybook/vue3';

import Fileinput from './fileinput.vue';

const meta: Meta<typeof Fileinput> = {
	component: Fileinput,
};

export default meta;
type Story = StoryObj<typeof Fileinput>;


export const Primary: Story = {
	render: (args: any) => ({
		components: { Fileinput },
		setup() {
			return { args };
		},
		template: '<Fileinput v-bind="args" />',
	}),
	args: {
		
	},
};