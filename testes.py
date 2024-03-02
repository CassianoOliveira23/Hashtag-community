
from hashtagcommunity.models import Usuario, Posts, database
from main import app

'''with app.app_context():
    database.create_all()'''

'''with app.app_context():
    usuario = Usuario(username="João e Santo Cristo", email="joaosc@gmail.com", senha="123456")
    usuario2 = Usuario(username="Eduarda Kalitski", email="duda_kalitski@gmail.com", senha="123456789")

    database.session.add(usuario)
    database.session.add(usuario2)

    database.session.commit()'''
    
'''with app.app_context():
    user_teste = Usuario.query.filter_by(id=2).first()
    print(user_teste)
    print(user_teste.email)'''
    
    
'''with app.app_context():
    meu_post = Posts(id_usuario=1, titulo="Primeiro post", corpo="Indo pra Brazília")
    database.session.add(meu_post)
    database.session.commit()'''
    
'''with app.app_context():
    post = Posts.query.first()
    print(post.titulo)
    print(post.autor.email)'''
    
    
with app.app_context():
    database.drop_all()
    database.create_all()