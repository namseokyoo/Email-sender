import qrcode

def qrgen(number,addr):
  img = qrcode.make(addr)
  img.save(f"{number}.png")
