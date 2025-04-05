<script setup lang="ts">
import { ref, defineEmits } from 'vue';
import Operadora from '@/models/Operadora';

const searchQuery = ref('');
const searchOption = ref('');
const emit = defineEmits(['search']);
const selectedOption = ["CNPJ", "Registro ANS", "Nome Fantasia", "Endereco Eletrônico", "Modalidade", "Data de Registro"];
const valueOptions = ["cnpj", "registro_ans", "nome_fantasia", "endereco_eletronico", "modalidade", "data_registro"];

const handleInput = (event: Event) => {
    const target = event.target as HTMLInputElement;
    searchQuery.value = target.value;
};

const onClick = () => {
    const data: Operadora[] = [];
    if (searchQuery.value === '') {
        alert('Digite algo para buscar!');
    } else if(searchOption.value === '') {
        alert('Selecione uma opção para buscar!');
    }else {
        emit('search', searchOption.value + '/' + searchQuery.value);
    }
};

</script>

<template>
    <div class="container">
        <select v-model="searchOption" class="select">
            <option value="">Buscar por</option>
            <option v-for="(option, index) in selectedOption" :key="index" 
            :value="valueOptions[index]">{{ option }}</option>
        </select>
        <input
          type="text"
          placeholder="Pesquisar..."
          v-model="searchQuery"
          @input="handleInput"
          class="search-input"
        /> 
        <button @click="onClick" class="search-button">Buscar</button>
    </div>
</template>

<style scoped>
.container {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 20px;
}
.select {
    padding: 10px;
    border-radius: 5px;
    border: 1px solid #ccc;
    border-color: #555555;
    background-color: #EBEBEB;
    color: #6A39A7;
    margin-right: 10px;
    min-width: 150px;
}
.search-input {
    padding: 10px;
    border-radius: 5px;
    border: 1px solid #ccc;
    border-color: #555555;
    color: #6A39A7;
    width: 200px;
    margin-right: 10px;
    min-width: 40vw;
    &:focus {
        outline: none;
        border-color: #6A39A7;
        box-shadow: 0 0 5px #6A39A7;
    }
}
.search-button {
    padding: 10px 15px;
    border-radius: 5px;
    border: none;
    background-color: #007bff;
    color: white;
    cursor: pointer;
}
.search-button:hover {
    background-color: #0056b3;
    box-shadow: 0 0 2px #0056b3;
}
</style>