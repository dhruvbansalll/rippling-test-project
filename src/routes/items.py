from flask import Blueprint, request, jsonify
from ..models import Item
from ..db import db

items_bp = Blueprint("items", __name__, url_prefix="/items")

@items_bp.route("", methods=["POST"])
def create_item():
    data = request.get_json() or {}
    name = data.get("name")
    if not name:
        return {"error": "name required"}, 400

    item = Item(name=name)
    db.session.add(item)
    db.session.commit()
    return {"id": item.id, "name": item.name}, 201