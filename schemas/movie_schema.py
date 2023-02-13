from main import ma

# create Movie Schema with Marshmallow, provides the serialization needed for converting data to JSON
class MovieSchema(ma.Schema):
    class Meta:
        fields = ("id", "title", "genre", "length", "year")

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)
