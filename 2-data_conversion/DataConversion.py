import pdfplumber
import pandas as pd
import os

def extract_tables_from_pdf(pdf_path: str) -> pd.DataFrame | None:
    """
    Convert a PDF file to a CSV file.

    :param pdf_path: str - The path to the PDF file.
    :param csv_path: str - The path where the CSV file will be saved.
    """
    all_tables = []
    count = 0
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            tables = page.extract_table()
            
            if tables:
                count += 1
                print(f"Total tables found: {count}", end="\r")
                df = pd.DataFrame(tables[1:], columns=tables[0])
                all_tables.append(df)

    if all_tables:
        return pd.concat(all_tables, ignore_index=True)
    else:
        print("No tables found in PDF.")
        return None

def main():
    file_name = "Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"

    # Extract tables from the PDF file
    df = extract_tables_from_pdf(f"1-scraping/files/{file_name}")
    if df is None:
        return
    
    # Switch the acronyms in the DataFrame
    acronyms = {
        "OD":  "Seg. Odontológica",
        "AMB": "Seg. Ambulatorial",
        "HCO": "Seg. Hospitalar Com Obstetrícia",
        "HSO": "Seg. Hospitalar Sem Obstetrícia",
        "REF": "Plano Referência",
        "PAC": "Procedimento de Alta Complexidade",
        "DUT": "Diretriz de Utilização"
    }

    for row in df.iterrows():
        if row[1]['OD'] in acronyms:
            df.at[row[0], 'OD'] = acronyms[row[1]['OD']]
        if row[1]['AMB'] in acronyms:
            df.at[row[0], 'AMB'] = acronyms[row[1]['AMB']]

    # Save the DataFrame to a CSV file and a ZIP file
    folder_path = "2-data_conversion/files/"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    csv_path = os.path.join(folder_path, "table.csv")
    df.to_csv(csv_path, index=False)
    print(f"Data saved at: {csv_path}")

    zip_path = os.path.join(folder_path, "table.zip")
    df.to_csv(zip_path, index=False, compression='zip')
    print(f"Data saved at: {zip_path}")

if __name__ == "__main__":
    main()