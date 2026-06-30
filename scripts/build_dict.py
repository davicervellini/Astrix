import os
import json
import yaml

def build_dictionary():
    dict_dir = "dictionary"
    output_file = "dictionary.json"
    
    # Estrutura base do dicionário final
    final_dict = {
        "language": "Astrix",
        "version": "0.3",
        "description": "Língua construída otimizada para a era interestelar",
        "categories": {}
    }
    
    # Verifica se a pasta existe
    if not os.path.exists(dict_dir):
        print(f"Diretório '{dict_dir}' não encontrado.")
        return
        
    # Processa cada arquivo YAML na pasta
    for filename in os.listdir(dict_dir):
        if filename.endswith(".yaml") or filename.endswith(".yml"):
            category_name = os.path.splitext(filename)[0]
            file_path = os.path.join(dict_dir, filename)
            
            with open(file_path, 'r', encoding='utf-8') as f:
                try:
                    data = yaml.safe_load(f)
                    final_dict["categories"][category_name] = data
                    print(f"Categoria carregada: {category_name} ({len(data) if data else 0} palavras)")
                except Exception as e:
                    print(f"Erro ao ler {filename}: {e}")
                    
    # Salva o arquivo JSON compilado
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(final_dict, f, ensure_ascii=False, indent=2)
        
    print(f"Dicionário compilado com sucesso em {output_file}!")

if __name__ == "__main__":
    build_dictionary()
