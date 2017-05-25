import math
import re
from random import random

from coroweb import get, post, Auth
from models import Marker


@Auth(False)
@get('/')
async def index():
    return 'DDDDDDDDD:'


EARTH_RADIUS = 6371  # 地球平均半径，6371km


@Auth(False)
@get("/markers")
async def get_markers(request, *, lat, lng):
    lat = float(lat)
    lng = float(lng)
    dis = 2  # 2千米距离
    dlng = 2 * math.asin(math.sin(dis / (2 * EARTH_RADIUS)) / math.cos(lat * math.pi / 180))
    dlng = dlng * 180 / math.pi
    dlat = dis / EARTH_RADIUS
    dlat = dlat * 180 / math.pi
    minlat = lat - dlat
    maxlat = lat + dlat
    minlng = lng - dlng
    maxlng = lng + dlng
    ms = await Marker.findAll(where='lng>=? and lng<=? and lat>=? and lat<=?',
                              args=(minlng, maxlng, minlat, maxlat))
    return {
        'markers': ms
    }


@Auth(False)
@post("/markers/add")
async def add_markers(request, *, lat, lng, show_name, phone, intro):
    lat = float(lat)
    lng = float(lng)

    dis = 2  # 2千米距离
    dlng = 2 * math.asin(math.sin(dis / (2 * EARTH_RADIUS)) / math.cos(lat * math.pi / 180))
    dlng = dlng * 180 / math.pi
    dlat = dis / EARTH_RADIUS
    dlat = dlat * 180 / math.pi
    minlat = lat - dlat
    maxlat = lat + dlat
    minlng = lng - dlng
    maxlng = lng + dlng
    ms = await Marker.findAll(where='lng>=? and lng<=? and lat>=? and lat<=?',
                              args=(minlng, maxlng, minlat, maxlat))

    # index = 0
    # if len(ms) == 0:
    #     index = 0
    # else:
    #     index = (ms[len(ms) - 1]['logo_index'] + 1) % 4
    m = Marker(lat=lat, lng=lng, show_name=show_name, phone=phone, intro=intro)
    await m.save()
    return {
        'status': 'ok',
    }


def url_for(request, endpoint, **values):
    item = globals().get(endpoint)
    __regex = re.compile(r'\{\w+\}')
    if item is not None and hasattr(item, '__call__'):
        path = item.__route__
        path = path.split('/')
        i = 0
        for x in path:
            if __regex.match(x):
                for k, v in values.items():
                    if x[1:-1] == k:
                        path[i] = v
            i += 1
        return request.scheme + '://' + request.host + '/'.join(path)
    return None


def hav(theta):
    s = math.sin(theta / 2)
    return s * s


def get_distance_hav(lat0, lng0, lat1, lng1):
    "用haversine公式计算球面两点间的距离。"
    # 经纬度转换成弧度
    lat0 = math.radians(lat0)
    lat1 = math.radians(lat1)
    lng0 = math.radians(lng0)
    lng1 = math.radians(lng1)

    dlng = math.fabs(lng0 - lng1)
    dlat = math.fabs(lat0 - lat1)
    h = hav(dlat) + math.cos(lat0) * math.cos(lat1) * hav(dlng)
    distance = 2 * EARTH_RADIUS * math.asin(math.sqrt(h))

    return distance

# async def cookie2user(cookie_str):
#     if not cookie_str:
#         return None
#     try:
#         L = cookie_str.split('-')
#         if len(L) != 3:
#             return None
#         uid, expires, sha1 = L
#         if int(expires) < time.time():
#             return None
#         user = await ManageUser.findByPk(uid)
#         if user is None:
#             return None
#         s = '%s-%s-%s-%s' % (uid, user.password, expires, _COOKIE_KEY)
#         if sha1 != hashlib.sha1(s.encode('utf-8')).hexdigest():
#             logging.info('invalid sha1')
#             return None
#         user.password = '******'
#         return user
#     except Exception as e:
#         logging.exception(e)
#         return None
