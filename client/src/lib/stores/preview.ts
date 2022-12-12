import { writable } from 'svelte/store';
import { browser } from '$app/environment';

const initValues = {
	y: 0,
	infinity: false,
	darkMode: false,
	fullScreen: false,
	isScrolling: false,
	showSpotlight: false
};

export const stored = writable(initValues);

type Keys = keyof typeof initValues;

export const toggle = (key: Keys) => {
	stored.update((value) => {
		return { ...value, [key]: !value[key] };
	});
};

stored.subscribe((value) => {
	// Store values in localStorage
	if (browser) {
		const color = value.darkMode ? 'dark' : 'light';
		localStorage.setItem('theme', color);
	}
});
