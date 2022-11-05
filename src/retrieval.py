import discogs_client


def main():
    d = discogs_client.Client('DiscogsWishlistNotifications/0.1', user_token="HlrlaVdlbKnDSjiQlYOeeyyllTXeLnzKKVrWdwZY")
    user_info = d.user("maeve399")
    wantlist = user_info.wantlist
    for item in wantlist:
        print(item.id)


if __name__ == "__main__":
    main()
