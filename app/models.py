from app import db
from sqlalchemy import Column,Integer,String,ForeignKey,Float
from sqlalchemy.orm import relationship
class Category(db.Model):
    __tablename__= 'category'
    id=Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(50),nullable=False,unique=True)


class Product(db.Model):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    price = Column(Float, default=0)
    image = Column(String(100))
    category_id = Column(Integer,ForeignKey(Category.id), nullable=False)


if __name__=='__main__':
    from app import app
    with app.app_context():
        c1 = Category(name='tai nghe')
        c2= Category(name='moto')
        db.session.add(c1)
        db.session.add(c2)
        db.session.commit()
        # #
        # p1 = Product(name='Xe dap' ,price =1000000,category_id = 2,image ='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRLBnF3K5y9VDks933c3z4f-rT3YtKC4pwyfg&usqp=CAU')
        p2 = Product(name='Xe dua', price=160000, category_id=1,
                     image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1690461425/bqjr27d0xjx4u78ghp3s.jpg')

        p4 = Product(name='Xe buyt', price=3000, category_id=1,
                     image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1690461425/bqjr27d0xjx4u78ghp3s.jpg')
        p5 = Product(name='xe lan', price=15000, category_id=2,
                     image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1690461425/bqjr27d0xjx4u78ghp3s.jpg')
        db.session.add_all([p2,p4,p5])
        db.session.commit()
        # # p1 =
        #  db.create_all()