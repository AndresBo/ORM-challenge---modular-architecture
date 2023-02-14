from main import ma
from models.user import User
from marshmallow.validate import Length


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
    password = ma.String(validate=Length(min=8))

user_schema = UserSchema()
users_schema = UserSchema(many=True)
