import { ENDPOINT } from '$lib/constant';
import type { DataIn } from '$lib/types';
import type { LoadEvent } from '@sveltejs/kit';

export async function load({ fetch }: LoadEvent) {
	const params = new URLSearchParams({ page: '1', page_id: 'NDk=' });
	const response = await fetch(`${ENDPOINT}/api/items?${params.toString()}`);

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
