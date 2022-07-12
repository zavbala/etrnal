import { expect, test } from '@playwright/test';
import { resizer } from '../src/lib/utils.js';

const sources = [
	[
		'https://cdn.dribbble.com/upload/original.png',
		'https://cdn.dribbble.com/upload/original.png?compress=1&resize=700x500'
	],
	[
		'https://mir-cdn.behance.net/v1/user/projects/original/0abf11142180905.jpg',
		'https://mir-cdn.behance.net/v1/user/projects/404/0abf11142180905.jpg'
	]
];

for (const source of sources) {
	const [link, expected] = source;
	test(`resize image ${link}`, () => {
		expect(resizer(link)).toBe(expected);
	});
}
