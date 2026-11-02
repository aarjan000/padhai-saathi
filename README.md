📚 Padhai Saathi – AI Quiz Maker



Padhai Saathi is an AI-powered quiz generator built with Python, Flask, and Groq. It helps students create multiple-choice quizzes on any topic using AI.



✨Features



\- Generate AI-powered multiple-choice questions.

\- Choose a topic for your quiz.

\- Customize the number of questions (1–20).

\- Get four answer options (A, B, C, D) for each question.

\- Receive structured JSON responses from the AI model.

\- Simple web application powered by Flask.



🛠️Tech Stack



\- Python – Core programming language

\- Flask – Backend web framework

\- Groq API – AI model access

\- GPT-OSS-120B – Language model

\- HTML – Frontend

\- python-dotenv – Environment variable management



📁 Project Structure



text

padhai-saathi/

│

├── main.py

├── templates/

│   └── index.html

├── .env

├── .gitignore

└── README.md





⚙️Installation and Setup



1\. Clone the repository



```bash

git clone https://github.com/aarjan000/padhai-saathi.git

cd padhai-saathi

```



2\. Install dependencies



```bash

pip install flask groq python-dotenv

```



3\. Configure your API key



Create a `.env` file in the project root directory:



```env

GROQ\_API\_KEY=your\_groq\_api\_key\_here

```



Replace `your\_groq\_api\_key\_here` with your own Groq API key.





4\. Run the application



```bash

python main.py

```



Open your browser and visit:



```text

http://127.0.0.1:5000

```



🔑 Environment Variables



| Variable | Description |

|---|---|

| `GROQ\_API\_KEY` | Your Groq API key |



🚀 Future Improvements



\- Add quiz scoring and evaluation.

\- Display correct answers after quiz submission.

\- Add difficulty levels (Easy, Medium, Hard)

\- Support different classes and subjects.

\- Save quiz history and results.



👨‍💻 Author



Aarjan Acharya



GitHub: \[@aarjan000](https://github.com/aarjan000)









