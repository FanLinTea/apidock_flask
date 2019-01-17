from apps.Edit_Doc.Edit_Doc_Blueprint import Edit_Doc
from flask import render_template,request,url_for,Response
import os
import re
import json

@Edit_Doc.route('/select')
def select_doc():

    return render_template('tes.html')

@Edit_Doc.route('/select2')
def select_doc2():

    return render_template('apidoc/index.html')


@Edit_Doc.route('/create_menu')
def create_doc():
    file_name = request.form.get('file_name')
    # windows文件命名规范re
    info = re.match(r'(?!((^(con)$)|^(con)/..*|(^(prn)$)|^(prn)/..*|(^(aux)$)|^(aux)/..*|(^(nul)$)|^(nul)/..*|(^(com)[1-9]$)|^(com)[1-9]/..*|(^(lpt)[1-9]$)|^(lpt)[1-9]/..*)|^/s+|.*/s$)(^[^/////:/*/?/"/</>/|]{1,255}$)', file_name)
    if info:
        try:
            f = open(f'utils/{file_name}')
            message = json.dumps({'message: '})
        except Exception as e:
            print(e)
        finally:
            f.close()
    return render_template('tes.html')

