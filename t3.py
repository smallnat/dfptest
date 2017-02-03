from urllib import request, parse, error
import json
import hashlib
import hmac

# 拼数据
pkg = {}
pkg['userAgent'] = 'MOZILL'
pkg['canvasCode'] = '8UW70C5RTE79838SUWAAP948DDD77432ED'
pkg['cookieCode'] = 'ACPZD8COJ46DQCKUQQQQTTT'
pkg['partnerCode'] = 'LIZH'
pkg['scrHeight'] = '768'
pkg['scrWidth'] = '1366'

sort = sorted(pkg.items(), key=lambda x:x[0])
prePkg = parse.urlencode(sort).encode()
sign = hashlib.sha256(prePkg)
pkg['sign'] = sign.hexdigest()


data = {}
packageStr = parse.urlencode(pkg)
data['packageStr'] = packageStr
data['partnerCode'] = 'xinbang'
data['platform'] = '2'
# print(parse.urlencode(data).encode())
signature = hmac.new(b'9cWbNgUqiL91raHPVmrP', parse.urlencode(data).encode(), hashlib.sha1)
data['signature'] = signature.hexdigest()


header = {'Content-Type':'application/json'}
protocol = 'http'
ip = 'dfp3.bsfit.com.cn'
port = '80'
interface = '/api/device-fingerprint'
url = protocol + '://' + ip + ':' + port + interface
req = request.Request(url, json.dumps(data).encode('utf-8'), header)
try:
	response = request.urlopen(req)
	print(response.read())
except error.HTTPError as err:
	print("dadfa")
	print(err.read())
