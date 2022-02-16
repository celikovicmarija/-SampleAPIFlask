from db import db


class StoreModel(db.Model):
    TABLE_NAME = 'stores'
    __tablename__ = 'stores'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    items=db.relationship('ItemModel', lazy='dynamic')
    #da se ne bi odmah krerao objekat za svaki item koji ima odgovorajuci store id
    #cim se StoreModel kreira, kreira se i ta veza
    #whenever we create store model, we go and create an object for each item
    #in the database that matches that store id
    #can be an expensive operation
    #self.item is no longer list of items, it is a query builder
    #that can look into the items table
    #and we can use .all() to retrieve all the matching items in that table
    #every time you call json() methon, you retrieve again all the elements in the database
    #but you create  store for free
    #there is a trade of between the speed of creation of the store
    #and speed of calling the json method

    def __init__(self, name):
        self.name = name

    def json(self):
        return {'name': self.name,'items':[item.json() for item in self.items.all()]}


    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self) #for both update and insert
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()



