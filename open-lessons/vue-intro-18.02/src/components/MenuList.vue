<script setup lang="ts">
import MenuItem from "@/components/MenuItem.vue"

import { type FoodItem, type FoodType, foodTypes } from "@/types/food.ts"
import { computed, ref } from "vue"

let id = 1
const menu: FoodItem[] = [
  { id: id++, name: 'Cola', type: 'drinks', available: true },
  { id: id++, name: 'Tea', type: 'drinks', available: false },
  { id: id++, name: 'Juice', type: 'drinks', available: true },
  { id: id++, name: 'Caesar', type: 'salads', available: true },
  { id: id++, name: 'Greek Salad', type: 'salads', available: true },
  { id: id++, name: 'Coleslaw', type: 'salads', available: false },
  { id: id++, name: 'Burger', type: 'main', available: true },
  { id: id++, name: 'Pizza', type: 'main', available: true },
  { id: id++, name: 'Steak', type: 'main', available: true },
  { id: id++, name: 'Soup', type: 'main', available: false },
]

const selectedFoodType = ref<FoodType>(foodTypes[0])

const food = computed(() => menu.filter(el => el.type === selectedFoodType.value))

const cartItems = ref<FoodItem[]>([])

function handleMenuItemClick(item: FoodItem) {
  if (item.available) {
    cartItems.value.push(item)
  }
}
</script>
<template>
  <h3>Available today:</h3>

  <select v-model="selectedFoodType">
    <option
      v-for="type in foodTypes"
      :key="type"
      :value="type"
    >
      {{ type }}
    </option>
  </select>

  <ul>
    <MenuItem
      v-for="item in food"
      :key="item.id"
      :name="item.name"
      :class="{
        'not-available': !item.available,
      }"
      @click="handleMenuItemClick(item)"
    />
  </ul>

  <hr>

  <div v-if="!cartItems.length">
    Cart empty
  </div>
  <div v-else>
    <h5>Your food:</h5>
    <ul>
      <li
        v-for="(food, index) in cartItems"
        :key="index"
      >
        {{ food.name }}
      </li>
    </ul>
  </div>
</template>

<style scoped>
.not-available {
  text-decoration: line-through;
}
</style>
