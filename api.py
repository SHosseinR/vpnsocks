import requests

cookies = {
    '_biz_uid': '00f684b3014c45a2ba7462e742f5188d',
    'ajs_anonymous_id': '31e66fe3-e48e-4d17-92b3-92af57c5076c',
    '_biz_flagsA': '%7B%22Version%22%3A1%2C%22ViewThrough%22%3A%221%22%2C%22XDomain%22%3A%221%22%7D',
    'ajs_user_id': '284c4dbf-25ba-4bde-a082-d4fec241c581',
    '_ga': 'GA1.2.895004180.1686572926',
    '_biz_sid': '48a73a',
    'id': 'MTY5Nzg5MTY4MnxwSjNxbW1LUDlhNGlXUWpjLVdLLVo2OHRCRm1fUm9xVVJtUV9XOUtFa0hMakNoVWFIcmZ5S0FaZllfZXFLZ1Q0eTk4UG5ycmtoMGhfQVJodVNCaTctX0xRX2ZIZ3g2M1JudVhna3VsNzdlRURoZmxoMHhFNnZrWVFGelpIRTFteWJrMzVkUlZzT3FsMXNhVzR0d3F5a0QxZ0tkbHR5VUd2cE5RSklPbmxhZjNHWU9QUjV6a01ISHByREtkRFVUZUdqc1BIbEU5LW1VTEdMRmFMZkM2ZmFzOVR2TUxlLXNTVG96dUw1SGhRUGdMRTFCY2Q1bWFyN2FpN0c5R25pbTVpSURXSnZmZE1QSTZXQlhfQnyMxKcg0vwg3f28zoIcCoZtiHqelxOEiHwLxIWdgtKDxA==',
    '_biz_nA': '143',
    '_biz_pendingA': '%5B%22ipv%3F_biz_r%3Dhttps%253A%252F%252Flabs.play-with-docker.com%252F%26_biz_h%3D802059049%26_biz_u%3D00f684b3014c45a2ba7462e742f5188d%26_biz_s%3D48a73a%26_biz_l%3Dhttps%253A%252F%252Flabs.play-with-docker.com%252Fp%252Fckpsap6fml8g00dfhflg%26_biz_t%3D1697891686301%26_biz_i%3DDocker%2520Playground%26_biz_n%3D142%26rnd%3D392567%22%5D',
    '_gid': 'GA1.2.159323849.1697891687',
    '_gat': '1',
    '_ga_5219ZE0FPY': 'GS1.2.1697891687.30.0.1697891687.0.0.0',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://labs.play-with-docker.com',
    'Connection': 'keep-alive',
    'Referer': 'https://labs.play-with-docker.com/',
    # 'Cookie': '_biz_uid=af9ec2ddce4f4dc7a89a304ba5e6199d; _biz_sid=68dca0; _biz_nA=5; _biz_pendingA=%5B%5D; _biz_flagsA=%7B%22Version%22%3A1%2C%22ViewThrough%22%3A%221%22%2C%22XDomain%22%3A%221%22%7D; ajs_anonymous_id=f8273b3f-3b5a-4f41-9589-fb2b627b4962; id=MTY4NzQ1MzE5Nnx0LUwxZlZjc0lBMmxDZnY1d1h2MldfZVNZaldtQ01lN1hCU09ZcGFRM2JGR2RsT21zU2RsMmhhQm5BQl9lV3NrbmU3bXFkaXI1UnJUVXFpbE1SVVhnczM2ZklYRmVaVG5NQXBvekRyYU1lcE9OSGRTZy1GSUhqZHpudXZPZjFQX0tUZ3FSNS1EOGJrbUotUmttQW1BS2FoWE9tNm10bnNzWnBJdFNINWd2dXFyV0VCV2Niei00amlUcWo1SXFMRE96dS0zUXc0NjBLVEJKWFBGcmRPaFE2MXJ3bU5GNWpoeTdTRkN0QjhvR25CVlp4aWEwa09SVUF4ZDNyNFVVX0p4UXYyT3NaUTR0aXBzWUlGN3wAQeAOL7Y2GBbB4FRaIe_ViJKQNtu3KRsYTqkJZT9u2g==; ajs_user_id=284c4dbf-25ba-4bde-a082-d4fec241c581; _ga=GA1.2.1199048311.1687453341; _gid=GA1.2.1322198996.1687453341; _ga_5219ZE0FPY=GS1.2.1687453341.1.0.1687453341.0.0.0',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
}

