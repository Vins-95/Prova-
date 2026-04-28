import os

# Skill: Generazione automatica stato progetto
files = os.listdir('.')
conta_file = len(files)

with open("STATO_PROGETTO.txt", "w") as f:
    f.write(f"REPORT AGENTE VINS\n")
    f.write(f"-------------------\n")
    f.write(f"Nella cartella ci sono {conta_file} file.\n")
    f.write(f"L'agente è configurato e pronto all'azione.")

print("Skill eseguita: creato file STATO_PROGETTO.txt")
