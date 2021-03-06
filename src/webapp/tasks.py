import database as db
from database.model import Team
from geotools import simple_distance
from geotools.routing import MapPoint

try:
    from uwsgidecorators import spool
except ImportError as e:
    def spool(fn):
        def nufun(*args, **kwargs):
            raise e
        return nufun


@spool
def get_aqua_distance(args):
    team = db.session.query(Team).filter(Team.id == int(args["team_id"])).first()

    if team is None:
        return

    target = MapPoint.from_team(team)
    #aqua = MapPoint(51.04485, 13.74011) # real aqua
    aqua = MapPoint(51.05299472808838, 13.742453455924988) # hfbk
    team.location.center_distance = simple_distance(target, aqua)
    db.session.commit()