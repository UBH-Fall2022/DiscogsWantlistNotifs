import discogs_client
import processing

d = discogs_client.Client('DiscogsWishlistNotifications/0.1', user_token="HlrlaVdlbKnDSjiQlYOeeyyllTXeLnzKKVrWdwZY")

def main():   # get_new_wantlist

   user_info = d.user("maeve399")
   new_wantlist = user_info.wantlist

   wantlist_w_release_info = []

   for release_item in new_wantlist:
      release = d.release(release_item.id)
      if release.marketplace_stats.num_for_sale >= 1:
          release_info = get_release_info(release)
          wantlist_w_release_info.append(release_info)

   processing.newWantlistData(wantlist_w_release_info)


def get_release_info(release):

    artists = [artist.name for artist in release.artists]

    formats = [format["name"] for format in release.formats]

    release_info = {"id": release.id, "title": release.title, "artists": artists, "formats": formats, "num_for_sale": release.marketplace_stats.num_for_sale, "lowest_price": release.marketplace_stats.lowest_price.value}

    return release_info


if __name__ == "__main__":
    main()
