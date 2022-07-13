export const APP_NAME = 'Etrnal';

export const ENDPOINT =
	process.env.NODE_ENV === 'development'
		? 'http://localhost:5000'
		: import.meta.env.VITE_ETRNAL_SERVICE;