data = {
    'stack': '',
    'stack_name': '',
    'image_name': '',
}

response = requests.post('https://labs.play-with-docker.com/', cookies=cookies, headers=headers, data=data, allow_redirects=False)

# print(1, response.status_code, response.headers)

Location = response.headers["Location"]
Location_last = Location.split("/")[2]

headers = {
    'authority': 'labs.play-with-docker.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,fa-IR;q=0.8,fa;q=0.7',
    'cache-control': 'no-cache',
    # 'cookie': '_biz_uid=b93e17804abb465a8006b23519ef8f82; _biz_flagsA=%7B%22Version%22%3A1%2C%22ViewThrough%22%3A%221%22%2C%22XDomain%22%3A%221%22%7D; ajs_anonymous_id=eb1967d1-5f69-46c5-8a5c-f9b7bb94c060; ajs_user_id=284c4dbf-25ba-4bde-a082-d4fec241c581; _ga=GA1.2.762165734.1686589187; _gid=GA1.2.1249801449.1687369911; id=MTY4NzQ1MDE5NHx2amJaNl9YZlZhOVB5bXE0YUZWWXZTVzBZc1RhR0tpc1RyczlrR0p3d2xydmsyZ2dDZG05OFFBOGM3amtVaW5nMTZodU56SGx3MVNvQ2NyNmtua0pRNTRnaDRtZU94Si1zbGpiRDRLUXJWR21VN3hNa0hVb1ZBTGF4VGxiYkJBempXd2NZaWs0SGdFVnVfMlJTSEV3eHVMa3lTeHdRNzd0UllnVGlHMDFINUg0LWJ6WS1RXzEzT3g5WHd1WjJVcExoZ3R2QXNhNHA2QmxXeVJORVl1ZEpBYTlPcXlwUkE1ZTlGdnRqYTZsV2NjbVZoM3RlaHk0eDFIcDhhTWNzc1Qzc2NNbjBUOGVHd205QmxDTnz6TMS99-LyoHgeh6f8SuZgJYdkUK8vSH0lqxnSYBssaQ==; _biz_sid=4d82f2; _gat=1; _biz_nA=53; _biz_pendingA=%5B%22m%2Fipv%3F_biz_r%3Dhttps%253A%252F%252Flabs.play-with-docker.com%252F%26_biz_h%3D805002629%26_biz_u%3Db93e17804abb465a8006b23519ef8f82%26_biz_s%3D4d82f2%26_biz_l%3Dhttps%253A%252F%252Flabs.play-with-docker.com%252Fp%252Fcia8qecsnmng00ajejg0%26_biz_t%3D1687457084184%26_biz_i%3DDocker%2520Playground%26_biz_n%3D52%26rnd%3D677188%22%5D; _ga_5219ZE0FPY=GS1.2.1687457085.7.0.1687457085.0.0.0',
    'pragma': 'no-cache',
    'referer': f'https://labs.play-with-docker.com{Location}',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36',
}


response = requests.get('https://labs.play-with-docker.com/my/playground', cookies=cookies, headers=headers)

# print(2, response.status_code, response.json())





import requests


