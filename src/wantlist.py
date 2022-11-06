from cockroachdb.sqlalchemy import run_transaction
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from queries import get_wantlist_txn, add_wantlist_txn

class WantList:
    def __init__(self, conn_string):
        self.engine = create_engine(conn_string, convert_unicode=True)
        self.sessionmaker = sessionmaker(bind=self.engine)

    def get_wantlist(self):
        return run_transaction(self.sessionmaker,
                               lambda session: self.prepare_wantlist(session))

    def add_release(self, release):
        return run_transaction(self.sessionmaker,
                               lambda session: add_wantlist_txn(session, release.id, release.title, release.artists, release.formats, release.num_for_sale, release.lowest_price))

    def prepare_wantlist(self, session):

        wantlist = get_wantlist_txn(session)

        result = list(map(lambda wantlist, i: {'id': wantlist.id,
                                            'album': wantlist.album,
                                            'artist': wantlist.artist,
                                            'format': wantlist.format,
                                            'num_on_sale': wantlist.sum_on_sale,
                                            'lowest_price': wantlist.lowest_price
                                            },
                        wantlist,
                        list(range(len(wantlist)))))
        return result