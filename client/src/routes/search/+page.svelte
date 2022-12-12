<script lang="ts">
	import Grid from '$lib/components/Grid.svelte';
	import type { Record } from '$lib/types';

	export let data: Record[];
	$: children = Object.values(data).map((record) => record);
</script>

<svelte:head>
	<title>Search</title>
</svelte:head>

{#key children}
	<Grid {children} />
{/key}
