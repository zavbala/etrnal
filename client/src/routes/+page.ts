import type { DataIn } from '$lib/types';
import type { LoadEvent } from '@sveltejs/kit';

export async function load({ fetch }: LoadEvent) {
	const response = await fetch(
		`${import.meta.env.VITE_ETRNAL_SERVICE}/api/items?page=1&page_id=NDk=`
	);

	if (response.ok) {
		const { page_id, records } = (await response.json()) as DataIn;

		return {
			nextPage: page_id,
			records
		};
	}

	return {
		nextPage: 'NDk=',
		records: []
	};
}
