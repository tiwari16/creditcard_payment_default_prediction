
# Credit Card Payment Default Prediction Model

This project was done as part of data science internship with [iNeuron](https://internship.ineuron.ai).

The project is written in Python and predicts the probability of credit default based on card holder's
characteristics and payment history for the past 6 months.

## Approach
The credit data for this project is obtained from kaggle [Link](https://www.kaggle.com/uciml/default-of-credit-card-clients-dataset).
Data is then loaded in to the cassandra database and extracted via a csv file and loaded in to a Jupyter notebook to perform, data exploration, data cleaning, feature engineering, model training, model validation, model selection, hyperparameter tuning and finally saving it in to a .pkl file. This is a binary classifiaction problem. The final model used is based on the XGBoost algorithm. XGBoost is an optimized gradient boosting library, it provides a parallel tree boosting and implements under the Gradient Boosting framework.
The .pkl file contains the final model which is been used to create app.py file to load the model and generate prediction from input data which will be recieved from the Streamlit web app page. Streamlit is an open-source python library which allows to create a web application for free. This project is mostly written in python using pycharm IDE. This application is then deployed via Dockerised app. Currently model is predicting with 86% accuracy.

## Technologies

### Analysis and Model Building

* Jupyter
* Pycharm

### Model Deployment

* Streamlit
* Docker
## Run locally

Use docker to build and run:
`docker build -t ccdefault:latest . && docker run -it -p 8501:8501 ccdefault:latest`

Then access the app at:
`http://localhost:8501`
## Acknowledgements

 Lichman, M. (2013). UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science.

## App Reference

#### Input Parameter

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `LIMIT_BAL` | `float64` | **Required**. Amount of given credit |

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `SEX` | `int64` | **Required**. Gender (1=male, 2=female) |

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `EDUCATION` | `int64` | **Required**. (1=graduate school, 2=university, 3=high school, 4=others, 5=unknown, 6=unknown) |

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `MARRIAGE` | `int64` | **Required**. Marital status (1=married, 2=single, 3=others) |

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `AGE` | `int64` | **Required**. Age in years |

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `PAY_0` | `int64` | **Required**. Repayment status for 1st month(-1=pay duly, 1=payment delay for one month, 2=payment delay for two months, … 8=payment delay for eight months, 9=payment delay for nine months and above) |

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `PAY_2` | `int64` | **Required**. Repayment status for 2nd month(-1=pay duly, 1=payment delay for one month, 2=payment delay for two months, … 8=payment delay for eight months, 9=payment delay for nine months and above) |

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `PAY_3` | `int64` | **Required**. Repayment status for 3rd month(-1=pay duly, 1=payment delay for one month, 2=payment delay for two months, … 8=payment delay for eight months, 9=payment delay for nine months and above) |

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `PAY_4` | `int64` | **Required**. Repayment status for 4th month(-1=pay duly, 1=payment delay for one month, 2=payment delay for two months, … 8=payment delay for eight months, 9=payment delay for nine months and above) |

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `PAY_5` | `int64` | **Required**. Repayment status for 5th months(-1=pay duly, 1=payment delay for one month, 2=payment delay for two months, … 8=payment delay for eight months, 9=payment delay for nine months and above) |

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `PAY_6` | `int64` | **Required**. Repayment status for 6th month(-1=pay duly, 1=payment delay for one month, 2=payment delay for two months, … 8=payment delay for eight months, 9=payment delay for nine months and above) |

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `BILL_AMT1` | `float64` | **Required**. Amount of bill statement for 1st month|

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `BILL_AMT2` | `float64` | **Required**. Amount of bill statement for 2nd month |

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `BILL_AMT3` | `float64` | **Required**. Amount of bill statement for 3rd month |

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `BILL_AMT4` | `float64` | **Required**. Amount of bill statement for 4th month |

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `BILL_AMT5` | `float64` | **Required**. Amount of bill statement for 5th month|

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `BILL_AMT6` | `float64` | **Required**. Amount of bill statement for 6th month |

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `PAY_AMT1` | `float64` | **Required**. Amount of due payment recieved for 1st month |

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `PAY_AMT2` | `float64` | **Required**. Amount of due payment recieved for 2nd month |

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `PAY_AMT3` | `float64` | **Required**. Amount of due payment recieved for 3rd month |

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `PAY_AMT4` | `float64` | **Required**. Amount of due payment recieved for 4th month |

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `PAY_AMT5` | `float64` | **Required**. Amount of due payment recieved for 5th month |

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `PAY_AMT6` | `float64` | **Required**. Amount of due payment recieved for 6th month |


#### Output

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `default.payment.next.month`      | `int` | **One** if customer will default otherwise **Zero**|


## Appendix

Dataset Information:

The dataset for this project was obtained from Kaggle. It contains information on default payments, demographic factors, credit data, history of payment, and bill statements of credit card clients in Taiwan from April 2005 to September 2005.

Content:

There are 25 variables:

1. ID: ID of each client
2. LIMIT_BAL: Amount of given credit in NT dollars (includes individual and family/supplementary credit
3. SEX: Gender (1=male, 2=female)
4. EDUCATION: (1=graduate school, 2=university, 3=high school, 4=others, 5=unknown, 6=unknown)
5. MARRIAGE: Marital status (1=married, 2=single, 3=others)
6. AGE: Age in years
7. PAY_0: Repayment status in September, 2005 (-1=pay duly, 1=payment delay for one month, 2=payment delay for two months, … 8=payment delay for eight months, 9=payment delay for nine months and above)
8. PAY_2: Repayment status in August, 2005 (scale same as above)
9. PAY_3: Repayment status in July, 2005 (scale same as above)
10. PAY_4: Repayment status in June, 2005 (scale same as above)
11. PAY_5: Repayment status in May, 2005 (scale same as above)
12. PAY_6: Repayment status in April, 2005 (scale same as above)
13. BILL_AMT1: Amount of bill statement in September, 2005 (NT dollar)
14. BILL_AMT2: Amount of bill statement in August, 2005 (NT dollar)
15. BILL_AMT3: Amount of bill statement in July, 2005 (NT dollar)
16. BILL_AMT4: Amount of bill statement in June, 2005 (NT dollar)
17. BILL_AMT5: Amount of bill statement in May, 2005 (NT dollar)
18. BILL_AMT6: Amount of bill statement in April, 2005 (NT dollar)
19. PAY_AMT1: Amount of previous payment in September, 2005 (NT dollar)
20. PAY_AMT2: Amount of previous payment in August, 2005 (NT dollar)
21. PAY_AMT3: Amount of previous payment in July, 2005 (NT dollar)
22. PAY_AMT4: Amount of previous payment in June, 2005 (NT dollar)
23. PAY_AMT5: Amount of previous payment in May, 2005 (NT dollar)
24. PAY_AMT6: Amount of previous payment in April, 2005 (NT dollar)
25. default.payment.next.month: Default payment (1=yes, 0=no)



## Authors

- [@tiwari16](https://github.com/tiwari16/creditcard_payment_default_prediction)

