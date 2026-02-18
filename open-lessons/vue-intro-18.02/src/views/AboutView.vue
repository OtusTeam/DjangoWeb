<script setup lang="ts">
import { ref } from "vue"

const userName = ref<string | null>("")
</script>

<template>
  <div class="about">
    <h1>Hello, {{ userName }}</h1>
    <div>
      <input
        v-model="userName"
        placeholder="What is your name?"
      >
    </div>
  </div>
</template>

<style>

</style>
