<script lang="ts">
	import ActionButton from '$lib/components/ActionButton.svelte';
	import { stored, toggle } from '$lib/stores/preview';
	import { fly } from 'svelte/transition';

	const style =
		'z-40 p-4 flex-col fixed shadow-lg rounded-lg bg-white flex justify-around align-items';

	const toggler =
		'z-40 fixed w-20 h-20 block md:right-10 md:bottom-8 right-4 bottom-3 shadow-lg rounded-full bg-white';

	let opened = false;

	$: buttons = [
		{
			title: 'Search',
			icon: 'magnifying-glass',
			action: () => {
				toggle('showSpotlight');
				opened = false;
			}
		},
		{
			title: $stored.fullScreen ? 'Exit Full Screen' : 'Enter Full Screen',
			icon: $stored.fullScreen ? 'minimize' : 'maximize',
			action: () => {
				toggle('fullScreen');
				if (!document.fullscreenElement) {
					document.documentElement.requestFullscreen();
				} else {
					if (document.exitFullscreen) {
						document.exitFullscreen();
					}
				}
			}
		},
		{
			title: $stored.darkMode ? 'Day Mode' : 'Night Mode',
			icon: $stored.darkMode ? 'sun' : 'moon',
			action: () => {
				toggle('darkMode');
				document.documentElement.classList.toggle('dark');
			}
		},
		{
			title: $stored.infinity ? 'Grid Mode' : 'Infinity Mode',
			icon: $stored.infinity ? 'grip' : 'infinity',
			action: () => toggle('infinity'),
			className: 'lg:block hidden'
		},
		{
			title: 'Top',
			icon: 'arrow-up',
			action: () => {
				// Mobile
				document.documentElement.scrollTo({ top: 0 });

				// Large
				stored.update((state) => ({ ...state, y: 0 }));
			}
		},
		{
			title: 'Repo',
			icon: 'github',
			action: () => window.open('https://github.com/zavbala/etrnal', '_blank')
		}
	];
</script>

{#if opened}
	<nav transition:fly class="{style} md:bottom-32 md:right-10 bottom-28 right-4">
		{#each buttons as btn}
			<ActionButton size="lg" className="bg-white w-12 h-12" {...btn} />
		{/each}
	</nav>
{/if}

<ActionButton
	className={toggler}
	icon={opened ? 'x' : 'bars'}
	action={() => (opened = !opened)}
	title={(opened ? 'Close' : 'Open') + ' Menu'}
/>
