<script lang="ts">
	export let icon: string;
	export let action: () => void;
	export let size: 'sm' | 'md' | 'lg' = 'md';

	const sizes = {
		sm: 'text-base',
		md: 'text-xl',
		lg: 'text-2xl'
	}[size];

	const blacklist = ['github'];
</script>

<button class="rounded-full w-12 h-12 {sizes} hover:bg-gray-100 dark:bg-white" on:click={action}>
	<i class="{blacklist.includes(icon) ? 'fa-brands' : 'fa-solid'} fa-{icon} text-black block" />
</button>
