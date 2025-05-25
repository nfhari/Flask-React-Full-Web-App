from app import db
#Friends Model
class Friend(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    description = db.Column(db.Text, nullable=False)
    role = db.Column(db.String(50), nullable=False)
    img_url = db.Column(db.String(300), nullable=True)

    def to_json(self):
        return {
            "id":self.id,
            "name":self.name,
            "gender":self.gender,
            "description":self.description,
            "role":self.role,
            "imgUrl":self.img_url,
        }