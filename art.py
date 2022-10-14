import streamlit as st
import pandas as pd
import numpy as np
import data
import pre_model as pm
#import my_trainmodel2.pt

# import sys
# import io
# sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
# sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

st.header("미술 큐레이션 마음돌봄 서비스")
st.write("텍스트를 통해 당신의 감성을 인공지능이 분석하여 당신만을 위한 그림을 추천해 드립니다. Enjoy!"
"""
***
""")


def main() :
    
    # 유저한테 입력을 받는 방법

    # 1. 이름 입력 받기
    name = st.text_input('이름을 입력하세요!')

    if name != '' :
        st.subheader(name + '님 안녕하세요??')

    # 2. 입력 글자 갯수 제한
    address = st.text_input('오늘 당신에게 있었던 일을 들려 주세요', max_chars=60)
    st.subheader(address)

    #mymodel = torch.load("my_trainmodel2.pt")
    #pred = my_model(새로운 데이)
    
if __name__ == "__main__" :
    main()


start = st.button("분석 시작")

model = pm.load_model( )
pm.predict(address)

# # data.get_address("기쁨")

data.get_address(predicted)



stop = st.button("Reset")


st.text("오늘 하루 일로 인해 많이 피곤하셨군요...")
st.text('당신의 기분 전환을 위해 추천된 그림은 입니다...')   


# import streamlit as st
# from PIL import Image

# def main() :
    
#     # 인터넷상에 있는 이미지를 화면에 표시하기
#     # URL이 있는 이미지를 말한다.
    
#     url = 'https://t1.daumcdn.net/cfile/tistory/145134574E2FBF6519'
#     st.image(url)
#     st.text('사진출처 : https://https://duga.tistory.com/550')

# if __name__ == "__main__" :
#     main()


import streamlit as st
from PIL import Image

def main() :
    
    img = Image.open('C:/Users/user/Desktop/project/art/example.jpg')
    st.image(img)

if __name__ == "__main__" :
    main()



# ######################
# # Input molecules
# ######################

# st.header('User Input Features')

# ## Read SMILES input
# SMILES_input = ("")

# SMILES = st.text_area("SMILES input", SMILES_input)
# SMILES = "C\n" + SMILES #Adds C as a dummy, first item
# SMILES = SMILES.split('\n')

# st.header('Input SMILES')
# SMILES[1:] # Skips the dummy first item

# ## Calculate molecular descriptors
# st.header('Computed molecular descriptors')
# X = generate(SMILES)
# X[1:] # Skips the dummy first item

# ######################
# # Pre-built model
# ######################

# # Reads in saved model
# load_model = pickle.load(open('solubility_model.pkl', 'rb'))

# # Apply model to make predictions
# prediction = load_model.predict(X)
# #prediction_proba = load_model.predict_proba(X)

# st.header('Predicted LogS values')
# prediction[1:] # Skips the dummy first item