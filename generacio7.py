import os, json, ast
from google import genai
from google.genai import types

MODEL_NAME = "gemini-2.0-flash-exp"
DATASETS_FILE = "datasets.json"
SYSTEM_INSTRUCTION = ("Ets una eina que només genera llistes Python amb dades de prova. "
                      "Sempre has de respondre nomes amb una llista Python vàlida, sense cap text addicional."
                      "No afegeixis explicacions, comentaris ni text abans o després de la llista."
                      "La resposta ha de ser directament interpretable com a codi Python.")

class GeneradorDatasets:
    def __init__(self):
        self.datasets = {}
        self.client = None
        self._gestio_json("carregar")
        self._inicialitzar_api()

    def _inicialitzar_api(self):
        try:
            api_key = os.getenv("GEMINI_API_KEY")
            if not api_key:
                print("ERROR No hi ha GEMINI_API_KEY")
                return
            self.client = genai.Client(api_key=api_key)
        except Exception as e:
            print(f"ERROR al inicialitzar l'API: {e}")

    def _gestio_json(self, mode="carregar"):
        try:
            if mode=="carregar" and os.path.exists(DATASETS_FILE):
                with open(DATASETS_FILE,'r',encoding='utf-8') as f: self.datasets=json.load(f)
            elif mode=="guardar":
                with open(DATASETS_FILE,'w',encoding='utf-8') as f: json.dump(self.datasets,f,ensure_ascii=False,indent=2)
        except Exception as e:
            print(f"ERROR {mode}: {e}")
            if mode=="carregar": self.datasets={}

    def _construir_prompt(self, tipus_dada, num_elements, descripcio):
        tipus_map={1:"enters",2:"decimals",3:"text (strings)"}
        return (f"Genera una llista Python amb {num_elements} elements de tipus {tipus_map.get(tipus_dada,'text')}. "
                f"Descripció de les dades: {descripcio} "
                f"Respon nomes amb la llista Python, sense cap text addicional- "
                f"- La llista ha de tenir exactament {num_elements} elements")

    def _validar_llista(self,resposta):
        try: return ast.literal_eval(resposta.strip())
        except: return None

    def generar_dataset(self):
        print("-"*30+"    Generació d'un nou set"+"-"*30)
        if not self.client: print("ERROR No s'ha pogut connectar amb l'API "); return
        nom=input("Introdueix un nom per al set de dades: ").strip()
        if not nom: print("ERROR El nom no pot estar buit"); return
        if nom in self.datasets:
            if input(f"Ja existeix un set amb el nom '{nom}'. Vols sobreescriure'l? (s/n): ").lower()!='s': print("Operació cancel·lada"); return
        print("Quin tipus de dada vols que sigui?1 - Enters 2 - Decimals 3 - Text")
        try: tipus_dada=int(input("Tipus de dada: ")); 
        except: print("ERROR Has d'introduir un número"); return
        try: num_elements=int(input("Quants elements vols? ")); 
        except: print("ERROR Has d'introduir un número vàlid"); return
        descripcio=input("Quines dades necessites que et generi? > ").strip()
        if not descripcio: print("ERROR La descripció no pot estar buida"); return
        prompt=self._construir_prompt(tipus_dada,num_elements,descripcio)
        print("Generant dades")
        try:
            response=self.client.models.generate_content(model=MODEL_NAME,contents=prompt,
                config=types.GenerateContentConfig(system_instruction=SYSTEM_INSTRUCTION,temperature=1.0))
            llista=self._validar_llista(response.text)
            if not llista: print("ERROR: La IA no ha retornat una llista vàlida"); return
            if len(llista)!=num_elements: print(f"Advertència: S'esperaven {num_elements} elements però s'han rebut {len(llista)}")
            self.datasets[nom]={"dades":llista,"tipus":tipus_dada,"descripcio":descripcio}
            self._gestio_json("guardar") and print(f'Set "{nom}" guardat correctament!') or print(f'ERROR: No s ha pogut guardar el set "{nom}"')
        except Exception as e: print(f"ERROR en generar les dades: {e}Comprova la connexió a Internet i la clau d'API")

    def visualitzar_datasets(self):
        print("-"*30+"  Visualitzar Sets de Dades"+"-"*30)
        if not self.datasets: print("No hi ha cap set de dades disponible"); return
        opcio=input("1 - Visualitzar un set concret 2 - Visualitzar tots els sets Opció: ").strip()
        if opcio=="1":
            print("Sets disponibles:"); [print(f"- {n}") for n in self.datasets.keys()]
            nom=input("Quin vols visualitzar? ").strip()
            if nom not in self.datasets: print(f"ERROR No existeix cap set amb el nom '{nom}'"); return
            self._mostrar(nom)
        elif opcio=="2": [self._mostrar(n) for n in self.datasets.keys()]
        else: print("ERROR: Opció no vàlida")

    def _mostrar(self, nom):
        d=self.datasets[nom]; print(f"Set: {nom} Dades: {d['dades']} Nombre d'elements: {len(d['dades'])}")

    def esborrar_datasets(self):
        print("-"*30+"  Esborrar Sets de Dades"+"-"*30)
        if not self.datasets: print("No hi ha cap set de dades disponible"); return
        opcio=input("1 - Esborrar un set concret 2 - Esborrar tots els sets Opció: ").strip()
        if opcio=="1":
            print("Sets disponibles:"); [print(f"- {n}") for n in self.datasets.keys()]
            nom=input("Quin vols esborrar? ").strip()
            if nom not in self.datasets: print(f"ERROR No existeix cap set amb el nom '{nom}'"); return
            if input(f"Estàs segur que vols esborrar '{nom}'? (s/n): ").lower()=='s': 
                del self.datasets[nom]; self._gestio_json("guardar") and print(f"Set '{nom}' esborrat correctament")
        elif opcio=="2":
            if input("Estàs segur que vols esborrar TOTS els sets? (s/n): ").lower()=='s':
                self.datasets={}; self._gestio_json("guardar") and print("Tots els sets han estat esborrats")
        else: print("ERROR Opció no vàlida")

    def mostrar_menu(self):
        print("-"*30+"  Generador de Sets de Dades"+"-"*30)
        print("1. Generar un nou set de dades 2. Visualitzar un o tots els sets de dades 3. Esborrar un o tots els sets de dades 4. Sortir")

    def executar(self):
        while True:
            self.mostrar_menu()
            opcio=input("Tria una opció: ").strip()
            {"1":self.generar_dataset,"2":self.visualitzar_datasets,"3":self.esborrar_datasets,"4":lambda: exit(print("Tancant el programa. Fins aviat!"))}.get(opcio,lambda: print("ERROR Opció no vàlida"))()
            print()

def main():
    GeneradorDatasets().executar()

if __name__=="__main__":
    main()
