<script>
	import { dev } from '$app/environment';
	import { page } from '$app/stores';
	import Controls from '$lib/components/Controls.svelte';
	import Spotlight from '$lib/components/Spotlight.svelte';
	import { stored } from '$lib/stores/preview';
	import { inject } from '@vercel/analytics';

	import '../app.css';

	inject({ mode: dev ? 'development' : 'production' });

	const domain = 'https://etrnal.vercel.app';
	const title = 'Infinite Design, Inspiration Beyond.';
	const description = 'Get daily dose of design inspiration from the best designers in the world.';

	$: pathname = $page.url.pathname;
	$: link = domain + pathname;
</script>

<svelte:head>
	<!-- Open Graph / Facebook -->
	<meta property="og:type" content="website" />
	<meta property="og:url" content={link} />
	<meta property="og:title" content={title} />
	<meta property="og:description" content={description} />
	<meta property="og:image" content={domain + '/banner.png'} />

	<!-- Twitter -->
	<meta property="twitter:card" content="summary_large_image" />
	<meta property="twitter:url" content={link} />
	<meta property="twitter:title" content={title} />
	<meta property="twitter:description" content={description} />
	<meta property="twitter:image" content={domain + '/banner.png'} />
</svelte:head>

<main class="max-w-5xl mx-auto sm:px-5">
	<slot />
</main>

{#if $stored.showSpotlight}
	<Spotlight />
{/if}

<Controls />
