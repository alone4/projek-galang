import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
from ti import *


#option_menu di bawah bekerja sebagai tab jadi di website ini ada 3 halaman jika salah satu akan bertganti
selected2 = option_menu(None, ["Home", 'Brands', "Products"], 
    icons=['house', 'Brands', "Products"], 
    menu_icon="cast", default_index=0, orientation="horizontal")

# di selected2 = home artinya jika user mengclick pada tabnya akan di arah ke halaman home dan menunjukkan semua codingan yang ada di dalamnya

with st.container():
    if selected2 == "Home":
      #pada open_im(brands()[0]) merupakan hal untuk memanggil sebuah image dari function brands yang di encode agar bisa di panggil pada html
      # bran[br[0]]['text] untuk memanggil nama brand yang disimpan pada dictionary bran
        components.html(f"""
        <!DOCTYPE html>
<html lang="en">
<head>
  <title>Bootstrap Example</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>
</head>
<body>

<!-- Carousel -->
<div id="demo" class="carousel slide" data-bs-ride="carousel">

  <!-- Indicators/dots -->
  <div class="carousel-indicators">
    <button type="button" data-bs-target="#demo" data-bs-slide-to="0" class="active"></button>
    <button type="button" data-bs-target="#demo" data-bs-slide-to="1"></button>
    <button type="button" data-bs-target="#demo" data-bs-slide-to="2"></button>
  </div>
  
  <!-- The slideshow/carousel -->
  <div class="carousel-inner">
    <div class="carousel-item active">
    
      <img src="data:image/gif;base64,{open_im(brands()[0])}" alt="Los Angeles" class="d-block" style=" width:30%; margin-left:34%; margin-bottom: 15%">
      <div class="carousel-caption">
       
        <h3 style="color: black;">{(bran[br[0]]['text'])}</h3>
        <p style="color: black;">We had such a great time in LA!</p>
      </div>
    </div>
    <div class="carousel-item">
      <img src="data:image/gif;base64,{open_im(brands()[1])}" alt="Chicago" class="d-block" style="width:30%; margin-left:34%; margin-bottom: 15%">
      <div class="carousel-caption">
        <h3 style="color: black;">{(bran[br[1]]['text'])}</h3>
        <p style="color: black;">Thank you, Chicago!</p>
      </div> 
    </div>
    <div class="carousel-item">
      <img src="data:image/gif;base64,{open_im(brands()[2])}" alt="New York" class="d-block" style="width:30%;margin-left:34%; margin-bottom: 10%">
      <div class="carousel-caption">
        <h3 style="color: black;">{(bran[br[2]]['text'])}</h3>
        <p style="color: black;">We love the Big Apple!</p>
      </div>  
    </div>
  </div>
  
  <!-- Left and right controls/icons -->
  <button class="carousel-control-prev" type="button" data-bs-target="#demo" data-bs-slide="prev">
    <span class="carousel-control-prev-icon"></span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#demo" data-bs-slide="next">
    <span class="carousel-control-next-icon"></span>
  </button>
</div>

</body>
</html>
        """)
        with st.container():
            st.header("Hot Brands",)
            col1,col2,col3,col4 = st.columns(4)
            with col1:
              #if 'count' di bawah ini digunakan untuk user ketika mengclick forward maupun back dan setiap click forward dan menambahkan count begitupun sebaliknya untuk back
                if 'count' not in st.session_state:
                    st.session_state.count = 0
                p = st.button('back')
                # di if bawah ini jika count telah melampui 3 akan merteset ke 0
                if p:
                    st.session_state.count += 1
                if st.session_state.count >= len(brands())-1:
                    st.session_state.count = 0
                    st.session_state.count -=1
            with col2:
              #pada not while ketika user tidak mengclick tombol forward dan back maka akan muncul gambar sesuai dengan count
                while not p:
                  #st.image untk memanggil gambar yang berdasarkan function brands() sedangkan count di gunakan untuk memanggil spesifik gambar
                    st.image(brands()[st.session_state.count])
                    break
                  # while digunakan untuk mengganti gambar ketika di click
                while p:
                    st.image(brands()[st.session_state.count])
                    break
            with col3:
                while not p:
                    st.image(brands()[st.session_state.count+1])
                    break
                while p:
                    if st.session_state.count == 0:
                        st.image(brands()[st.session_state.count+2])
                    else:
                        st.image(brands()[st.session_state.count+1])
                    break
            with col4:
                    p = st.button("forward")
                    if p:
                        st.session_state.count += 1
        with st.container():
            st.header("Hot Products",)
            col1,col2,col3,col4 = st.columns(4)
            with col1:
                if 'cou' not in st.session_state:
                    st.session_state.cou = 0
                ppp = st.button('<')
                if ppp:
                    st.session_state.cou += 1
                if st.session_state.cou >= len(brands())-1:
                    st.session_state.cou = 0
                    st.session_state.cou -=1
            with col2:
                while not ppp:
                    st.image(bran['nike']["product"]["image"][st.session_state.cou])
                    break
                while ppp:
                    st.image(bran['nike']["product"]["image"][st.session_state.cou])
                    break
            with col3:
                while not ppp:
                    st.image(bran['nike']["product"]["image"][st.session_state.cou+1])
                    break
                while ppp:
                    if st.session_state.cou == 0:
                        st.image(bran['nike']["product"]["image"][st.session_state.cou+3])
                    else:
                        st.image(bran['nike']["product"]["image"][st.session_state.cou+1])
                    break
            with col4:
                    ppp = st.button(" forward ")
                    if ppp:
                        st.session_state.cou += 1

if selected2 == "Brands":
    with st.container():
        col1,col2 = st.columns(2)
        #for di bawah ini di gunakan untuk mengambil range pada length yang ada di function dan kemudian digunakan untuk memanggil spesifik image dari brands
        for x in range(len(brands())):
          #if di bawah ini untuk membagi image jika image itu genap akan munculk di sebelah kiri sedankan ganjil muncul di sebelah kanan
            if x % 2 == 0:
                with col1:
                    st.image(brands()[x],width=300)
                    st.write(bran[br[x]]['text'])
            else:
                with col2:
                    st.image(brands()[x],width=300)
                    st.write(bran[br[x]]['text'])

if selected2 == "Products":
    with st.container():
        col1,col2,col3 = st.columns(3)
    with col1:
        st.header("filter")
        # pada st.selectbox di gunakan untuk memilih jenis brand dari product yang ingin di tampilkan jika user memilih salah satu maka akan muncul semua product dari brand tersebut
        options = st.selectbox(
    "brands", [x for x in bran.keys()])
    
        for x in range (len(bran[options]["product"]["image"])):
            with col2:
                if x % 2 == 0:
                    st.image(bran[options]["product"]["image"][x])
                    st.write(options)
            with col3:
                if x % 2 == 1:
                    st.image(bran[options]["product"]["image"][x])
                    st.write(options)
with st.container():
    col1,col2,col3 = st.columns(3)
    with col1:
      st.header("brands")
      #lp di bawah sebagai list dari br yang ada pada ti.py
      lp = [x for x in br]
      #dan kemudian dipanggil ke for untuk di tampilkan semua listnya pada st.write
      for x in lp:
        st.write(x)
    with col2:
      st.header("Information")
      lp = ("About Us","Contact Us","Location","Ordering")
      for x in lp:
        st.write(x)
    with col3:
      st.header("Legal")
      lp = ("Privacy Policy","Terms and Condition")
      for x in lp:
        st.write(x)


