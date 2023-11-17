import numpy as np 
import pickle
import streamlit as st 
from twilio.rest import Client
model=pickle.load(open('C:/Users/GAURAV PRATAP SINGH/Downloads/trained_model.sav','rb'))

def credit_fraudprediction(features,user_mobile):
#  features_as_numpy_array=np.asarray(features)
#  features = np.array(features) 
#  features = features.reshape(-1, 1)

 Predictions= model.predict(features)
 
 if(Predictions[0]==1):
        account_sid = "AC2ef05c93a74ad2a5e2d1e66fe899dadf"
        auth_token = "a7a60167ccca5d995520c1ddf5902184"
        client = Client(account_sid, auth_token)

        # Define the message to be sent
        message = client.messages.create(
            body="Your credit card transaction appears to be fraudulent. Please contact your bank.",
            from_="+17344695159",
            to=user_mobile
        )
        st.success("Fraud detected. Message sent to your mobile.")

  
 else:
    st.success("No fraud detected. Your transaction is secure.")


def main():


    st.title("Credit Card Fraud Detection Web App")

    st.write(""" About
Credit card fraud is a form of identity theft that involves an unauthorized taking of another's credit card information for the purpose of charging purchases to the account or removing funds from it.

**This Streamlit App utilizes a Machine Learning API in order to detect fraudulent credit card based on the following criteria: hours, type of transaction, amount, balance before and after the transaction, etc.**

""")


    st.header('Input Features of The Transaction')

    step = st.selectbox("""Specify its value""",(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19))
    modeofpaym= st.sidebar.subheader(f"""
                    Enter Type of Transfer Made:\n\n\n\n
                    0 for 'Cash In' Transaction\n 
                    1 for 'Cash Out' Transaction\n 
                    2 for 'Debit' Transaction\n
                    3 for 'Payment' Transaction\n  
                    4 for 'Transfer' Transaction\n""")
    modeofpaym = st.selectbox("",(0,1,2,3,4))
    x = ''
    if modeofpaym == 0:
        x = 'Cash in'
    if modeofpaym == 1:
        x = 'Cash Out'
    if modeofpaym == 2:
        x = 'Debit'
    if modeofpaym == 3:
        x = 'Payment'
    if modeofpaym == 4:
        x =  'Transfer'
        
    amount = st.number_input("Amount in $",min_value=0, max_value=110000)
    oldbalanceOrg = st.number_input("""Original Balance Before Transaction was made""",min_value=0, max_value=110000)
    newbalanceOrig= st.number_input("""New Balance After Transaction was made""",min_value=0, max_value=110000)
    oldbalanceDest= st.number_input("""Old Balance""",min_value=0, max_value=110000)
    newbalanceDest= st.number_input("""New Balance""",min_value=0, max_value=110000)
    isFlaggedFraud = st.selectbox("""Specify if this was flagged as Fraud by your System: """,(0,1))
    features=([[step,modeofpaym,amount,oldbalanceOrg,newbalanceOrig,oldbalanceDest,newbalanceDest,isFlaggedFraud]])
    user_mobile = st.text_input("Enter your mobile number:")
    transaction_amount = st.number_input("Enter transaction amount:")
    values = " "
    if st.button("Detection Result"):
       credit_fraudprediction(features,user_mobile)

if __name__  == '__main__' :
    main()
   

