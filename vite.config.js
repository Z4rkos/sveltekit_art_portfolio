import { sveltekit } from '@sveltejs/kit/vite';

/** @type {import('vite').UserConfig} */
const config = {
	plugins: [sveltekit()],
    fs: {
        allow: [
            './static/global.css'
        ]
    }
};

export default config;
