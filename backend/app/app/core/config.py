import os


def getenv_boolean(var_name, default_value=False):
    result = default_value
    env_value = os.getenv(var_name)
    if env_value is not None:
        result = env_value.upper() in ("TRUE", "1")
    return result


API_V1_STR = "/api/v1"

SECRET_KEY = os.getenvb(b"SECRET_KEY")
if not SECRET_KEY:
    SECRET_KEY = os.urandom(32)

ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 8  # 60 minutes * 24 hours * 8 days = 8 days

CONFERENCE_LIST = {"CVPR", "ICCV", "ACCV", "ECCV", "NIPS", "NEURIPS", "SIGGRAPH", "AAAI", "ICML", "IJCAI"}

MYSQL_SERVER = os.getenv("MYSQL_SERVER")
MYSQL_PORT = os.getenv("MYSQL_PORT")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")
SQLALCHEMY_DATABASE_URI = f"mysql+mysqldb://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_SERVER}:{MYSQL_PORT}/{MYSQL_DATABASE}"
# a string of origins separated by commas, e.g: "http://localhost, http://localhost:4200, http://localhost:3000 "
BACKEND_CORS_ORIGINS = os.getenv("BACKEND_CORS_ORIGINS")

FIRST_SUPERUSER = os.getenv("FIRST_SUPERUSER")
FIRST_SUPERUSER_EMAIL = os.getenv("FIRST_SUPERUSER_EMAIL")
FIRST_SUPERUSER_PASSWORD = os.getenv("FIRST_SUPERUSER_PASSWORD")

USERS_OPEN_REGISTRATION = getenv_boolean("USERS_OPEN_REGISTRATION")

SEARCH_CATEGORIES = ["cs.CV", "cs.RO", "cs.AI", "cs.LG"]

CATEGORY_LIST = ["astro-ph",
                 "astro-ph.CO",
                 "astro-ph.EP",
                 "astro-ph.GA",
                 "astro-ph.HE",
                 "astro-ph.IM",
                 "astro-ph.SR",
                 "cond-mat.dis-nn",
                 "cond-mat.mes-hall",
                 "cond-mat.mtrl-sci",
                 "cond-mat.other",
                 "cond-mat.quant-gas",
                 "cond-mat.soft",
                 "cond-mat.stat-mech",
                 "cond-mat.str-el",
                 "cond-mat.supr-con",
                 "cs.AI",
                 "cs.AR",
                 "cs.CC",
                 "cs.CE",
                 "cs.CG",
                 "cs.CL",
                 "cs.CR",
                 "cs.CV",
                 "cs.CY",
                 "cs.DB",
                 "cs.DC",
                 "cs.DL",
                 "cs.DM",
                 "cs.DS",
                 "cs.ET",
                 "cs.FL",
                 "cs.GL",
                 "cs.GR",
                 "cs.GT",
                 "cs.HC",
                 "cs.IR",
                 "cs.IT",
                 "cs.LG",
                 "cs.LO",
                 "cs.MA",
                 "cs.MM",
                 "cs.MS",
                 "cs.NA",
                 "cs.NE",
                 "cs.NI",
                 "cs.OH",
                 "cs.OS",
                 "cs.PF",
                 "cs.PL",
                 "cs.RO",
                 "cs.SC",
                 "cs.SD",
                 "cs.SE",
                 "cs.SI",
                 "cs.SY",
                 "econ.EM",
                 "eess.AS",
                 "eess.IV",
                 "eess.SP",
                 "gr-qc",
                 "hep-ex",
                 "hep-lat",
                 "hep-ph",
                 "hep-th",
                 "math.AC",
                 "math.AG",
                 "math.AP",
                 "math.AT",
                 "math.CA",
                 "math.CO",
                 "math.CT",
                 "math.CV",
                 "math.DG",
                 "math.DS",
                 "math.FA",
                 "math.GM",
                 "math.GN",
                 "math.GR",
                 "math.GT",
                 "math.HO",
                 "math.IT",
                 "math.KT",
                 "math.LO",
                 "math.MG",
                 "math.MP",
                 "math.NA",
                 "math.NT",
                 "math.OA",
                 "math.OC",
                 "math.PR",
                 "math.QA",
                 "math.RA",
                 "math.RT",
                 "math.SG",
                 "math.SP",
                 "math.ST",
                 "math-ph",
                 "nlin.AO",
                 "nlin.CD",
                 "nlin.CG",
                 "nlin.PS",
                 "nlin.SI",
                 "nucl-ex",
                 "nucl-th",
                 "physics.acc-ph",
                 "physics.ao-ph",
                 "physics.app-ph",
                 "physics.atm-clus",
                 "physics.atom-ph",
                 "physics.bio-ph",
                 "physics.chem-ph",
                 "physics.class-ph",
                 "physics.comp-ph",
                 "physics.data-an",
                 "physics.ed-ph",
                 "physics.flu-dyn",
                 "physics.gen-ph",
                 "physics.geo-ph",
                 "physics.hist-ph",
                 "physics.ins-det",
                 "physics.med-ph",
                 "physics.optics",
                 "physics.plasm-phics",
                 "physics.pop-ph",
                 "physics.soc-ph",
                 "physics.space-ph",
                 "q-bio.BM",
                 "q-bio.CB",
                 "q-bio.GN",
                 "q-bio.MN",
                 "q-bio.NC",
                 "q-bio.OT",
                 "q-bio.PE",
                 "q-bio.QM",
                 "q-bio.SC",
                 "q-bio.TO",
                 "q-fin.CP",
                 "q-fin.EC",
                 "q-fin.GN",
                 "q-fin.MF",
                 "q-fin.PM",
                 "q-fin.PR",
                 "q-fin.RM",
                 "q-fin.ST",
                 "q-fin.TR",
                 "quant-ph",
                 "stat.AP",
                 "stat.CO",
                 "stat.ME",
                 "stat.ML",
                 "stat.OT",
                 "stat.TH"
                 ]
