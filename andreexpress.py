import pyodbc
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def student():
   return render_template('formulario.html')

@app.route('/resultado',methods = ['POST', 'GET'])
def resultado():
    if request.method == 'POST':
      result = request.form
      tipodemercadoria = request.form['Mercadoria']
      quantidade = request.form['Quantidade']
      cor = request.form['Cor']
      preco = request.form['Preco']
      descricao = request.form['Descricao']

      server = 'DESKTOP-83G9QQT\SQLEXPRESS'
      database = 'DADOS_AULA' 
      cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;')
      cursor = cnxn.cursor()
     
      sql = "INSERT into andreexpress values ('" + tipodemercadoria + "','" + quantidade + "','" + cor + "','" + preco + "','" + descricao + "')"
      cursor.execute(sql)
      cursor.commit()
      cursor.close()
      
    
      

      strHtml = '<!DOCTYPE html> '
      strHtml += '<html> '
      strHtml += '<h1>Mercadoria Cadastrada</h1>'
      strHtml += '<a href="http://127.0.0.1:5000/">Pretende adicionar mais mercadorias?</a><br>'
      strHtml += '<a href="http://127.0.0.1:5000/list/">Deseja excluir?</a>'
      strHtml += '</body> '
      strHtml += '</html> '

      return strHtml
      

wsgi_app = app.wsgi_app
@app.route('/list/')
def lista():
       
     
      server = 'DESKTOP-83G9QQT\SQLEXPRESS'
      database = 'DADOS_AULA' 
      cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;')
      cursor = cnxn.cursor()

      cursor.execute("SELECT * FROM andreexpress")
      result_set = cursor.fetchall()

      strHtml = '<!DOCTYPE html> '
      strHtml += '<html> '
      strHtml += '<body> '

      strHtml += '<table border="1"> '
      strHtml += '<tr> '
      strHtml += '<th>tipodemercadoria</th> '
      strHtml += '<th>Quantidade</th> '
      strHtml += '<th>Cor</th> '
      strHtml += '<th>Preço</th> '
      strHtml += '<th>Descriçao</th> '
      strHtml += '<th>Link</th> '
      strHtml += '<th>Vender</th> '
      strHtml += '</tr> '
      

      for row in result_set:
            strHtml += '<tr> '
            strHtml += '<td>'+row.tipodemercadoria+'</td> '
            strHtml += '<td>'+str(row.quantidade)+'</td> '
            strHtml += '<td>'+row.cor+'</td> '
            strHtml += '<td>'+str(row.preco)+'</td> '
            strHtml += '<td>'+row.descricao+'</td> '
            strHtml += '<td><a href="http://127.0.0.1:5000/excluir/'+str(row.id_andreexpress)+'">retirar</a></td> '
            strHtml += '<td><a href="http://127.0.0.1:5000/vender/'+str(row.id_andreexpress)+'">vendas</a></td> '
            strHtml += '</tr> '
      
      
      strHtml += '</table> '

      strHtml += '</body> '
      strHtml += '</html> '
      
      return strHtml

@app.route('/retirar/<idUsr>')
def retirar(idUsr):

   server = 'DESKTOP-83G9QQT\SQLEXPRESS'
   database = 'DADOS_AULA' 
   
   cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;')
   cursor = cnxn.cursor()

   cursor.execute("DELETE from andreexpress where id_andreexpress ='" + idUsr + "'")
   cursor.commit()
   cursor.close()
   
   return idUsr

@app.route('/vendas/<idUsr>')
def vendas(idUsr):
   
   server = 'DESKTOP-83G9QQT\SQLEXPRESS'
   database = 'DADOS_AULA' 
   cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;')
   cursor = cnxn.cursor()
   cursor.execute("UPDATE andreexpress set  quantidade = quantidade -1 where id_andreexpress ='" + idUsr + "'")
   cursor.commit()
   cursor.close()
      
   return idUsr


if __name__ == '__main__':
   app.run(debug = True)
