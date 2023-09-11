import path from 'path'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'


// https://vitejs.dev/config/
export default defineConfig({
	root: path.resolve(__dirname, 'src'),
  plugins: [vue()],
  resolve: {
    alias: {
		'~bootstrap': path.resolve(__dirname, 'node_modules/bootstrap'),
    },
  },
})
