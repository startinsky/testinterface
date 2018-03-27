import requests
class Get_cookies(object):
  def test_have_cookies(self,url,payload):
     r=requests.get(url,params=payload).cookies
     return r

if __name__ == "__main__":
   url="登录链接自己填"
   payload = {'ddh': 'admin', '密码': 'xndmx'}
   h = Get_cookies()
   r1=h.test_have_cookies(url,payload)
