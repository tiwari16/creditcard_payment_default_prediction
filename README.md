
# Credit Card Payment Default Prediction Model

This project was done as part of data science internship with [iNeuron](https://internship.ineuron.ai).

The project is written in Python and predicts the probability of credit default based on card holder's
characteristics and payment history for the past 6 months.

## Approach
The credit data for this project is obtained from kaggle [link](https://www.kaggle.com/uciml/default-of-credit-card-clients-dataset).
Data is then loaded in to the cassandra database and extracted via a csv file and loaded in to a Jupyter notebook to perform, data exploration, data cleaning, feature engineering, model training, model validation, model selection, hyperparameter tuning and finally saving it in to a Pickle (.pkl) file. 

The Pickle file contains the final model which is been used to create a python app to load the model and generate prediction based on the input data. I used Streamlit to build the web app for gathering the input. This project is written in python and runs as a Dockerised app. 

This is a binary classification problem and the final model is based on the XGBoost algorithm, predicting with **86% accuracy**.

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

