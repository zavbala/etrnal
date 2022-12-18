<script lang="ts">
	import Grid from '$lib/components/Grid.svelte';
	import type { Record } from '$lib/types';

	export let data: { records: Record[] };
</script>

<svelte:head>
	<title>Search | ETRNAL</title>
</svelte:head>

{#key data}
	<Grid children={data.records} />
{/key}
