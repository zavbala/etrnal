<script lang="ts">
	export let icon: string;
	export let className = '';
	export let action: () => void = () => {};
	export let size: 'sm' | 'md' | 'lg' = 'md';

	const element = {
		type: 'button'
	};

	const sizes = {
		sm: 'text-base',
		md: 'text-xl',
		lg: 'text-2xl'
	}[size];

	const blacklist = ['github'];
</script>

<button
	on:click={action}
	class="flex items-center justify-center {className}"
	{...element}
	{...$$props}
>
	<i class="{blacklist.includes(icon) ? 'fa-brands' : 'fa-solid'} fa-{icon} {sizes}" />
</button>
