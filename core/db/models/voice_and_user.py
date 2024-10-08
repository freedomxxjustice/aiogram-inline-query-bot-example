from tortoise import fields
from tortoise.models import Model


class AnyTypeOfMessage(Model):
    id = fields.IntField(pk=True)
    file_id = fields.CharField(max_length=256)
    title = fields.CharField(max_length=64, null=False)
    description = fields.CharField(max_length=64, null=True)
    sends = fields.IntField(pk=False)


class User(Model):
    id = fields.BigIntField(pk=True)
    username = fields.CharField(max_length=32, null=True)
