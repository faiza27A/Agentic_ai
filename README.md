# 🤖 Agentic AI – E-commerce Customer Support Agent
![Application Screenshot](app-screenshot.png)

## Project Overview

An AI-powered E-commerce Customer Support Agent designed to assist customers with common order-related queries. The application uses Large Language Models (LLMs) and tool calling to understand customer requests and execute relevant backend operations.

The agent can identify when a customer needs order information or wants to cancel an order and call the appropriate backend function.

## Key Features

- **Order Status Tracking:** Retrieve order details and current order status using an order ID.
- **Order Cancellation:** Process order cancellation requests through backend functions.
- **AI-Powered Responses:** Uses an LLM to understand customer questions and select appropriate tools.
- **Tool Integration:** Connects AI decision-making with Python backend functions.
- **Database Integration:** Uses MySQL to access e-commerce order information.
- **Web Interface:** Provides a Streamlit-based interface for customer interaction.

## Technologies Used

- Python
- LangChain
- OpenRouter API
- MySQL
- Streamlit
- Git and GitHub

## Project Structure

```text
AgenticAi/
│
├── app.py
├── app2.py
├── customer_agent.py
├── db_service.py
├── decode.py
├── decode2.py
├── requirements.txt
├── .gitignore
└── README.md
```

## How It Works

1. The customer submits a question through the application.
2. The AI agent analyzes the question.
3. The LLM determines which tool is required.
4. The selected Python function executes the requested operation.
5. The backend retrieves or updates the relevant order information.
6. The application returns the result to the customer.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the Project Folder

```bash
cd AgenticAi
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure Environment Variables

Create a `.env` file in the project directory and configure your API key and database credentials.

Example:

```env
OPENROUTER_API_KEY=your_api_key_here
```

Add the database configuration variables required by your `db_service.py`.

**Important:** Never upload your `.env` file, API keys, or database passwords to GitHub.

### 7. Run the Application

If `app.py` is your Streamlit entry point:

```bash
streamlit run app.py
```

## Learning Outcomes

Through this project, I gained practical experience in:

- Building AI-powered applications using Python.
- Integrating LLMs with backend tools.
- Implementing tool calling using LangChain.
- Connecting Python applications with MySQL.
- Managing API credentials using environment variables.
- Building web interfaces using Streamlit.
- Managing project versions using Git and GitHub.

## Future Enhancements

- Add more customer support operations.
- Implement customer authentication.
- Improve error handling and logging.
- Add conversation history.
- Deploy the application online.

## Author

Developed as a hands-on Agentic AI project to explore practical applications of AI, automation, and backend integration.