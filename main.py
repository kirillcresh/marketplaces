import requests
import json


def get_data():
    # Берем curl listing'а ОБНОВЛЯЕТСЯ РАЗ В ПОЛЧАСА
    cookies = {
        '__lhash_': '872719cecfc53f37ddf3ee4c49fff699',
        'MVID_CASCADE_CMN': 'true',
        'MVID_CHAT_VERSION': '4.16.4',
        'MVID_CITY_ID': 'CityR_49',  # г. Псков
        'MVID_CREDIT_DIGITAL': 'true',
        'MVID_CREDIT_SERVICES': 'true',
        'MVID_CRITICAL_GTM_INIT_DELAY': '3000',
        'MVID_EMPLOYEE_DISCOUNT': 'true',
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GEOLOCATION_NEEDED': 'true',
        'MVID_GTM_ENABLED': '011',
        'MVID_INTERVAL_DELIVERY': 'true',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_KLADR_ID': '6000000100000',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_MINDBOX_DYNAMICALLY': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_REGION_ID': '49',
        'MVID_REGION_SHOP': 'S970',
        'MVID_SERVICES': '111',
        'MVID_SINGLE_CHECKOUT': 'true',
        'MVID_SP': 'true',
        'MVID_TIMEZONE_OFFSET': '3',
        'MVID_TYP_CHAT': 'true',
        'MVID_WEB_SBP': 'true',
        'SENTRY_ERRORS_RATE': '0.1',
        'SENTRY_TRANSACTIONS_RATE': '0.5',
        'MVID_ENVCLOUD': 'prod1',
        '_ym_uid': '1697300978903737743',
        '_ym_d': '1697300978',
        '_gid': 'GA1.2.1305335314.1697300978',
        '_ym_isad': '1',
        '__SourceTracker': 'yandex.ru__organic',
        'admitad_deduplication_cookie': 'yandex.ru__organic',
        'SMSError': '',
        'authError': '',
        'tmr_lvid': '80b8fa8b85dd67f69c73abc87f3d8ea0',
        'tmr_lvidTS': '1697300982105',
        'advcake_track_id': 'e908f845-29b2-e5f3-893a-d46a0f9976a0',
        'advcake_session_id': '86f16fda-0c84-f31a-1963-fb2b1cb54798',
        'uxs_uid': 'e0efa6c0-6aae-11ee-b0f5-77d1768f00f6',
        '_gpVisits': '{"isFirstVisitDomain":true,"idContainer":"100025D5"}',
        'afUserId': '68a4d01d-eafc-4c57-88b0-318e9b996fd9-p',
        'AF_SYNC': '1697300983091',
        'flocktory-uuid': 'af399e69-cd69-452e-b6f2-c50b9d5055ae-2',
        'flacktory': 'no',
        'BIGipServeratg-ps-prod_tcp80': '1795480586.20480.0000',
        'bIPs': '-1991023829',
        'tmr_detect': '1%7C1697309501202',
        '_ga_TY7GLH5RV3': 'GS1.2.1697309397.2.1.1697309501.60.0.0',
        '_gp100025D5': '{"hits":4,"vc":1,"ac":1,"a6":1}',
        '__hash_': 'd135a58c50c288f8e76053759317d630',
        'gssc218': '',
        'gsscgib-w-mvideo': 'VWP0/VGtHSteCh8aBBFQOnJ909lVpujfWQZ7w9qD2ocOX1dzMJh3Yyu0Ge3TvpdftaqCUKGhMzzHBomYIqlZs9uoncHNfiTkViy9p0GX2wqpv/7/WDE4Dmv2VCcy57Qvkelq/FfumtMyg2WWVjRZGKAi229YaEL9osvPOErEHGJVDnyB69nnTu7F+V3L4sbBJ00Hw6zfaPXNx6JT7lzrWH/zXANHhCd+QWqij6TDpAHGMuwvm+0suUSkV9GP7YEpew==',
        'gsscgib-w-mvideo': 'VWP0/VGtHSteCh8aBBFQOnJ909lVpujfWQZ7w9qD2ocOX1dzMJh3Yyu0Ge3TvpdftaqCUKGhMzzHBomYIqlZs9uoncHNfiTkViy9p0GX2wqpv/7/WDE4Dmv2VCcy57Qvkelq/FfumtMyg2WWVjRZGKAi229YaEL9osvPOErEHGJVDnyB69nnTu7F+V3L4sbBJ00Hw6zfaPXNx6JT7lzrWH/zXANHhCd+QWqij6TDpAHGMuwvm+0suUSkV9GP7YEpew==',
        'mindboxDeviceUUID': '08d2e8bc-1e6a-496c-929e-d37caef4ddba',
        'directCrm-session': '%7B%22deviceGuid%22%3A%2208d2e8bc-1e6a-496c-929e-d37caef4ddba%22%7D',
        'fgsscgib-w-mvideo': '718G9547525da1ae4b5feb2796a4b40f24b95193',
        'fgsscgib-w-mvideo': '718G9547525da1ae4b5feb2796a4b40f24b95193',
        'cfidsgib-w-mvideo': 'G/9f6V+nB4tDcloN2TuAfT0Y5DJRMxfJwALukH3cQzHq1K1W7K9Qc/p7QFP/Z4f9r0mXzzys+drWLM2qt5O+kwGcqseJXLL89x/8wE30xOcknS9UTblogaFuvGcI3j+DWjN3yViSpbXTTeiuH3UH0oxnZm3K9Z+GkempaA==',
        '_dc_gtm_UA-1873769-1': '1',
        '_sp_ses.d61c': '*',
        '_sp_id.d61c': '08af505f-f3d8-43d9-8b9f-d9c831dd0faa.1697300978.3.1697311882.1697309498.87cb2f8e-bfce-46e8-a650-c014d00003d9.62e4bbc1-29e6-4886-90f2-150cfc3d2e52.df71ad6b-6d38-4dd8-906b-1bd2f940a634.1697311881908.1',
        '_ga_CFMZTSS5FM': 'GS1.1.1697311878.3.1.1697311881.0.0.0',
        '_ga': 'GA1.1.780554528.1697300978',
        '_ga_BNX5WPP3YK': 'GS1.1.1697311878.3.1.1697311881.57.0.0',
        '_ga_HCF1KSW48B': 'GS1.2.1697311882.3.0.1697311882.60.0.0',
    }

    headers = {
        'authority': 'www.mvideo.ru',
        'accept': 'application/json',
        'accept-language': 'ru,en;q=0.9',
        'baggage': 'sentry-environment=production,sentry-public_key=1e9efdeb57cf4127af3f903ec9db1466,sentry-trace_id=843b98844723455aa5cb11f79dc65229,sentry-sample_rate=0.5,sentry-transaction=%2F**%2F,sentry-sampled=true',
        # 'cookie': '__lhash_=872719cecfc53f37ddf3ee4c49fff699; MVID_CASCADE_CMN=true; MVID_CHAT_VERSION=4.16.4; MVID_CITY_ID=CityR_49; MVID_CREDIT_DIGITAL=true; MVID_CREDIT_SERVICES=true; MVID_CRITICAL_GTM_INIT_DELAY=3000; MVID_EMPLOYEE_DISCOUNT=true; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GTM_ENABLED=011; MVID_INTERVAL_DELIVERY=true; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=6000000100000; MVID_LAYOUT_TYPE=1; MVID_MINDBOX_DYNAMICALLY=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_REGION_ID=49; MVID_REGION_SHOP=S970; MVID_SERVICES=111; MVID_SINGLE_CHECKOUT=true; MVID_SP=true; MVID_TIMEZONE_OFFSET=3; MVID_TYP_CHAT=true; MVID_WEB_SBP=true; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; MVID_ENVCLOUD=prod1; _ym_uid=1697300978903737743; _ym_d=1697300978; _gid=GA1.2.1305335314.1697300978; _ym_isad=1; __SourceTracker=yandex.ru__organic; admitad_deduplication_cookie=yandex.ru__organic; SMSError=; authError=; tmr_lvid=80b8fa8b85dd67f69c73abc87f3d8ea0; tmr_lvidTS=1697300982105; advcake_track_id=e908f845-29b2-e5f3-893a-d46a0f9976a0; advcake_session_id=86f16fda-0c84-f31a-1963-fb2b1cb54798; uxs_uid=e0efa6c0-6aae-11ee-b0f5-77d1768f00f6; _gpVisits={"isFirstVisitDomain":true,"idContainer":"100025D5"}; afUserId=68a4d01d-eafc-4c57-88b0-318e9b996fd9-p; AF_SYNC=1697300983091; flocktory-uuid=af399e69-cd69-452e-b6f2-c50b9d5055ae-2; flacktory=no; BIGipServeratg-ps-prod_tcp80=1795480586.20480.0000; bIPs=-1991023829; tmr_detect=1%7C1697309501202; _ga_TY7GLH5RV3=GS1.2.1697309397.2.1.1697309501.60.0.0; _gp100025D5={"hits":4,"vc":1,"ac":1,"a6":1}; __hash_=d135a58c50c288f8e76053759317d630; gssc218=; gsscgib-w-mvideo=VWP0/VGtHSteCh8aBBFQOnJ909lVpujfWQZ7w9qD2ocOX1dzMJh3Yyu0Ge3TvpdftaqCUKGhMzzHBomYIqlZs9uoncHNfiTkViy9p0GX2wqpv/7/WDE4Dmv2VCcy57Qvkelq/FfumtMyg2WWVjRZGKAi229YaEL9osvPOErEHGJVDnyB69nnTu7F+V3L4sbBJ00Hw6zfaPXNx6JT7lzrWH/zXANHhCd+QWqij6TDpAHGMuwvm+0suUSkV9GP7YEpew==; gsscgib-w-mvideo=VWP0/VGtHSteCh8aBBFQOnJ909lVpujfWQZ7w9qD2ocOX1dzMJh3Yyu0Ge3TvpdftaqCUKGhMzzHBomYIqlZs9uoncHNfiTkViy9p0GX2wqpv/7/WDE4Dmv2VCcy57Qvkelq/FfumtMyg2WWVjRZGKAi229YaEL9osvPOErEHGJVDnyB69nnTu7F+V3L4sbBJ00Hw6zfaPXNx6JT7lzrWH/zXANHhCd+QWqij6TDpAHGMuwvm+0suUSkV9GP7YEpew==; mindboxDeviceUUID=08d2e8bc-1e6a-496c-929e-d37caef4ddba; directCrm-session=%7B%22deviceGuid%22%3A%2208d2e8bc-1e6a-496c-929e-d37caef4ddba%22%7D; fgsscgib-w-mvideo=718G9547525da1ae4b5feb2796a4b40f24b95193; fgsscgib-w-mvideo=718G9547525da1ae4b5feb2796a4b40f24b95193; cfidsgib-w-mvideo=G/9f6V+nB4tDcloN2TuAfT0Y5DJRMxfJwALukH3cQzHq1K1W7K9Qc/p7QFP/Z4f9r0mXzzys+drWLM2qt5O+kwGcqseJXLL89x/8wE30xOcknS9UTblogaFuvGcI3j+DWjN3yViSpbXTTeiuH3UH0oxnZm3K9Z+GkempaA==; _dc_gtm_UA-1873769-1=1; _sp_ses.d61c=*; _sp_id.d61c=08af505f-f3d8-43d9-8b9f-d9c831dd0faa.1697300978.3.1697311882.1697309498.87cb2f8e-bfce-46e8-a650-c014d00003d9.62e4bbc1-29e6-4886-90f2-150cfc3d2e52.df71ad6b-6d38-4dd8-906b-1bd2f940a634.1697311881908.1; _ga_CFMZTSS5FM=GS1.1.1697311878.3.1.1697311881.0.0.0; _ga=GA1.1.780554528.1697300978; _ga_BNX5WPP3YK=GS1.1.1697311878.3.1.1697311881.57.0.0; _ga_HCF1KSW48B=GS1.2.1697311882.3.0.1697311882.60.0.0',
        'referer': 'https://www.mvideo.ru/noutbuki-planshety-komputery-8/planshety-195/f/skidka=da/tolko-v-nalichii=da',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "YaBrowser";v="23"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sentry-trace': '843b98844723455aa5cb11f79dc65229-b655e34813b32a15-1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.967 YaBrowser/23.9.1.967 Yowser/2.5 Safari/537.36',
        'x-set-application-id': 'fa57aac9-c119-44bf-9ecd-306c06db9db7',
    }

    params = {
        'categoryId': '195', # Планшеты
        'offset': '0',
        'limit': '24',
        'filterParams': [
            'WyJza2lka2EiLCIiLCJkYSJd',
            'WyJ0b2xrby12LW5hbGljaGlpIiwiIiwiZGEiXQ==',
        ],
        'doTranslit': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies,
                            headers=headers).json()
    # получаем из списка айди продуктов
    products_ids = response.get('body').get('products')

    with open('1_products_ids.json', 'w', encoding="utf-8") as file:
        json.dump(products_ids, file, indent=4, ensure_ascii=False)
    # получаем инфо о продуктах
    json_data = {
        'productIds': products_ids,
        'mediaTypes': [
            'images',
        ],
        'category': True,
        'status': True,
        'brand': True,
        'propertyTypes': [
            'KEY',
        ],
        'propertiesConfig': {
            'propertiesPortionSize': 5,
        },
        'multioffer': False,
    }

    response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers,
                             json=json_data).json()

    with open('2_items.json', 'w', encoding="utf-8") as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    products_ids_str = ','.join(products_ids)

    params = {
        'productIds': products_ids_str,
        'addBonusRubles': 'true',
        'isPromoApplied': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies,
                            headers=headers).json()

    with open('3_prices', 'w', encoding="utf-8") as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    items_prices = {}
    material_prices = response.get('body').get('materialPrices')

    for item in material_prices:
        item_id = item.get('price').get('productID')
        item_base_price = item.get('price').get('basePrice')
        item_sale_price = item.get('price').get('salePrice')
        item_bonus = item.get('price').get('total')

        items_prices[item_id] = {
            "item_base_price": item_base_price,
            "item_sale_price": item_sale_price,
            "item_bonus": item_bonus
        }

        with open('4_items_prices.json', 'w', encoding="utf-8") as file:
            json.dump(items_prices, file, indent=4, ensure_ascii=False)


def get_result():
    with open('2_items.json') as file:
        products_data = json.load(file)

    with open('4_items_prices.json') as file:
        products_prices = json.load(file)

    for item in products_data:
        product_id = item.get('productID')
        if product_id in products_prices:
            prices = products_prices[product_id]
            item["item_basePrice"] = prices.get('item_basePrice')
            item["item_salePrice"] = prices.get('item_salePrice')
            item["item_bonus"] = prices.get('item_bonus')

    with open('5_result.json', 'w', encoding="utf-8") as file:
        json.dump(products_data, file, indent=4, ensure_ascii=False)


def main():
    get_data()
    get_result()


if __name__ == "__main__":
    main()
