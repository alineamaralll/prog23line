from backend.geral.config import *
from caminho import caminho_imagens

 # curl -i -X POST -F files="@pdf1 14pgs.pdf" http://127.0.0.1:5000/upload
@app.route("/save_image", methods=['POST'])
def salvar_imagem():
    try:
        #print("comecando")
        file_val = request.files['files']
        #print("vou salvar em: "+file_val.filename)
        arquivoimg = os.path.join(caminho_imagens, 'bola.png')
        file_val.save(arquivoimg)
        r = jsonify({"resultado":"ok", "detalhes": file_val.filename})
    except Exception as e:
        r = jsonify({"resultado":"erro", "detalhes": str(e)})

    return r