<script lang="ts">
	import AcButton from '$lib/components/ActionButton.svelte';
	import { stored } from '$lib/stores/preview';
	import type { Record } from '$lib/types';
	import { resizer } from '$lib/utils';

	export let record: Record;
	const { cover, owner, source } = record;
</script>

<article
	class="group col-span-1 p-3 {$stored.infinity &&
		'h-screen flex align-items justify-center flex-col'}"
>
	<img
		on:dragstart|preventDefault
		on:click={() => window.open(cover, '_blank')}
		loading="lazy"
		src={resizer(cover)}
		alt=""
		class="rounded-lg cursor-zoom-in {$stored.infinity && 'mx-auto h-full'}"
	/>

	<div
		class="mt-3 {!$stored.infinity &&
			'group-hover:opacity-100 opacity-0 transition-all duration-200'} flex justify-between align-items"
	>
		<span
			class="dark:text-white text-black uppercase hover:underline hover:decoration-wavy cursor-pointer decoration-blue-700"
			on:click={() => window.open(owner, '_blank')}
		>
			{owner.split('/')[3]}
		</span>
		<AcButton icon="arrow-trend-up" size="sm" action={() => window.open(source, '_blank')} />
	</div>
</article>
