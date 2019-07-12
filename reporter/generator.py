def read(json_path, md_path):
    
    with open (json_path, 'r') as in_file:
        reloaded = json.load(in_file)

    with open (md_path, "w", encoding='utf-8') as out_file:
        out_file.write(header.create_header(reloaded))

    print("wrote")
    
   
    

class Generator:
    
    def __init__(self, json_path, xls_path, md_path):

        self.json_path = json_path
        self.xls_path = xls_path
        self.md_path = md_path
    
    def creat_graph(self):
    
    
        series = pd.read_excel(
        "reporter/data/series-1800-2015_simplified.xlsx"
         ). set_index("année").transpose().dropna(how="all", axis=1)
        series.index = series.index.astype(int)
        series["dib_norm"] = series['dette_immo_menages'] / series["nb_ménages"]
        series.plot("dib_norm", 'prix_logement_Fr')
        
        plt.savefig("graph.png")

    
    def createmarkdown(self):
        with open(self.json_path, 'r') as js_file:
            authors = json.load(js_file)
        text = header.create_header(authors) + "\n\n![a graph](graph.png)\n"
        with open(self.md_path, "w") as out:
            out.write(text)
        