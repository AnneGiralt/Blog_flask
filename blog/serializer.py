from marshmallow_sqlalchemy import ModelSchema
from app import Post


class PostSchema(ModelSchema):
    class Meta:
        model = Post
