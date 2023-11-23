import requests

cookies = {
    '_biz_uid': 'dd0c124957654a52c0e6263f063f2edb',
    '_biz_flagsA': '%7B%22Version%22%3A1%2C%22ViewThrough%22%3A%221%22%2C%22XDomain%22%3A%221%22%7D',
    'bf_lead': '2g2joil8nkog00',
    '_mkto_trk': 'id:929-FJL-178&token:_mch-play-with-docker.com-1694168407497-86517',
    'ajs_anonymous_id': '7f88c857-6dae-4b0f-a7a8-66651b8f9cb6',
    'ajs_user_id': '284c4dbf-25ba-4bde-a082-d4fec241c581',
    '_ga': 'GA1.2.310246074.1694176221',
    '_gid': 'GA1.2.1928191892.1700679841',
    'id': 'MTcwMDc0NTM3OXxkbDNWN2FFVVM2enlyOWRORnhwdjZZNTh0b0Zjc1lNYVpPcVkxUUhGSUFSRTY1dmZCUkZDZm54NFB5X0JOOVdMQWs4T0xRX3BZSl9QVDFLNGt2X3dWbXM4NGJ6bHl6eDRfTWZOSklsU2o4NW1kajNzMlQyY2MzNXhuUUhnU2NNbWdxcjZJSVdMQWtad2trOWR4c3NmLTlKQ20zUTdiYTV1b0trWkRlLTZfWHpvRXFGNWNKbm5KSFZJb3FvZU1DcmI1WmN1WHZhbEY5MVpiTjhLMjAtX1hEdHIzX1NqdmRnNXRvWVJ6Vm5zSHRKSkl3Qk5WOGFXUlVjRWREZnpHcnVmQk1md2hzZU9TQThZank5cHzTXlK9XoPz4MKA_P18DDn66i-oz1nxIM8mPkYcH96F0Q==',
    '_gat': '1',
    '_ga_5219ZE0FPY': 'GS1.2.1700745392.16.0.1700745392.0.0.0',
    '_biz_nA': '79',
    '_biz_pendingA': '%5B%5D',
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
