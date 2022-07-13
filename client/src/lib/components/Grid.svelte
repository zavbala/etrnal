<script lang="ts">
	import Card from '$lib/components/Record.svelte';
	import { stored } from '$lib/stores/preview';
	import type { Record } from '$lib/types';

	export let children: Record[];
</script>

<section
	class="grid justify-items-center {$stored.infinity
		? 'grid-cols-1'
		: 'grid-cols-3 gap-5 my-10 md:grid-cols-2 sm:grid-cols-1'}"
>
	{#each children as record}
		<Card {record} />
	{/each}
</section>
