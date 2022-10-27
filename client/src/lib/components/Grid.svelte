<script lang="ts">
	import Card from '$lib/components/Record.svelte';
	import { stored } from '$lib/stores/preview';
	import type { Record } from '$lib/types';

	export let children: Record[];
</script>

<section
	class="grid justify-items-center md:px-0 px-4
	{$stored.infinity ? 'grid-cols-1' : 'md:grid-cols-2 lg:grid-cols-3 gap-5 my-10 grid-cols-1'}"
>
	{#each children as record}
		<Card {record} />
	{/each}
</section>
