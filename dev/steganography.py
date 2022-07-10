from PIL import Image

mask_img = Image.open('C:/Users/imbmi/OneDrive/바탕 화면/랩실/세미나/Steganography/alcholguntak.jpg')  # 숨겨줄 파일
secret_img = Image.open('C:/Users/imbmi/OneDrive/바탕 화면/랩실/세미나/Steganography/secret.bmp')  # 숨겨지는 파일

mask_width, mask_height = mask_img.size  # 숨겨줄 파일의 크기
secret_width, secret_height = secret_img.size  # 숨겨지는 파일의 크기

for y in range(secret_height):
    for x in range(secret_width):
        secret_rgb = secret_img.getpixel((x, y))
        mask_rgb = mask_img.getpixel((x, y))

        sec_r, sec_g, sec_b = secret_rgb  # 숨겨지는 사진의 RGB 추출
        mask_r, mask_g, mask_b = mask_rgb  # 숨겨줄 사진의 RGB 추출

        if sec_r & 1 == 0:  # 숨겨지는 사진의 비트가 0이라면
            mask_r -= mask_r & 2  # 숨겨줄 사진의 r의 LSB의 상위 비트(2)를 0으로 바꾸고(검은색)
        else:                 # 아니면 1(하얀색)
            mask_r = mask_r | 2
        mask_img.putpixel((x, y), (mask_r, mask_g, mask_b))  # 계산된 픽셀을 다시 숨겨줄 사진에 대입

mask_img.save("lsbstegano.png", "png")