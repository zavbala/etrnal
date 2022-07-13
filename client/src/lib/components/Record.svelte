<script lang="ts">
	import AcButton from '$lib/components/ActionButton.svelte';
	import { stored } from '$lib/stores/preview';
	import type { Record } from '$lib/types';
	import { resizer } from '$lib/utils';

	export let record: Record;
	const { cover, owner, source } = record;
	const author = owner.split('/')[3];
</script>

<article
	class="group col-span-1 p-3 {$stored.infinity &&
		'h-screen flex align-items justify-center flex-col'}"
>
	<img
		on:dragstart|preventDefault
		on:click={() => window.open(cover, '_blank')}
		loading="lazy"
		title="Full Size"
		alt={'Art by ' + author}
		src={$stored.infinity ? cover : resizer(cover)}
		class="rounded-lg cursor-zoom-in {$stored.infinity && 'mx-auto h-full'}"
	/>

	<div
		class="mt-3 {!$stored.infinity &&
			'group-hover:opacity-100 opacity-0 transition-all duration-200'} 
			flex justify-between align-items md:opacity-100"
	>
		<span
			title="Author"
			class="dark:text-white text-black uppercase underline underline-offset-8 
			decoration-wavy font-body md:decoration-1 cursor-pointer decoration-blue-700"
			on:click={() => window.open(owner, '_blank')}
		>
			{author}
		</span>
		<AcButton
			size="sm"
			title="Source"
			icon="arrow-trend-up"
			action={() => window.open(source, '_blank')}
			className="transform hover:scale-90 hover:bg-white border-2 border-black dark:border-0"
		/>
	</div>
</article>
