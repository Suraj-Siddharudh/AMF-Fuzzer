import pyamf
from pyamf import remoting
from pyamf.flex import messaging
import uuid
import requests
from pyamf.remoting.client import RemotingService
import json


# Login Request
payload = {'WE_USERNAME': <username>,
           'WE_PASSWORD': <password>,
           'WE_Version': "1.1.0.0",
           'AUTHTYPE': "PASSWORD"}

resp = requests.post(<url>,
                     data=payload,
                     verify=False
                     )
# print(resp.content)
print("\n------------------------------\n")
# print(resp.headers['Set-Cookie'])
print("\n------------------------------\n")
login_header = resp.headers['Set-Cookie'].split(',')
for data in login_header:
    if "SMSESSION" in data:
        data = data.split(";")
        data = data[0].split("=")
        print(data)

cookies = {'SMSESSION': data[1],
           'TS0115c575': '0159fffb6670d4f050f15ccf6f4008111b5db91efc0c16e81535cf32dae600d36a0068b88c4da597c7379aff788db512164bf1e1c3871b1c72b1858c536ff6a96cf04c0d416d867547dd7641ea1f216bf4a0b42607',
           'TS0157d5db':'0159fffb66d37a90c0a710441436619d4ccc171057c074bbfdfc9f63b4faae68196fb4227f918566d0b72b45795afd2bc057982220'}

msg = messaging.RemotingMessage(operation='getUploadFiles',
                                clientId='6525D474-C40B-310E-5166-1BBAD11DB51D',
                                destination='scheduleUploadDocCommand',
                                messageId=str(uuid.uuid4()).upper(),
                                body=['IRMEHT2'],
                                headers={'DSId': '62A318D7-A719-932E-AAB7-19ED3B5CFA23',
                                        'DSEndpoint': 'my-amf', 'DSRequestTimeout': '150'},
                                timeToLive= 0,
                                timestamp=0)


#         # msg_2 = messaging.RemotingMessage(operation='getReportDetails',
#         #                           clientId='6525D474-C40B-310E-5166-1BBAD11DB51D',
#         #                           destination='scheduleUploadDocCommand',
#         #                           messageId=str(uuid.uuid4()).upper(),
#         #                           body=['IRMEHT2'],
#         #                           headers={'DSId': '62A318D7-A719-932E-AAB7-19ED3B5CFA23',
#         #                                    'DSEndpoint': 'my-amf', 'DSRequestTimeout': '150'},
#         #                           timeToLive=0,
#         #                           timestamp=0)
req = remoting.Request(target=None, body=[msg])#, msg_2])
ev = remoting.Envelope(pyamf.AMF3)
ev['/0'] = req
# print("\n\n" + str(req))
# Encode request
bin_msg = remoting.encode(ev)

        # print("\n<-------------Encoded Request------------------>\n")
        # print(bin_msg.getvalue())

#         # Fuzzing Logic
#         # Send request; You can use other channels like RTMP
resp = requests.post(<url>,
                    data=bin_msg.getvalue(),
                    headers={'Content-type': 'application/x-amf'},
                    cookies=cookies,
                    verify=False
                    )
# #         count += 1
# resp_msg = remoting.decode(resp.content)
#         response[entries.strip()] = str(resp_msg.bodies[0][1])
# print("No of Requests Sent: ", format(count))
# print("File to be saved: ", format(r"C:\Thick Client\Responses\sqli_timestamp_getuploadfiles.txt"))
# # print(response)
# with open(r"C:\Thick Client\Responses\sqli_timestamp_getuploadfiles.txt", 'w') as fuzz_response:
#     # json.dump(response, fuzz_response)
#     fuzz_response.write(json.dumps(response))