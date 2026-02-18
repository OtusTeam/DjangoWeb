<script setup lang="ts">

const props = defineProps({
  name: {
    type: String,
    required: true,
  }
})
</script>

<template>
  <li>{{ name }}</li>
</template>
