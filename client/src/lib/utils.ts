export const resizer = (link: string) => {
	const [host] = link.match(/dribbble|behance/g) || [];

	switch (host) {
		case 'dribbble':
			return link + '?compress=1&resize=404x316';

		case 'behance':
			return link.replace(/original/g, '404');
	}
};
