import json

from steam.client import SteamClient


def main():
    """Generate app info json files"""
    client = SteamClient()
    client.anonymous_login()

    app_ids = [730, 232250]
    infos = client.get_product_info(app_ids)['apps']

    for app_id in app_ids:
        if 'depots' not in infos[app_id]:
            continue

        with open(f'depots/{app_id}.json', 'w', encoding='utf-8') as fp:
            json.dump(infos[app_id]['depots'], fp, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    main()
