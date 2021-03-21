async def clock():
    headers = {
        'authorization': token,
        'content-type': 'application/json',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36 OPR/53.0.2907.43'
    }

    custom_s = {
        'status': random.choice(statuss),
        "custom_status": {
            "text": f'{strftime("%H:%M:%S", localtime())}',
            "emoji_name": chr(128335+int(datetime.now().strftime('%I')))
        }
    }

    requests.patch("https://discord.com/api/v8/users/@me/settings",headers=headers, json=custom_s)