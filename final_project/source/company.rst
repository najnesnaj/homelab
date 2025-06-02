Investment Masters
===================


At Investment Masters, a fictional company specializing in stock market analysis, our mission is to uncover hidden patterns in stock data to inform investment strategies. 


In this project, we focus on the German company Deutz (DEZ.DE) as a case study for pattern recognition. 


While human analysts can visually identify recurring price cycles in Deutz’s stock data, these patterns are challenging to define mathematically or programmatically without advanced techniques. To address this, we leverage Machine Learning (ML) to detect complex patterns. We have compiled a database of quarterly data for approximately 200 German stocks, providing a robust foundation for analysis. Additionally, we developed a synthetic data generator that mimics real stock market behavior, producing quarterly stock data with a specific pattern: a stock price increasing by over 80% four times over 17 years, resulting in cycles of approximately four years. This synthetic data, designed to resemble real-world volatility and randomness, serves as the training set for our neural network model. The ultimate goal is to train an ML model capable of recognizing the Deutz stock’s pattern when fed its real historical data. By deploying this model using Azure Machine Learning, FastAPI, Docker, and Kubernetes, we aim to create an automated, scalable solution for pattern detection. This project, part of the Masterclass Deploying AI Solutions, demonstrates our ability to operationalize ML workflows (MLOps) efficiently. We will document the process, including data preparation, model training, API integration, and deployment, in a comprehensive report, showcasing how this solution integrates into Investment Masters’ investment analysis platform.


