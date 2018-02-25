# coding: utf-8

from flask import Flask, request, url_for

from db import noticias


app = Flask("python_api")

base_html = u"""
  <html>
  <head>
      <title>{title}</title>
  </head>
  <body>
     {body}
  </body>
  </html>
"""


@app.route("/noticias/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        dados_do_formulario = request.form.to_dict()
        nova_noticia = noticias.insert(dados_do_formulario)
        return u"""
            <h1>Noticia id %s inserida com sucesso!</h1>
            <a href="%s"> Inserir nova notícia </a>
        """ % (nova_noticia, url_for('cadastro'))
    else:  # GET
        formulario = u"""
           <form method="post" action="/noticias/cadastro">
               <label>Titulo:<br />
                    <input type="text" name="titulo" id="titulo" />
               </label>
               <br />
               <label>Texto:<br />
                    <textarea name="texto" id="texto"></textarea>
               </label>
               <input type="submit" value="Postar" />
           </form>
        """
        return base_html.format(title=u"Inserir nova noticia", body=formulario)


@app.route("/")
def index():

    noticia_template = u"""
        <a href="/noticia/{noticia[id]}">{noticia[titulo]}</a>
    """

    # it's a kind of magic :)
    todas_as_noticias = [
        noticia_template.format(noticia=noticia)
        for noticia in noticias.all()
    ]

    return base_html.format(
        title=u"Todas as notícias",
        body=u"<br />".join(todas_as_noticias)
    )


@app.route("/noticia/<int:noticia_id>")
def noticia(noticia_id):
    noticia = noticias.find_one(id=noticia_id)
    noticia_html = u"""
        <h1>{titulo}</h1>
        <p>{texto}</p>
    """.format(**noticia)
    return base_html.format(title=noticia['titulo'], body=noticia_html)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
