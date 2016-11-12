from app import db

class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), unique=True)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True
    
    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)
        except:
            return str(self.id)

    def __repr__(self):
        return '<User %r>' % (self.nickname)


class Collection(db.Model):
    __tablename__ = "collection"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), unique = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User',backref=db.backref('user', lazy='dynamic'))

    def __repr__(self):
        return '<Collection %r>' % (self.name)

class Question(db.Model):
    __tablename__ = "Questions"

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(), unique=True)
    body = db.Column(db.String())
    collection_id = db.Column(db.Integer, db.ForeignKey('collection.id'))
    collection = db.relationship('Collection', backref = db.backref('collection', lazy='dynamic'))
