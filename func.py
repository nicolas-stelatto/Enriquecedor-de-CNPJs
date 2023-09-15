import time
import requests
import pandas as pd


def clean_cnpj(cnpj_list):
    # Removes ".", "/" and "-" from CNPJs in a list of CNPJs
    
    cnpj_list_clean = []
    for cnpj in cnpj_list:
        step1 = cnpj.replace('.', '').replace('/', '').replace('-', '')
        if len(step1) < 13:
            cnpj_list_clean.append(step1.zfill(13))
        else:
            cnpj_list_clean.append(step1)

    return cnpj_list_clean



def consultar_cnpj(cnpj_list, url_base, headers):
    # Function to get Receita CNPJs for a list of CNPJs, respecting the 30seg interval between requests
    
    last_request_time = None
    request_interval = 30
    cnpjs_info = []
    cnpjs_rejected = []
    
    for company in cnpj_list:
        # Looping through CNPJs, respecting the request_interval time
        if not last_request_time:
            last_request_time = time.time()
        else:
            elapsed_time = time.time() - last_request_time
            
            if elapsed_time < request_interval:
                time.sleep(request_interval - elapsed_time)
            last_request_time = time.time()
        
        # Requesting response from API    
        url = url_base + company
        response = requests.get(url, headers=headers)
        data = response.json()

        
        if response.status_code == 200 and data['status'] == 'OK':
            cnpj = data['cnpj']
            abertura = data['abertura']
            situacao = data['situacao']
            tipo = data['tipo']
            nome = data['nome']
            porte = data['porte']
            uf = data['uf']
            capital_social = data['capital_social']
            status = data['status']
            natureza_juridica = data['natureza_juridica']
            atividade_principal = data['atividade_principal'][0]['code']
        
            atividade_secundaria = []
            for atividade in data['atividades_secundarias']:
                atividade_secundaria.append(atividade['code'])
        
            while len(atividade_secundaria) < 99:
                atividade_secundaria.append(None)

            cnpjs_info.append([cnpj, abertura, situacao, tipo, nome, porte, uf, capital_social, status, natureza_juridica, atividade_principal, *atividade_secundaria])
            print(cnpj)
        else:
            cnpjs_rejected.append(company)
        
     # Salvar dados em uma database
    empresas_df = pd.DataFrame(cnpjs_info, columns=['cnpj', 'data_abertura', 'situacao_fiscal', 'tipo', 'razao_social', 'porte', 'uf', 'capital_social', 'status', 'natureza_juridica', 'atividade_principal', 'atividade_secundaria_1', 'atividade_secundaria_2', 'atividade_secundaria_3', 'atividade_secundaria_4', 'atividade_secundaria_5', 'atividade_secundaria_6', 'atividade_secundaria_7', 'atividade_secundaria_8', 'atividade_secundaria_9', 'atividade_secundaria_10', 'atividade_secundaria_11', 'atividade_secundaria_12', 'atividade_secundaria_13', 'atividade_secundaria_14', 'atividade_secundaria_15', 'atividade_secundaria_16', 'atividade_secundaria_17', 'atividade_secundaria_18', 'atividade_secundaria_19', 'atividade_secundaria_20', 'atividade_secundaria_21', 'atividade_secundaria_22', 'atividade_secundaria_23', 'atividade_secundaria_24', 'atividade_secundaria_25', 'atividade_secundaria_26', 'atividade_secundaria_27', 'atividade_secundaria_28', 'atividade_secundaria_29', 'atividade_secundaria_30', 'atividade_secundaria_31', 'atividade_secundaria_32', 'atividade_secundaria_33', 'atividade_secundaria_34', 'atividade_secundaria_35', 'atividade_secundaria_36', 'atividade_secundaria_37', 'atividade_secundaria_38', 'atividade_secundaria_39', 'atividade_secundaria_40', 'atividade_secundaria_41', 'atividade_secundaria_42', 'atividade_secundaria_43', 'atividade_secundaria_44', 'atividade_secundaria_45', 'atividade_secundaria_46', 'atividade_secundaria_47', 'atividade_secundaria_48', 'atividade_secundaria_49', 'atividade_secundaria_50', 'atividade_secundaria_51', 'atividade_secundaria_52', 'atividade_secundaria_53', 'atividade_secundaria_54', 'atividade_secundaria_55', 'atividade_secundaria_56', 'atividade_secundaria_57', 'atividade_secundaria_58', 'atividade_secundaria_59', 'atividade_secundaria_60', 'atividade_secundaria_61', 'atividade_secundaria_62', 'atividade_secundaria_63', 'atividade_secundaria_64', 'atividade_secundaria_65', 'atividade_secundaria_66', 'atividade_secundaria_67', 'atividade_secundaria_68', 'atividade_secundaria_69', 'atividade_secundaria_70', 'atividade_secundaria_71', 'atividade_secundaria_72', 'atividade_secundaria_73', 'atividade_secundaria_74', 'atividade_secundaria_75', 'atividade_secundaria_76', 'atividade_secundaria_77', 'atividade_secundaria_78', 'atividade_secundaria_79', 'atividade_secundaria_80', 'atividade_secundaria_81', 'atividade_secundaria_82', 'atividade_secundaria_83', 'atividade_secundaria_84', 'atividade_secundaria_85', 'atividade_secundaria_86', 'atividade_secundaria_87', 'atividade_secundaria_88', 'atividade_secundaria_89', 'atividade_secundaria_90', 'atividade_secundaria_91', 'atividade_secundaria_92', 'atividade_secundaria_93', 'atividade_secundaria_94', 'atividade_secundaria_95', 'atividade_secundaria_96', 'atividade_secundaria_97', 'atividade_secundaria_98', 'atividade_secundaria_99'])
    return empresas_df, cnpjs_rejected