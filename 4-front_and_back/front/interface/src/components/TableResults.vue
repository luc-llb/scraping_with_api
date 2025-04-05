<script setup lang="ts">
import { ref } from 'vue';
import { defineProps } from 'vue';
import Operadora from '@/models/Operadora';

const itemSelecionado = ref({} as Operadora);
const mostrarModal = ref(false);

const props = defineProps({
  items: {
    type: Array<Operadora>,
    required: true,
    default: []
  },
  firstAccess: {
    type: String,
    default: ""
  },
});

const detalhar = function (item: Operadora) {
  itemSelecionado.value = item;
  mostrarModal.value = true;
}

const closeModal = function () {
  mostrarModal.value = false;
}
</script>

<template>
    <div v-if="items.length > 0">
        <table class="table">
          <thead>
            <tr>
                <th>Registro ANS</th>
                <th>CNPJ</th>
                <th>Nome Fantasia</th>
                <th>Endereço eletrônico</th>
                <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(item, index) in items" :key="index">
                <td>{{ item.registro_ans }}</td>
                <td>{{ item.cnpj }}</td>
                <td>{{ item.nome_fantasia }}</td>
                <td>{{ item.endereco_eletronico }}</td>
                <td style="padding: 10px;"><a @click.prevent="detalhar(item)">Detalhar</a></td>
            </tr>
          </tbody>
        </table>
    </div>
    <div v-else-if="firstAccess === ''">
        <h2>Selecione um método de busca e informe o que deseja buscar</h2>
        <p>
            Após clicar no botão "Buscar" será gerada uma tabela contentendo até 10
            operadoras que atendam a sua busca.
        </p>
    </div>
    <div v-else>
        <h2>Não foram encontrados resultados</h2>
        <p>Verifique se o conteúdo digitado está correto.</p>
    </div>

    <div v-if="mostrarModal" class="modal">
    <div class="modal-content">
      <h3>Detalhes</h3>
      <p><strong>Registro ANS:</strong> {{ itemSelecionado.registro_ans }}</p>
      <p><strong>CNPJ:</strong> {{ itemSelecionado.cnpj }}</p>
      <p><strong>Nome Fantasia:</strong> {{ itemSelecionado.nome_fantasia }}</p>
      <p><strong>Modalidade:</strong> {{ itemSelecionado.modalidade }}</p>
      <p><strong>Endereço:</strong> {{itemSelecionado.logradouro}}, {{itemSelecionado.numero}}, {{itemSelecionado.complemento}}, 
        {{itemSelecionado.bairro}}, {{itemSelecionado.cidade}}/{{itemSelecionado.uf}} - {{ itemSelecionado.cep }}</p>
      <p><strong>Telefone:</strong> ({{ itemSelecionado.ddd }}) {{ itemSelecionado.telefone }}</p>
      <p><strong>Fax:</strong> {{ itemSelecionado.fax }}</p>
      <p><strong>Email:</strong> {{ itemSelecionado.endereco_eletronico }}</p>
      <p><strong>Representante:</strong> {{ itemSelecionado.representante }}</p>
      <p><strong>Cargo do Representante:</strong> {{ itemSelecionado.cargo_representante }}</p>
      <p><strong>Região de Comercialização:</strong> {{ itemSelecionado.regiao_de_comercializacao }}</p>
      <p><strong>Data de Registro ANS:</strong> {{ itemSelecionado.data_registro_ans }}</p>
      <button @click="closeModal">Fechar</button>
    </div>
  </div>
</template>

<style scoped>
.table {
  width: 100%;
  overflow: hidden;
}
.table th {
  background-color: #6A39A7;
  color: white;
  text-align: center;
}
.table tr:nth-child(even) {
  background-color: #e1d9e2;
}
a{
  color: #6A39A7;
  text-decoration: none;
  cursor: pointer;
  text-underline-offset: 2px;
}
a:hover {
  text-decoration: underline;
}
.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
}
.modal-content {
  text-align: left;
  background: white;
  padding: 20px;
  width: 300px;
  margin: 100px auto;
  border-radius: 8px;
  max-height: 70vh;      /* Limita a altura da caixinha */
  overflow-y: auto;
}
.modal-content button {
  background-color: #6A39A7;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
}
.modal-content button:hover {
  background-color: #5a2e8c;
}
</style>