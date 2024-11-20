import os
import re
import argparse

def split_markdown_by_headings(input_file, output_dir):
    # Crea la cartella di output se non esiste
    os.makedirs(output_dir, exist_ok=True)

    # Leggi il contenuto del file Markdown
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Variabili per tracciare i file separati
    current_heading = None
    current_content = []

    # Funzione per salvare il contenuto in un nuovo file
    def save_current_file(heading, content):
        if heading and content:
            # Pulisce il titolo per usarlo come nome file
            filename = re.sub(r'[^\w\-_]', '_', heading.strip()) + ".md"
            filepath = os.path.join(output_dir, filename)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.writelines(content)

    # Processa il file riga per riga
    for line in lines:
        # Controlla se la riga è un heading di livello 1
        if line.startswith("# "):
            # Salva il file precedente
            save_current_file(current_heading, current_content)

            # Avvia un nuovo file
            current_heading = line.strip("# ").strip()
            current_content = [line]
        else:
            # Aggiungi la riga al contenuto corrente
            current_content.append(line)

    # Salva l'ultimo file
    save_current_file(current_heading, current_content)

    print(f"Markdown separato con successo in: {output_dir}")

def main():
    # Configura l'argparse per leggere i parametri
    parser = argparse.ArgumentParser(description="Dividi un file Markdown in più file usando i titoli di livello 1.")
    parser.add_argument('input_file', type=str, help="Percorso del file Markdown sorgente.")
    parser.add_argument('output_dir', type=str, help="Cartella di destinazione per i file separati.")
    
    args = parser.parse_args()

    # Esegui la funzione principale con i parametri forniti
    split_markdown_by_headings(args.input_file, args.output_dir)

if __name__ == "__main__":
    main()
