from flask import Blueprint, jsonify, request, abort
from main import db
from models.actor import Actor
from models.user import User
from schemas.actor_schema import actor_schema, actors_schema
from datetime import date
from flask_jwt_extended import jwt_required, get_jwt_identity

# create the Blueprint controller
# app knows theres a Blueprint called 'actors' and points 
#                  name,  ,points to file name with __name__,  ,  parent url
actors = Blueprint('actors', __name__, url_prefix="/actors")

#           child URL
@actors.route("/", methods = ["GET"])
def get_cards():
    # get all the actors from the bd table
    actors_list = Actor.query.all()
    # converts the actors data from db into a JSON format and store in result
    result = actors_schema.dump(actors_list)
    # return the data in JSON format
    return jsonify(result)
    

@actors.route("/", methods=["POST"])
# decorator to make sure the jwt is included in the request
@jwt_required()
def actor_create():
    actor_fields = actor_schema.load(request.json)

    new_actor = Actor()
    new_actor.name = actor_fields["name"]
    new_actor.gender = actor_fields["gender"]
    new_actor.country = actor_fields["country"]
    new_actor.dob = actor_fields["dob"]

    db.session.add(new_actor)
    db.session.commit()

    return jsonify(actor_schema.dump(new_actor))


@actors.route("/<int:id>/", methods=["DELETE"])
@jwt_required()
# includes the id parameter
def actor_delete(id):
    # get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
    # find it in the db
    user = User.query.get(user_id)
    # make sure it is in the database
    if not user:
        return abort(401, description="Invalid user")

    # find the actor
    actor = Actor.query.filter_by(id=id).first()
    # return an error if the card does not exists
    if not actor:
        return abort(400, description="Actor does not exists")
    # Delete the actor from the db and commit
    db.session.delete(actor)
    db.session.commit()
    # return the card in the response
    return jsonify(actor_schema.dump(actor))
    
