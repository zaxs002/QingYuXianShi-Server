import time
import uuid

from orm import Model, StringField, BooleanField, FloatField, IntegerField


def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)


class User(Model):
    __table__ = 'users'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    email = StringField(ddl='varchar(50)')
    passwd = StringField(ddl='varchar(50)')
    admin = BooleanField()
    name = StringField(ddl='varchar(50)')
    image = StringField(ddl='varchar(500)')
    created_at = FloatField(default=time.time)


class Marker(Model):
    __table__ = 'markers'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    # 纬度
    lat = FloatField()
    # 精度
    lng = FloatField()
    show_name = StringField(ddl="varchar(50)")
    item_id = StringField(ddl="varchar(50)")
    phone = StringField(ddl="varchar(50)")
    intro = StringField(ddl="varchar(500)")
    logo_index = IntegerField()
    created_at = FloatField(default=time.time)
