# Blockchain-Based Fake News Detection Ledger

## Manifesto

### Mission Statement
Our mission is to **create and host a blockchain ledger that collects all key public data**, enabling it to be **searched and referenced by the public**. This ledger ultimately aims to provide clarity and transparency into what is truth versus what is not truth, empowering individuals with accurate information in the fight against misinformation.

### Vision
In a world where misinformation spreads rapidly, we envision a decentralized and transparent system where the truth is accessible to everyone. By leveraging blockchain technology and AI-powered verification, our platform will serve as a public repository of validated information, helping to distinguish real news from fake news with unparalleled reliability.

## Current Progress

### Overview
We have successfully built the first version of our blockchain ledger, integrating AI-powered fake content detection. This MVP (Minimum Viable Product) is designed to simulate a blockchain environment where data is stored securely and can be verified for authenticity using a basic AI model.

### Features Implemented
- **Blockchain Ledger**: A simple blockchain implementation in Python, capable of adding new data blocks that include content verification details.
- **AI-Powered Fake News Detection**: An AI model based on a Naive Bayes classifier, trained to identify fake news from a small sample dataset.
- **API Development**: A Flask-based API that allows users to submit content for verification and view the blockchain ledger.

### Detailed Components

#### 1. **Blockchain Functionality**
   - **Data Blocks**: Each block in the blockchain contains an index, timestamp, data (including author, content, and verification status), proof of work, and a hash of the previous block.
   - **Proof of Work**: The blockchain uses a simple proof-of-work algorithm to secure the network and ensure data integrity.
   - **Data Submission**: Users can submit content, which is then analyzed by the AI and stored in the blockchain.

#### 2. **Fake News Detection**
   - **Model**: The AI model uses a Naive Bayes classifier, trained on a small dataset to differentiate between real and fake news.
   - **Prediction**: When content is submitted, the AI model predicts whether it is 'real' or 'fake', and this verification is included in the blockchain data.

#### 3. **API Endpoints**
   - **/submit**: Allows users to submit content for verification. The API returns the block number where the data will be stored, along with the block details.
   - **/chain**: Provides a full view of the blockchain, showing all the blocks currently in the ledger.

### Next Steps
1. **Enhance AI Model**: Expand the training dataset and explore more advanced models like BERT to improve accuracy.
2. **Decentralization**: Investigate moving from a centralized blockchain to a decentralized platform using Ethereum or a custom peer-to-peer network.
3. **User Interface**: Develop a user-friendly web interface for easier public interaction with the ledger.
4. **Public API**: Open up the API for public use, allowing integration with other platforms and services.
5. **Scalability**: Plan for handling larger volumes of data and more users, potentially through off-chain storage or optimized consensus algorithms.

### How to Run the Project

1. **Set Up the Environment**
   - Ensure Python is installed.
   - Install a code editor like Visual Studio Code.

2. **Install Necessary Libraries**
   ```bash
   pip install Flask requests scikit-learn pandas numpy
3. **Run the Application**
* Navigate to the project directory.
Start the Flask server:
    ```bash
    python app.py
4. Interact with the API
* Submit Data: Use Postman or a web browser to submit content to 
`http://localhost:5000/submit`.
* View Blockchain: Access the current blockchain ledger at 
`http://localhost:5000/chain`.