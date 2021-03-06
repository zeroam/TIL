from app import db
from passlib.hash import pbkdf2_sha256 as sha256


class UserModel(db.Model):
    """
    User Model Class
    """
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def save_to_db(self):
        """
        Save user details in Database
        """
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        """
        Find user by username
        """
        return cls.query.filter_by(username=username).first()

    @classmethod
    def return_all(cls):
        """
        return all the user data in json form available in DB
        """
        def to_json(x):
            return {
                "username": x.username,
                "password": x.password
            }

        return {"users": [to_json(user) for user in UserModel.query.all()]}

    @classmethod
    def delete_all(cls):
        """
        Delete user data
        """
        try:
            num_rows_deleted = db.session.query(cls).delete()
            db.session.commit()
            return {"message": f"{num_rows_deleted} row(s) deleted"}
        except:
            return {"message": "Something went wrong"}

    @staticmethod
    def generate_hash(password):
        """
        generate hash from password by encryption using sha256
        """
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash_):
        """
        Verify hash and password
        """
        return sha256.verify(password, hash_)


class RevokedTokenModel(db.Model):
    """
    Revoded Token Model Class
    """
    __tablename__ = "revoked_tokens"

    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(120))

    def add(self):
        """
        Save Token in DB
        """
        db.session.add(self)
        db.session.commit()

    @classmethod
    def is_jti_blacklisted(cls, jti):
        """
        Checking that token is blacklisted
        """
        query = cls.query.filter_by(jti=jti).first()
        return bool(query)