headers = {
    'authority': 'labs.play-with-docker.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,fa-IR;q=0.8,fa;q=0.7',
    'cache-control': 'no-cache',
    # 'cookie': '_biz_uid=b93e17804abb465a8006b23519ef8f82; _biz_flagsA=%7B%22Version%22%3A1%2C%22ViewThrough%22%3A%221%22%2C%22XDomain%22%3A%221%22%7D; ajs_anonymous_id=eb1967d1-5f69-46c5-8a5c-f9b7bb94c060; ajs_user_id=284c4dbf-25ba-4bde-a082-d4fec241c581; _ga=GA1.2.762165734.1686589187; _gid=GA1.2.1249801449.1687369911; id=MTY4NzQ1MDE5NHx2amJaNl9YZlZhOVB5bXE0YUZWWXZTVzBZc1RhR0tpc1RyczlrR0p3d2xydmsyZ2dDZG05OFFBOGM3amtVaW5nMTZodU56SGx3MVNvQ2NyNmtua0pRNTRnaDRtZU94Si1zbGpiRDRLUXJWR21VN3hNa0hVb1ZBTGF4VGxiYkJBempXd2NZaWs0SGdFVnVfMlJTSEV3eHVMa3lTeHdRNzd0UllnVGlHMDFINUg0LWJ6WS1RXzEzT3g5WHd1WjJVcExoZ3R2QXNhNHA2QmxXeVJORVl1ZEpBYTlPcXlwUkE1ZTlGdnRqYTZsV2NjbVZoM3RlaHk0eDFIcDhhTWNzc1Qzc2NNbjBUOGVHd205QmxDTnz6TMS99-LyoHgeh6f8SuZgJYdkUK8vSH0lqxnSYBssaQ==; _biz_sid=4d82f2; _gat=1; _biz_nA=53; _biz_pendingA=%5B%22m%2Fipv%3F_biz_r%3Dhttps%253A%252F%252Flabs.play-with-docker.com%252F%26_biz_h%3D805002629%26_biz_u%3Db93e17804abb465a8006b23519ef8f82%26_biz_s%3D4d82f2%26_biz_l%3Dhttps%253A%252F%252Flabs.play-with-docker.com%252Fp%252Fcia8qecsnmng00ajejg0%26_biz_t%3D1687457084184%26_biz_i%3DDocker%2520Playground%26_biz_n%3D52%26rnd%3D677188%22%5D; _ga_5219ZE0FPY=GS1.2.1687457085.7.0.1687457085.0.0.0',
    'pragma': 'no-cache',
    'referer': f'https://labs.play-with-docker.com{Location}',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36',
}

url = f'https://labs.play-with-docker.com/sessions/{Location_last}'
# print(url)
response = requests.get(f'https://labs.play-with-docker.com/sessions/{Location_last}', cookies=cookies, headers=headers)

# print(3, response.status_code, response.text)

headers = {
    'authority': 'labs.play-with-docker.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,fa-IR;q=0.8,fa;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': '_biz_uid=b93e17804abb465a8006b23519ef8f82; _biz_flagsA=%7B%22Version%22%3A1%2C%22ViewThrough%22%3A%221%22%2C%22XDomain%22%3A%221%22%7D; ajs_anonymous_id=eb1967d1-5f69-46c5-8a5c-f9b7bb94c060; ajs_user_id=284c4dbf-25ba-4bde-a082-d4fec241c581; _ga=GA1.2.762165734.1686589187; _gid=GA1.2.1249801449.1687369911; id=MTY4NzQ1MDE5NHx2amJaNl9YZlZhOVB5bXE0YUZWWXZTVzBZc1RhR0tpc1RyczlrR0p3d2xydmsyZ2dDZG05OFFBOGM3amtVaW5nMTZodU56SGx3MVNvQ2NyNmtua0pRNTRnaDRtZU94Si1zbGpiRDRLUXJWR21VN3hNa0hVb1ZBTGF4VGxiYkJBempXd2NZaWs0SGdFVnVfMlJTSEV3eHVMa3lTeHdRNzd0UllnVGlHMDFINUg0LWJ6WS1RXzEzT3g5WHd1WjJVcExoZ3R2QXNhNHA2QmxXeVJORVl1ZEpBYTlPcXlwUkE1ZTlGdnRqYTZsV2NjbVZoM3RlaHk0eDFIcDhhTWNzc1Qzc2NNbjBUOGVHd205QmxDTnz6TMS99-LyoHgeh6f8SuZgJYdkUK8vSH0lqxnSYBssaQ==; _biz_sid=4d82f2; _biz_nA=53; _ga_5219ZE0FPY=GS1.2.1687457085.7.0.1687457085.0.0.0; _biz_pendingA=%5B%5D',
    'origin': 'https://labs.play-with-docker.com',
    'pragma': 'no-cache',
    'referer': f'https://labs.play-with-docker.com{Location}',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36',
}

json_data = {
    'ImageName': 'franela/dind',
    'type': 'linux',
}

response = requests.post(
    f'https://labs.play-with-docker.com/sessions/{Location_last}/instances',
    cookies=cookies,
    headers=headers,
    json=json_data,
)


# print(response.status_code, response.json())

json_response = response.json()
proxy_host = json_response["proxy_host"]

ssh_host = f'{proxy_host}@direct.labs.play-with-docker.com'

# print("ssh_host: ", ssh_host)

# print(ssh_host)

import sys
sys.stdout.write(ssh_host)
