**GAME-ON – Automatic Ticket Categorization System**
This application automatically categorizes and routes customer complaints for the GAME-ON gaming app using Machine Learning. It helps support teams handle tickets faster and more accurately.
1. Problem Statement
As the number of users grows, manually reading and routing complaints becomes inefficient. This system classifies complaints into predefined categories and routes them to the correct team.

2. Design Choice
I have chosen Logistic Regression + TF-IDF.
1. Why TF-IDF for Text Representation?
TF-IDF (Term Frequency – Inverse Document Frequency) converts raw text into meaningful numerical features by measuring how important a word is to a document relative to the entire corpus.

Justification:
Complaint texts are short, keyword-driven, and domain specific
Keywords like refund, charged, login, crash strongly indicate categories
TF-IDF captures this importance better than simple word counts
Advantages in this use case:
Works very well for classic text classification problems
Reduces the impact of common words (e.g., the, is, and)
Lightweight and fast to train
Easy to interpret which words influence predictions
Requires less data compared to deep learning models
Why not embeddings initially?
mbeddings (Word2Vec, BERT) need more data and compute
Overkill for a structured complaint routing problem
Harder to debug and explain decisions to stakeholders

3. Why Logistic Regression for Classification?
Logistic Regression is a strong linear baseline model for text classification.
Justification:
Works extremely well with high-dimensional sparse data like TF-IDF
Produces probability scores, enabling:
Confidence-based routing
Thresholding (e.g., route to “Other” if confidence < 0.25)
Fast training and inference — ideal for real-time ticketing systems
Stable and less prone to overfitting on small/medium datasets
Advantages in this project:
Easy to deploy on low-cost infrastructure (AWS EC2 free tier)
Highly interpretable (feature weights explain predictions)
Industry-standard baseline for NLP classification tasks

4. Complaint Categories with Examples
Billing
- I was charged twice for my GAME-ON premium subscription
- Refund for my in-game purchase is still not credited
- Money deducted but gems were not added to my account
Technical
- GAME-ON crashes when I start a multiplayer match
- Game freezes on the loading screen
- Unable to connect to the GAME-ON servers
Product
- Matchmaking is unfair and unbalanced
- Rewards system is not working as expected
- New update removed important game features
Account
- Unable to login to my GAME-ON account
- Password reset link is not working
- My account got locked without explanation
Other
- Customer support is not responding
- Overall experience with GAME-ON is disappointing
- I have a general feedback about the game
  
5. System Architecture
- Streamlit UI for complaint submission and dashboard
- Text preprocessing using NLP techniques
- Machine Learning model for classification
- Confidence-based routing logic
- CSV file storage for ticket persistence
  
6. Workflow / Order of Execution
1. User enters complaint in Streamlit UI
2. Text is preprocessed (cleaning, lemmatization)
3. Model predicts category and confidence
4. Low-confidence complaints are marked as Pending Review
5. Valid tickets are appended to a CSV file
6. Dashboard reads from CSV and displays tickets with filters
   
7. How to Run the App
1. Create a virtual environment and activate it
2. Install dependencies using requirements.txt
3. Run the app using: streamlit run app.py
4. Open the browser and start submitting complaints
   
8. Data Storage
Ticket data is stored in a CSV file instead of a database. Each ticket record contains Ticket ID, Complaint Text, Predicted Category, Routed Team, Confidence Score, Status, and Created Date.

9. Specific Files
Generated synthetic data- synthetic_complaints_new2.csv
cleaned synthetic data-cleaned_complaints_new2.csv
Stored complaints- ticket_predictions_new.csv

10. Key Features
- Automatic ticket categorization
- Confidence-based validation
- Daily-reset ticket ID generation
- Interactive dashboard with filters
- Simple CSV-based persistence
- Easy deployment on AWS EC2
