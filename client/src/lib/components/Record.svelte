<script lang="ts">
	import AcButton from '$lib/components/ActionButton.svelte';
	import { stored } from '$lib/stores/preview';
	import type { Record } from '$lib/types';
	import { resizer } from '$lib/utils';

	export let record: Record;
	const { cover, owner } = record;
	const author = owner.split('/')[3];

	let showControls = false;
	const infinity = 'flex flex-col justify-center items-end gap-y-2 h-screen';

	const actions = {
		owner: {
			title: 'Author',
			icon: 'user'
		},
		source: {
			title: 'Source',
			icon: 'arrow-trend-up'
		},
		cover: {
			title: 'Full Size',
			icon: 'magnifying-glass-plus'
		}
	};

	const external = (key: string) => window.open(record[key as keyof typeof actions], '_blank');
</script>

<article
	on:mouseenter={() => (showControls = true)}
	on:mouseleave={() => (showControls = false)}
	class="col-span-1 relative {$stored.infinity && infinity}"
>
	<img
		alt=""
		loading="lazy"
		class="rounded-lg"
		src={resizer(cover)}
		title="Art by {author}"
		on:dragstart|preventDefault
	/>

	<div
		class="opacity-100 bg-black/60 flex items-center rounded-2xl transition-all duration-150 p-2
		{showControls ? 'lg:opacity-100 z-40' : 'lg:opacity-0 z-0'}
		{$stored.infinity ? 'static' : 'absolute top-3 right-3'}"
	>
		{#each Object.entries(actions) as [key, props]}
			<AcButton size="sm" className="text-white w-9 h-9" action={() => external(key)} {...props} />
		{/each}
	</div>
</article>
