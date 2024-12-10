import requests

cookies = {
    '_biz_uid': 'dd0c124957654a52c0e6263f063f2edb',
    'ajs_anonymous_id': '7f88c857-6dae-4b0f-a7a8-66651b8f9cb6',
    'ajs_user_id': '284c4dbf-25ba-4bde-a082-d4fec241c581',
    '_biz_nA': '87',
    '_ga_5219ZE0FPY': 'GS1.2.1702491049.19.0.1702491049.0.0.0',
    '_biz_pendingA': '%5B%5D',
    '_ga': 'GA1.1.310246074.1694176221',
    '_ga_LMD5MFLF7Q': 'GS1.1.1730454494.33.1.1730455150.0.0.0',
    'id': 'MTczMzg0OTYzNHxFb1pjTi00aWh6TmM0WDFlQWhMR0d3LV9zRW5EY1EtNW44c2lHM3g3UTlINzFEWFl5TGNxZGZfUExWRjFpUHhPUkFJYUxOUEU1OUlUWXg0UTV1bTVibnJkN1QzMm9Ec1MzZlgwX3dQMUZEMjNFZ0ExdnlOeEVDQjRhTWFfeWZ5RVFaNU9tNERSTDA2SHZEY0h6Q1M0UUdrRWR5Zy1kZ3AySFlBcW8xVlQtMUdJZXBYTkpQREtMYUstMDJEemx3X2NHMjVOWDZpRldJUFpuX0Q4eFI4cE1CR3NWcVNjOVhKTnpDX3FBNkYxX0FfajRURk93cnZZbXptdFU5MGM2WWhWeFVLMDF4N0x2VlhvU0V1TXz_jGGM26cJPQTEBfF61rPLl1oOzf4Yx-PA2kUBDatP_Q==',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,fa-IR;q=0.8,fa;q=0.7',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': '_biz_uid=dd0c124957654a52c0e6263f063f2edb; ajs_anonymous_id=7f88c857-6dae-4b0f-a7a8-66651b8f9cb6; ajs_user_id=284c4dbf-25ba-4bde-a082-d4fec241c581; _biz_nA=87; _ga_5219ZE0FPY=GS1.2.1702491049.19.0.1702491049.0.0.0; _biz_pendingA=%5B%5D; _ga=GA1.1.310246074.1694176221; _ga_LMD5MFLF7Q=GS1.1.1730454494.33.1.1730455150.0.0.0; id=MTczMzg0OTYzNHxFb1pjTi00aWh6TmM0WDFlQWhMR0d3LV9zRW5EY1EtNW44c2lHM3g3UTlINzFEWFl5TGNxZGZfUExWRjFpUHhPUkFJYUxOUEU1OUlUWXg0UTV1bTVibnJkN1QzMm9Ec1MzZlgwX3dQMUZEMjNFZ0ExdnlOeEVDQjRhTWFfeWZ5RVFaNU9tNERSTDA2SHZEY0h6Q1M0UUdrRWR5Zy1kZ3AySFlBcW8xVlQtMUdJZXBYTkpQREtMYUstMDJEemx3X2NHMjVOWDZpRldJUFpuX0Q4eFI4cE1CR3NWcVNjOVhKTnpDX3FBNkYxX0FfajRURk93cnZZbXptdFU5MGM2WWhWeFVLMDF4N0x2VlhvU0V1TXz_jGGM26cJPQTEBfF61rPLl1oOzf4Yx-PA2kUBDatP_Q==',
    'origin': 'https://labs.play-with-docker.com',
    'priority': 'u=0, i',
    'referer': 'https://labs.play-with-docker.com/',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
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
