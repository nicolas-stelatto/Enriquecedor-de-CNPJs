# Import libraries
import pandas as pd
import os
from dotenv import load_dotenv
import csv

# Import functions
from func import clean_cnpj
from func import consultar_cnpj


def main():
    load_dotenv()
    # URL + header + token API ReceitaAWS
    url_base = 'https://www.receitaws.com.br/v1/cnpj/'
    token = os.getenv("API_KEY")
    headers = {'Authorization': 'Bearer ' + token}


    # Relative Path for entry file and output file
    input_file_path = os.path.join('arquivos_entrada', 'cnpjs_bruto.csv')
    current_directory = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(current_directory, input_file_path)
    
    
    # Read CSV file and store CNPJs in a list
    cnpjs_df = pd.read_csv(input_path, delimiter = ";")
    cnpjs_list = list(cnpjs_df['CNPJs'])

    
    # Clean CNPJ list
    cnpj_clean = clean_cnpj(cnpjs_list)

    
    # Get Request for CNPJ list and save do DF
    empresas_df, cnpjs_rejeitados = consultar_cnpj(cnpj_list=cnpj_clean, url_base=url_base, headers=headers)

    
    # Salva as informações em um arquivo CSV
    output_file_relative = os.path.join('arquivos_saida', 'cnpjs_enriquecidos.csv')
    current_directory = os.path.dirname(os.path.abspath(__file__))
    output_empresas_df_path = os.path.join(current_directory, output_file_relative)
    empresas_df.to_csv(output_empresas_df_path, sep=';', index=False)
    
    
    # Salva os CNPJs que deram erro em um arquivo TXT
    if len(cnpjs_rejeitados) > 0:
        output_errors_relative = os.path.join('arquivos_saida', 'cnpjs_rejeitados.csv')
        current_directory = os.path.dirname(os.path.abspath(__file__))
        output_errors_path = os.path.join(current_directory, output_errors_relative)
    
        with open(output_errors_path, mode='w', newline='') as arquivo_csv:
            escritor_csv = csv.writer(arquivo_csv)
        
            for cnpj in cnpjs_rejeitados:
                escritor_csv.writerow([cnpj])
    else:
        pass
    
if __name__ == "__main__":
    main()