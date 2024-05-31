import streamlit as st
import pickle
import numpy as np

svm_model=pickle.load(open('svm_model.pkl','rb'))

def predict(Node_ID,Timestamp,IP_Address,Packet_Rate,Packet_Drop_Rate):
    input=np.array([[Node_ID,Timestamp,IP_Address,Packet_Rate,Packet_Drop_Rate]]).astype(np.float64)
    prediction=svm_model.predict_proba(input)
    pred='{0:{1}f}'.format(prediction[0][0],2)
    return float(pred)

def main():
    st.title("CATCH")
    html_temp= """
        <div style="background-color:#025246 ;padding:10px">
        <h2 style="color:white;text-align:center;">Maliciouse node predection</h2>
         </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    Node_ID = st.text_input("Node ID","Type Here")
    Timestamp = st.text_input("Timestamp","Type Here")
    IP_Address = st.text_input("IP Address","Type Here")
    Packet_Rate = st.text_input("Packet Rate","Type Here")
    Packet_Drop_Rate = st.text_input("Packet Drop Rate","Type Here")


    safe_html="""  
      <div style="background-color:#F4D03F;padding:10px >
       <h2 style="color:white;text-align:center;"> Your node is safe</h2>
       </div>
    """

    danger_html="""  
      <div style="background-color:#F08080;padding:10px >
       <h2 style="color:black ;text-align:center;"> Your node is in danger</h2>
       </div>
    """
if st.button("Predict"):
        output=predict(Node_ID,Timestamp,IP_Address,Packet_Rate,Packet_Drop_Rate)
        st.success('The probability of fire taking place is {}'.format(output))

        if output > 0.5:
            st.markdown(danger_html,unsafe_allow_html=True)
        else:
            st.markdown(safe_html,unsafe_allow_html=True)

if __name__=='__main__':
    main()

