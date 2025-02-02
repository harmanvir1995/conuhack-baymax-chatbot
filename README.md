# Baymax AI - Medical Assistant

Baymax AI is an AI-powered assistant that helps doctors by summarizing clinical data, retrieving patient medical history, and using advanced AI tools like Cortex AI for analysis. This application connects to Snowflake for data storage and retrieval and leverages Cortex AI to generate insights.

<img width="1387" alt="UI" src="https://github.com/user-attachments/assets/a2ec2aaf-81e3-4ab1-b8b3-f4abf70dd253" />



## Technologies Used:
- **Snowflake**: Data storage and querying.
- **Cortex AI**: Clinical data analysis.
- **Streamlit**: Frontend application for user interaction.

## Requirements:
- Snowflake Account
- Python 3.9.x
- Streamlit
- Cortex AI Python SDK
- Pandas

## Setup Instructions:

1. **Clone this repository**:
    ```bash
    git clone https://github.com/yourusername/baymax-ai.git
    ```

2. **Create Snowflake Account**:
    We need to a snowflake account to run this application as the Cortex AI model is deployed on the Snowflake and we are using its APIs to make call.  

3. **Create Database, Schemas, Tables**:
   Create database, schemas and tables to store the data, then create the smentic model to send with the api call.
   
4. **Interact with the app**:
    Copy paste the code in the streamlit application code in your snowflake account.




   


## How it works:
1. The app queries patient medical data from Snowflake using a SQL query.
2. It then sends the retrieved data to Cortex AI for analysis.
3. The results are displayed in the Streamlit frontend for easy visualization.


<img width="1444" alt="UI-1" src="https://github.com/user-attachments/assets/15c072d2-320d-45de-8ea9-eb10c8a587bb" />

<img width="1478" alt="UI-2" src="https://github.com/user-attachments/assets/c60c11c5-962c-4ec1-81d8-184b0f52bd03" />
