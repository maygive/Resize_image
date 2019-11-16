from PIL import Image
import glob
list_img= glob.glob("D:\\India\\image_test\\mosquito2\\ss\\*.jpg")
##print(list_img)
print(len(list_img))
for i in range (len(list_img)):
    file_img=list_img[i]
    ##    print(str(file_img).split('\\')[-1])
    file_name=str(file_img).split('\\')[-1]
    print(file_img)
    file_img= file_img.replace('\\','\\\\')
    print(file_img)
    img = Image.open(file_img)
    new_img = img.resize((256,256))
    new_img.save(file_name, "JPEG", optimize=True)
















