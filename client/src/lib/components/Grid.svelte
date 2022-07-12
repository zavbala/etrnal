<script lang="ts">
	import AcButton from '$lib/components/ActionButton.svelte';
	import Card from '$lib/components/Record.svelte';
	import { stored, toggle } from '$lib/stores/preview';
	import type { Record } from '$lib/types';

	export let children: Record[];

	const viewRepo = () => {
		window.open('https://github.com/zavbala', '_blank');
	};

	const toggleFullScreen = () => {
		toggle('fullScreen');

		if (!document.fullscreenElement) {
			document.documentElement.requestFullscreen();
		} else {
			if (document.exitFullscreen) {
				document.exitFullscreen();
			}
		}
	};

	const handleTheme = () => {
		toggle('darkMode');
		document.documentElement.classList.toggle('dark');
	};
</script>

<nav
	class="z-10 m-5 p-4 fixed top-0 bg-white flex justify-between align-items shadow-xl rounded-lg"
>
	<div>
		<AcButton icon={$stored.infinity ? 'grip' : 'infinity'} action={() => toggle('infinity')} />
		<AcButton
			icon={$stored.fullScreen ? 'minimize' : 'maximize'}
			action={() => toggleFullScreen()}
		/>
		<AcButton icon={$stored.darkMode ? 'sun' : 'moon'} action={() => handleTheme()} />
	</div>

	<AcButton icon="github" size="lg" action={() => viewRepo()} />
</nav>

<section class="grid {$stored.infinity ? 'grid-cols-1' : 'grid-cols-3 gap-5 my-10'}">
	{#each children as record}
		<Card {record} />
	{/each}
</section>
