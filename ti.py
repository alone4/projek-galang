import os,base64
count = -1

# function open_im digunakan untuk membuka file yang berasal dari open_im_dir
def open_im(x):
    file_ = open(x, "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    return data_url


#function open_im_dir untuk mengambil semua file dari spesifik folder
def open_im_dir(x):
    list = os.listdir(x)
    return list
#memanggil semua file yang ada di brand dan telah di buka oleh open_im dan menjadikannya sebuah list
def brands():
    p=[]
    for x in open_im_dir("img/brands"):
            path = f'img/brands/{x}'
            p.append(path)
    return p
#memanggil semua file yang ada di product dan telah di buka oleh open_im dan menjadikannya sebuah list
def products(y):
    p=[]
    for x in open_im_dir(f"img/products/{y}"):
            path = f'img/products/{y}/{x}'
            p.append(path)
    return p

#bf1 di gunakan untuk memanggil file dari brands
bf1 = [x for x in brands()]
br = []
bran = {}
# pada for di bawah ini list dari bf1 akan di buat menjadi sebuah text berdasarkan nama brand tersebut dan di jadikan list tersendiri
for x in bf1:
    x = x[11:-4]
    br.append(x)

# for di bawah ini memasukkan semua file foto dari function product dan memasukkan nama brand dari br yang di jadikan satu dalam dictionary bran
for x in br:
    for y in bf1:
        if x in y:
            bran[x] = y
            po = {"text": x , "product" :{"image": [x for x in products(x)]}}
            bran[x] = po
            
                
print(bran)


