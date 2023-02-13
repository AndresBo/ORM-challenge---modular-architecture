from main import ma

# create Actor Schema with Marshmallow, provides the serialization needed for converting data to JSON
class ActorSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "gender", "country", "dob")

actor_schema = ActorSchema()
actors_schema = ActorSchema(many=True)
