import { writable } from 'svelte/store';

const initValues = {
	infinity: false,
	darkMode: false,
	fullScreen: false
};

export const stored = writable(initValues);

type Keys = keyof typeof initValues;

export const toggle = (key: Keys) => {
	stored.update((value) => {
		return { ...value, [key]: !value[key] };
	});
};
