<script>
	import Controls from '$lib/components/Controls.svelte';
	import Spotlight from '$lib/components/Spotlight.svelte';
	import { stored } from '$lib/stores/preview';
	import '../app.css';
</script>

<main class="max-w-5xl mx-auto sm:px-5">
	<slot />
</main>

{#if $stored.showSpotlight}
	<Spotlight />
{/if}

<Controls />
