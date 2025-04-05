-- Show the top 10 health insurance companies with the highest expenses in the last 3 months.
SELECT 
	ops.cnpj,
    ops.registro_ans,
    ops.razao_social,
    SUM(dc.vl_saldo_final) AS total_despesas
FROM demonstracoes_contabeis dc
JOIN operadoras_de_plano_de_saude_ativas ops
    ON dc.reg_ans = ops.registro_ans
WHERE 
    dc._data >= DATE_SUB(STR_TO_DATE('2024-12-31', '%Y-%m-%d'), INTERVAL 3 MONTH)
    AND dc.descricao LIKE REPLACE('EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR', ' ', '%')
GROUP BY ops.cnpj
ORDER BY total_despesas DESC
LIMIT 10;

-- Show the top 10 health insurance companies with the highest expenses in the last year.
SELECT
	ops.cnpj,
    ops.registro_ans,
    ops.razao_social,
    SUM(dc.vl_saldo_final) AS total_despesas
FROM demonstracoes_contabeis dc
JOIN operadoras_de_plano_de_saude_ativas ops
    ON dc.reg_ans = ops.registro_ans
WHERE 
    dc._data >= DATE_SUB(STR_TO_DATE('2024-12-31', '%Y-%m-%d'), INTERVAL 1 YEAR)
    AND dc.descricao LIKE REPLACE('EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR', ' ', '%')
GROUP BY ops.cnpj
ORDER BY total_despesas DESC
LIMIT 10;
