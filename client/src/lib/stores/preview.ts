import { writable } from 'svelte/store';

const initValues = {
	y: 0,
	infinity: false,
	darkMode: false,
	fullScreen: false,
	isScrolling: false
};

export const stored = writable(initValues);

type Keys = keyof typeof initValues;

export const toggle = (key: Keys) => {
	stored.update((value) => {
		return { ...value, [key]: !value[key] };
	});
};
