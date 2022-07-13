<script lang="ts">
	import ActionButton from '$lib/components/ActionButton.svelte';
	import { stored, toggle } from '$lib/stores/preview';

	$: buttons = [
		{
			title: $stored.infinity ? 'Grid Mode' : 'Infinity Mode',
			icon: $stored.infinity ? 'grip' : 'infinity',
			action: () => toggle('infinity')
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
			title: 'Top',
			icon: 'arrow-up',
			action: () =>
				document.documentElement.scrollTo({
					top: 0
				})
		},
		{
			title: 'Repo',
			icon: 'github',
			action: () => window.open('https://github.com/zavbala/etrnal', '_blank')
		}
	];
</script>

<nav class="z-10 m-5 p-4 fixed top-0 bg-white flex justify-around align-items shadow-xl rounded-lg">
	{#each buttons as btn}
		<ActionButton size="lg" {...btn} />
	{/each}
</nav>
