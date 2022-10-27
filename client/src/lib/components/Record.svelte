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
	class="col-span-1 flex flex-col gap-y-5
	{$stored.infinity && 'md:p-0 p-5 h-screen justify-center'}"
>
	<a href={cover} target="_blank" rel="noreferrer">
		<img
			loading="lazy"
			title="Full Size"
			src={resizer(cover)}
			alt={'Art by ' + author}
			on:dragstart|preventDefault
			class="rounded-lg cursor-zoom-in {$stored.infinity && 'mx-auto h-full'}"
		/>
	</a>

	<div class="flex justify-between">
		<button
			title="Author"
			on:click={() => window.open(owner, '_blank')}
			class="dark:text-white text-black uppercase underline underline-offset-8 
			decoration-wavy font-body md:decoration-1 cursor-pointer decoration-blue-700"
		>
			{author}
		</button>

		<AcButton
			size="sm"
			title="Source"
			icon="arrow-trend-up"
			action={() => window.open(source, '_blank')}
			className="transform hover:scale-105 duration-100 hover:bg-white border-2 border-black dark:border-0"
		/>
	</div>
</article>
