export const APP_NAME = 'etrnal';

export const ENDPOINT =
	process.env.NODE_ENV === 'development'
		? 'http://localhost:8000'
		: import.meta.env.VITE_ETRNAL_SERVICE;
