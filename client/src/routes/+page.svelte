<script lang="ts">
	import { browser } from '$app/environment';
	import Controls from '$lib/components/Controls.svelte';
	import Grid from '$lib/components/Grid.svelte';
	import { ENDPOINT } from '$lib/constant';
	import { handleHotKeys, handleMouseWheel } from '$lib/events';
	import { stored } from '$lib/stores/preview';
	import type { Direction, Record } from '$lib/types';

	let page = 2;
	let axisY = 0;
	let anchor = false;

	export let data: { records: Record[]; nextPage: string };
	let { nextPage, records } = data;

	let children: Record[] = [];

	const scrolling = (direction: Direction) => {
		const isScrollingUp = direction === 'Up';

		const pixels = $stored.y;
		const innerHeight = window.innerHeight;
		const negative = pixels - innerHeight;

		const value = isScrollingUp ? (negative > 0 ? negative : 0) : pixels + innerHeight;
		stored.update((state) => ({ ...state, y: value }));
	};

	const fetcher = async () => {
		const params = new URLSearchParams({ page: String(page), page_id: nextPage });

		const res = await fetch(`${ENDPOINT}/api/items?${params.toString()}`, {
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

	$: if (browser) {
		document.body.style.overflow = $stored.infinity ? 'hidden' : '';
		if ($stored.infinity) window.scrollTo({ top: $stored.y });
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
	on:keydown={(event) => $stored.infinity && handleHotKeys(event, scrolling)}
	on:wheel={(event) => $stored.infinity && handleMouseWheel(event, scrolling)}
/>

<svelte:head>
	<title>ETRNAL | Infinity Design</title>
</svelte:head>

<Controls />
<Grid children={records} />
