export interface Record {
	cover: string;
	source: string;
	owner: string;
}

export interface DataIn {
	page_id: string;
	records: Record[];
}

export type Direction = 'Up' | 'Down';
