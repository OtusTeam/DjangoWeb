export const foodTypes = [
  'drinks',
  'salads',
  'main',
] as const
export type FoodType = typeof foodTypes[number]


export interface FoodItem {
  id: number;
  name: string;
  type: FoodType;
  available: boolean;
}

