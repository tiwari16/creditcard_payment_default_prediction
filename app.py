import numpy as np
import pickle
import pandas as pd
import streamlit as st
from PIL import Image

pickle_in = open('Models/finalxgb_model.pkl', 'rb')
classifier = pickle.load(pickle_in)


def credit_card_payment_default(LIMIT_BAL, SEX, EDUCATION, MARRIAGE, AGE, PAY_0, PAY_2,
                                PAY_3, PAY_4, PAY_5, PAY_6, BILL_AMT1, BILL_AMT2,
                                BILL_AMT3, BILL_AMT4, BILL_AMT5, BILL_AMT6, PAY_AMT1,
                                PAY_AMT2, PAY_AMT3, PAY_AMT4, PAY_AMT5, PAY_AMT6):
    """Let's predict the default payments
    This is using docstrings for specifications
    ---
    parameters:
      - name: LIMIT_BAL
        in: query
        type: number
        required: true
      - name: SEX
        in: query
        type: number
        required: true
      - name: EDUCATION
        in: query
        type: number
        required: true
        name: MARRIAGE
        in: query
        type: number
        required: true
        - name: AGE
        in: query
        type: number
        required: true
        name: PAY_0
        in: query
        type: number
        required: true
        name: PAY_2
        in: query
        type: number
        required: true
        name: PAY_3
        in: query
        type: number
        required: true
        name: PAY_4
        in: query
        type: number
        required: true
        name: PAY_5
        in: query
        type: number
        required: true
        name: PAY_6
        in: query
        type: number
        required: true
        name: BILL_AMT1
        in: query
        type: number
        required: true
        name: BILL_AMT2
        in: query
        type: number
        required: true
        name: BILL_AMT3
        in: query
        type: number
        required: true
        name: BILL_AMT4
        in: query
        type: number
        required: true
        name: BILL_AMT5
        in: query
        type: number
        required: true
        name: BILL_AMT6
        in: query
        type: number
        required: true
        name: PAY_AMT1
        in: query
        type: number
        required: true
        name: PAY_AMT2
        in: query
        type: number
        required: true
        name: PAY_AMT3
        in: query
        type: number
        required: true
        name: PAY_AMT4
        in: query
        type: number
        required: true
        name: PAY_AMT5
        in: query
        type: number
        required: true
        name: PAY_AMT6
        in: query
        type: number
        required: true

    responses:
        200:
            description: The output values

    """

    # prediction = classifier.predict((pd.DataFrame([[LIMIT_BAL, SEX, EDUCATION, MARRIAGE, AGE, PAY_0, PAY_2,
    #                                                 PAY_3, PAY_4, PAY_5, PAY_6, BILL_AMT1, BILL_AMT2,
    #                                                 BILL_AMT3, BILL_AMT4, BILL_AMT5, BILL_AMT6, PAY_AMT1,
    #                                                 PAY_AMT2, PAY_AMT3, PAY_AMT4, PAY_AMT5, PAY_AMT6]])))

    prediction = classifier.predict((pd.DataFrame([[20000.0, 2, 2, 1, 24, 2, 2,
                                                    -1, -1, -2, -2, 3198.0, 3102.0,
                                                    3198.0, 3198.0, 0.0, 0.0, 689.0,
                                                    0.0, 0.0, 0.0, 685.0, 798.0]])))

    print(prediction)
    return prediction


def main():
    st.title("Credit Card Default Payment Prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Credit Card Payment Default Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    LIMIT_BAL = st.text_input("AMOUNT OF GIVEN CREDIT", 40000.0)
    SEX = st.text_input("GENDER (1=Male, 2=Female)", 1)
    EDUCATION = st.text_input("EDUCATION (1=Graduate School, 2=University, 3=High School, 4=Others, 5=Unknown, 6=Unknown)", 2)
    MARRIAGE = st.text_input("MARRIAGE (Marital status (1=Married, 2=Single, 3=Others)", 1)
    AGE = st.text_input("AGE (Age in years)", 36)
    PAY_0 = st.text_input("REPAYMENT1(-1=Pay Duly,1= Pmt Delay For 1 Month,2=Pmt Delay For 2 Months and so on",-1)
    PAY_2 = st.text_input("REPAYMENT2(-1=Pay Duly,1= Pmt Delay For 1 Month,2=Pmt Delay For 2 Months and so on",-1)
    PAY_3 = st.text_input("REPAYMENT3(-1=Pay Duly,1= Pmt Delay For 1 Month,2=Pmt Delay For 2 Months and so on",2)
    PAY_4 = st.text_input("REPAYMENT4(-1=Pay Duly,1= Pmt Delay For 1 Month,2=Pmt Delay For 2 Months and so on",-1)
    PAY_5 = st.text_input("REPAYMENT5(-1=Pay Duly,1= Pmt Delay For 1 Month,2=Pmt Delay For 2 Months and so on",-1)
    PAY_6 = st.text_input("REPAYMENT6(-1=Pay Duly,1= Pmt Delay For 1 Month,2=Pmt Delay For 2 Months and so on",-1)
    BILL_AMT1 = st.number_input("Amount Due 1st Month", 0.0)
    BILL_AMT2 = st.number_input("Amount Due 2nd Month", 0.0)
    BILL_AMT3 = st.number_input("Amount Due 3rd Month",0.0 )
    BILL_AMT4 = st.number_input("Amount Due 4th Month", 0.0)
    BILL_AMT5 = st.number_input("Amount Due 5th Month", 0.0)
    BILL_AMT6 = st.number_input("Amount Due 6th Month", 0.0)
    PAY_AMT1 = st.number_input("Payment Recieved 1st Month", 0.0)
    PAY_AMT2 = st.number_input("Payment Recieved 2nd Month", 0.0)
    PAY_AMT3 = st.number_input("Payment Recieved 3rd Month", 0.0)
    PAY_AMT4 = st.number_input("Payment Recieved 4th Month", 0.0)
    PAY_AMT5 = st.number_input("Payment Recieved 5th Month",0.0)
    PAY_AMT6 = st.number_input("Payment Recieved 6th Month",0.0)

    result = ""
    if st.button("Predict"):
        result = credit_card_payment_default(LIMIT_BAL, SEX, EDUCATION, MARRIAGE, AGE, PAY_0, PAY_2,
                                             PAY_3, PAY_4, PAY_5, PAY_6, BILL_AMT1, BILL_AMT2,
                                             BILL_AMT3, BILL_AMT4, BILL_AMT5, BILL_AMT6, PAY_AMT1,
                                             PAY_AMT2, PAY_AMT3, PAY_AMT4, PAY_AMT5, PAY_AMT6)

        st.success('The Output Is {}'.format(result))

        if result>0:
            st.write ('Customer will default the payment')
        else:
             st.write('Customer will not default the payment')


if __name__ == '__main__':
    main()
