from os import environ
from wantlist import WantList
from models import Release
from dotenv import load_dotenv
from sqlalchemy.dialects.postgresql.base import PGDialect

# override version check
PGDialect._get_server_version_info = lambda *args: (9, 2)

load_dotenv()
conn_string = environ.get("DB_URI")

wantlist = WantList(conn_string)


def newWantlistData(data):

    for release in data:

        print(release)

        wantlist.add_release(
                Release(id=release["id"],
            title = release["title"],
            artists = release["artists"],
            formats = release["formats"],
            num_for_sale = release["num_for_sale"],
            lowest_price = release["lowest_price"])
        )