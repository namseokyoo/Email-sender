from qrgenerator import qrgen
from emailsender import send_mail
 
 
number = 123321
addr = "namsoek.yoo@gmail.com"

qrgen(number,f"당신은 {number}번입니다.")



send_mail(addr, "테스트 제목", "test 입니다")