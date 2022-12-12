import { ENDPOINT } from '$lib/constant';
import type { LoadEvent } from '@sveltejs/kit';

export async function load({ fetch, url }: LoadEvent) {
	const query = url.searchParams.get('query') as string;
	const params = new URLSearchParams({ query });
	const response = await fetch(`${ENDPOINT}/api/search?${params.toString()}`);

	if (response.ok) {
		return await response.json();
	}
}
