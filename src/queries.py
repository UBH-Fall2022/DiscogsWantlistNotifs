from models import Release

def get_wantlist_txn(session):
    query = session.query(Release)
    return query.all()

def add_wantlist_txn(session, id, title, artists, formats, num_for_sale, lowest_price):
    release = Release(
        id = id,
        title = title,
        artists = artists,
        formats = formats,
        num_for_sale = num_for_sale,
        lowest_price = lowest_price
    )
    print(release.id)
    print(release.title)
    print(release.artists)
    print(release.formats)
    print(release.num_for_sale)
    print(release.lowest_price)
    session.add(release)