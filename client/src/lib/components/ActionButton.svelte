<script lang="ts">
	export let icon: string;
	export let size: 'sm' | 'md' | 'lg' = 'md';
	export let className = '';
	export let action: () => void;

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
	class="{className} rounded-full w-12 h-12 {sizes} hover:bg-gray-100 bg-white"
	{...element}
	{...$$props}
>
	<i class="{blacklist.includes(icon) ? 'fa-brands' : 'fa-solid'} fa-{icon} text-black block" />
</button>
