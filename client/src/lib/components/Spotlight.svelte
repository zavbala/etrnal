<script lang="ts">
	import { goto } from '$app/navigation';
	import { toggle } from '$lib/stores/preview';
	import { blur } from 'svelte/transition';
	import ActionButton from './ActionButton.svelte';

	let query = '';

	const hotkey = (event: KeyboardEvent) => {
		if (event.key === 'Escape') {
			toggle('showSpotlight');
		}
	};

	const init = (node: HTMLInputElement) => node.focus();

	const search = () => {
		const params = new URLSearchParams({ query });
		goto(`/search?${params.toString()}`);
		toggle('showSpotlight');
	};
</script>

<svelte:window on:keydown={hotkey} />

<div
	class="fixed top-0 w-full h-screen bg-gray-50/10 backdrop-blur-md z-50 flex items-center justify-center"
>
	<ActionButton
		icon="x"
		size="sm"
		action={() => toggle('showSpotlight')}
		className="absolute lg:top-3 lg:left-3 bg-white rounded-full p-3 h-10 w-10 bottom-3 right-3"
	/>
	<form
		autocomplete="off"
		class="lg:w-1/2 w-11/12 m-auto bg-white lg:h-32 h-24 rounded-lg shadow-xl relative"
	>
		<small class="text-black lg:block hidden absolute top-4 text-xs left-4"> ESC </small>
		<input
			use:init
			type="search"
			bind:value={query}
			class="h-full text-3xl font-bold text-center uppercase relative"
		/>
		<ActionButton
			type="submit"
			icon="paper-plane"
			className="hover:bg-gray-50 lg:w-16 lg:h-16 w-10 h-10 rounded-full absolute right-5 top-8"
			action={search}
		/>
	</form>
</div>
