export default class Operadora {
    id: number;
    registro_ans: number;
    cnpj: string;
    razao_social: string;
    nome_fantasia: string;
    modalidade: string;
    logradouro: string;
    numero: string;
    complemento: string;
    bairro: string;
    cidade: string;
    uf: string;
    cep: string;
    ddd: string;
    telefone: string;
    fax: string;
    endereco_eletronico: string;
    representante: string;
    cargo_representante: string;
    regiao_de_comercializacao: string;
    data_registro_ans: Date;

    constructor(
        id: number = 0,
        registro_ans: number = 0,
        cnpj: string = '',
        razao_social: string = '',
        nome_fantasia: string = '',
        modalidade: string = '',
        logradouro: string = '',
        numero: string = '',
        complemento: string = '',
        bairro: string = '',
        cidade: string = '',
        uf: string = '',
        cep: string = '',
        ddd: string = '',
        telefone: string = '',
        fax: string = '',
        endereco_eletronico: string = '',
        representante: string = '',
        cargo_representante: string = '',
        regiao_de_comercializacao: string = '',
        data_registro_ans: Date = new Date()
    ) {
        this.id = id;
        this.registro_ans = registro_ans;
        this.cnpj = cnpj;
        this.razao_social = razao_social;
        this.nome_fantasia = nome_fantasia;
        this.modalidade = modalidade;
        this.logradouro = logradouro;
        this.numero = numero;
        this.complemento = complemento;
        this.bairro = bairro;
        this.cidade = cidade;
        this.uf = uf;
        this.cep = cep;
        this.ddd = ddd;
        this.telefone = telefone;
        this.fax = fax;
        this.endereco_eletronico = endereco_eletronico;
        this.representante = representante;
        this.cargo_representante = cargo_representante;
        this.regiao_de_comercializacao = regiao_de_comercializacao;
        this.data_registro_ans = data_registro_ans;
    }
}