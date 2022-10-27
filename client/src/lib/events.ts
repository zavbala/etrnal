import type { Direction } from '$lib/types';

export const handleHotKeys = (event: KeyboardEvent, callback: (value: Direction) => void) => {
	const { key } = event;

	const action = {
		ArrowUp: 'Up',
		ArrowDown: 'Down'
	}[key] as Direction;

	if (action) callback(action);
};

export const handleMouseWheel = (event: WheelEvent, callback: (value: Direction) => void) => {
	const { deltaY } = event;
	const direction = deltaY < 0 ? 'Up' : 'Down';

	callback(direction);
};
