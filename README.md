# Baymax AI - Medical Assistant

Baymax AI is an AI-powered assistant that helps doctors by summarizing clinical data, retrieving patient medical history, and using advanced AI tools like Cortex AI for analysis. This application connects to Snowflake for data storage and retrieval and leverages Cortex AI to generate insights.

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

## License:
MIT License

## Disclaimer:
Ensure you configure the proper credentials for Snowflake and Cortex AI before using this application in production.
