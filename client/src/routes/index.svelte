<script lang="ts" context="module">
	import type { DataIn } from '$lib/types';
	import type { LoadEvent } from '@sveltejs/kit';

	export async function load({ fetch }: LoadEvent) {
		const response = await fetch(
			`${import.meta.env.VITE_ETRNAL_SERVICE}/api/items?page=1&page_id=NDk=`
		);

		if (response.ok) {
			const { page_id, records } = (await response.json()) as DataIn;
			return {
				props: {
					nextPage: page_id,
					records
				}
			};
		}

		return {
			props: {
				nextPage: 'NDk=',
				records: []
			}
		};
	}
</script>

<script lang="ts">
	import { browser } from '$app/env';
	import Grid from '$lib/components/Grid.svelte';
	import { handleHotKeys, handleMouseWheel } from '$lib/events';
	import { stored } from '$lib/stores/preview';
	import type { Direction, Record } from '$lib/types';

	let y = 0;
	let page = 2;
	let axisY = 0;
	let current = 0;
	let anchor = false;

	export let records: Record[];
	export let nextPage: string;

	let children: Record[] = [];

	const scrolling = (direction: Direction) => {
		const isScrollingUp = direction === 'Up';
		isScrollingUp ? (current -= 1) : (current += 1);

		const pixels = y;
		const innerHeight = window.innerHeight;
		const negative = pixels - innerHeight;

		y = isScrollingUp ? (negative > 0 ? negative : 0) : pixels + innerHeight;
	};

	const fetcher = async () => {
		const args = [`page=${page}`, `page_id=${nextPage}`];
		const res = await fetch(`${import.meta.env.VITE_ETRNAL_SERVICE}/api/items?${args.join('&')}`, {
			method: 'GET',
			headers: new Headers({
				'Content-Type': 'application/json'
			})
		});

		if (res.ok) {
			const { page_id: pageID, records: items } = await res.json();

			nextPage = pageID;
			children = items;
			anchor = false;
			page++;
		}
	};

	$: {
		if (browser && $stored.infinity) {
			window.scrollTo({
				top: y
			});
		}
	}

	$: if (browser) {
		document.body.style.overflow = $stored.infinity ? 'hidden' : '';
	}

	$: if (axisY) {
		const element = document.documentElement;
		if (axisY >= element.offsetHeight * 0.5 && !anchor) {
			anchor = true;
			fetcher();
		}
	}

	$: {
		records = [...records, ...children];
	}
</script>

<svelte:window
	bind:scrollY={axisY}
	on:keydown={(event) => handleHotKeys(event, scrolling)}
	on:wheel={(event) => handleMouseWheel(event, scrolling)}
	on:contextmenu|preventDefault
/>

<svelte:head>
	<title>etrnal | Infinity Design</title>
</svelte:head>

<Grid children={records} />
