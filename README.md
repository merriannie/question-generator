# Question Generator

## Project Overview

This is a basic web app built in Python using FastAPI for the backend and a basic HTML and CSS frontend. It is designed to be a simple learning project, but it is still functional.

My name is Mercy Yaa Nyarko and I created this project as part of my learning journey in web development using html and css and python.

## Steps / Approach

1. A basic form where the user inputs a subject, topic, and number of questions
2. Upon submission, the data is sent to the backend
3. The backend receives this info and attempts to retrieve questions from an external question service
4. If the service is up and running, the generated questions are displayed on the page
5. If the service is down, the app uses some built-in fallback questions so that the app does not break
6. The results are displayed in an organized, simple layout on the webpage.

## Future Improvements

There are a somethings I would like to improve in the future. This includes:

- Making the design look nicer and modern .
- Add better error messages when the external service is unavailable.
- Let users choose different difficulty levels for the questions.
- Save generated questions so users can view them later.
- Add more features to make the app feel more complete.

## How to Run

1. Open the project folder in the terminal.
2. Run the app with:

```bash
.\.venv\Scripts\python.exe main.py
```

3. Open your browser and go to:

```text
http://127.0.0.1:3003/
```

## Notes

This project is a basic but good example of how a simple web app can work. I am still learning and I hope I can improve it more in the future.
