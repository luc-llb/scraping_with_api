<script setup lang="ts">
import { ref } from 'vue';
import BarSearch from './BarSearch.vue';
import TableResults from './TableResults.vue';
import Operadora from '@/models/Operadora';

const operadoras = ref([] as Operadora[]);
const search = ref('');

const callbackApi = async (path: string) => {
  const url = `http://localhost:8000/operadoras/${path}`;
  try {
    const response = await fetch(url, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
    });

    if (!response.ok) {
      throw new Error('Network response was not ok');
    }

    let data = await response.json();
    if (!Array.isArray(data)) {
      data = [data];
    }
    return data;
  } catch (error) {
    console.error('There was a problem with the fetch operation:', error);
    alert('Erro ao buscar operadoras. Verifique se os dados estão corretos.');
    return [];
  }
};

const handleSearch = async (path: string) => {
  const data = await callbackApi(path);
  operadoras.value = data;
};
</script>

<template>
  <div class="card">
  <BarSearch @search="handleSearch"></BarSearch>
  <TableResults :items="operadoras" :firstAccess="search"></TableResults>
  </div>
</template>

<style scoped>
.card {
  display: flex;
  flex-direction: column;
  text-align: center;
  gap: 20px;
  background-color: rgb(245, 245, 245);
  border-radius: 20px;
  padding: 20px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  margin: 20px;
}
</style>