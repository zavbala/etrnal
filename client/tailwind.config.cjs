/** @type {import('tailwindcss').Config} */
module.exports = {
	darkMode: 'class',
	content: ['./src/**/*.{html,js,svelte,ts}'],
	theme: {
		fontFamily: {
			body: ['IBM Plex Mono', 'monospace']
		},
		screens: {
			lg: { max: '1536px' },
			md: { max: '1024px' },
			sm: { max: '640px' }
		},
		extend: {}
	},
	plugins: []
};
