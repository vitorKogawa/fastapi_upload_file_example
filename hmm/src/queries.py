realizado_join_cc_with_account_number = "SELECT cc.NUMERO_CONTA, cr.ID, cr.DATA_CR, cr.VALOR_CR FROM ctcloud.custo_realizado AS cr INNER JOIN ctcloud.conta_publica AS cc ON cr.NUMERO_CONTA = cc.NUMERO_CONTA WHERE cc.NUMERO_CONTA = %s AND cr.DATA_CR >= %s ORDER BY cr.DATA_CR DESC LIMIT 12;"
realizado_join_cc_without_account_number = "SELECT cc.NUMERO_CONTA, cr.ID, cr.DATA_CR, cr.VALOR_CR FROM ctcloud.custo_realizado AS cr INNER JOIN ctcloud.conta_publica AS cc ON cr.NUMERO_CONTA = cc.NUMERO_CONTA WHERE cr.DATA_CR >= %s ORDER BY cr.DATA_CR DESC LIMIT 12;"

planejado_join_cc_with_account_number = "SELECT cc.NUMERO_CONTA, cp.ID, cp.DATA_CP, cp.VALOR_CP FROM ctcloud.custo_planejado AS cp INNER JOIN ctcloud.conta_publica AS cc ON cp.NUMERO_CONTA = cc.NUMERO_CONTA WHERE cc.NUMERO_CONTA = %s AND cp.DATA_CP >= %s ORDER BY cp.DATA_CP DESC LIMIT 12;"
planejado_join_cc_without_account_number = "SELECT cc.NUMERO_CONTA, cp.ID, cp.DATA_CP, cp.VALOR_CP FROM ctcloud.custo_planejado AS cp INNER JOIN ctcloud.conta_publica AS cc ON cp.NUMERO_CONTA = cc.NUMERO_CONTA WHERE cp.DATA_CP >= %s ORDER BY cp.DATA_CP DESC LIMIT 12;"

orcado_join_cc_with_account_number = "SELECT cc.NUMERO_CONTA, co.ID, co.DATA_CO, co.VALOR_CO FROM ctcloud.custo_orcado AS co INNER JOIN ctcloud.conta_publica AS cc ON co.NUMERO_CONTA = cc.NUMERO_CONTA WHERE cc.NUMERO_CONTA = %s AND co.DATA_CO >= %s ORDER BY co.DATA_CO DESC LIMIT 12;"
orcado_join_cc_without_account_number = "SELECT cc.NUMERO_CONTA, co.ID, co.DATA_CO, co.VALOR_CO FROM ctcloud.custo_orcado AS co INNER JOIN ctcloud.conta_publica AS cc ON co.NUMERO_CONTA = cc.NUMERO_CONTA WHERE co.DATA_CO >= %s ORDER BY co.DATA_CO DESC LIMIT 12;"


select_item_realizado = "SELECT * FROM ctcloud.custo_realizado as cr WHERE cr.numero_conta = %s AND cr.id = %s;"
select_item_planejado = "SELECT * FROM ctcloud.custo_planejado as cp WHERE cp.numero_conta = %s AND cp.id = %s;"
select_item_orcado = "SELECT * FROM ctcloud.custo_orcado as co WHERE co.numero_conta = %s AND co.id = %s;"