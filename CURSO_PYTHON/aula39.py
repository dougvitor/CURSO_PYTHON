primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

resultado_de_qual_eh_maior = 'O {valor_maior} é maior do que {valor_menor}' 

if primeiro_valor > segundo_valor:
    print(
            resultado_de_qual_eh_maior.format(
                valor_maior='primeiro_valor='+primeiro_valor, 
                valor_menor='segundo_valor='+segundo_valor
            )
    )
elif segundo_valor > primeiro_valor:
    print(
            resultado_de_qual_eh_maior.format(
                valor_maior='segundo_valor='+segundo_valor, 
                valor_menor='primeiro_valor='+primeiro_valor
            )
    )
else:
    print(
        f'Os valores {primeiro_valor=} ' 
        f'e {segundo_valor=} são iguais!'
    )
    