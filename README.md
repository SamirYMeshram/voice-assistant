# voice-assistant

Here’s a detailed **README.md** file for your project:

---

# **Joe - AI Voice Assistant**

Joe is an intelligent AI voice assistant designed to assist users with a variety of tasks. This assistant can respond to voice commands, fetch information from APIs, play music, schedule tasks, open applications, and much more. It is powered by Python and integrates several libraries and APIs to provide a seamless user experience.

---

## **Features**
- **Voice Commands**: Understands user speech and responds using text-to-speech.
- **Weather Updates**: Fetches real-time weather reports for any city using OpenWeatherMap API.
- **Wikipedia Search**: Provides summaries of topics from Wikipedia.
- **Google Search**: Opens Google for any specified search term.
- **Task Scheduling**: Allows users to schedule tasks or set reminders.
- **Music Control**: Plays local music or searches for it on YouTube.
- **Application Launch**: Opens applications like Chrome, Notepad, or Calculator.
- **Screenshot Capture**: Captures and saves a screenshot of the desktop.
- **News Updates**: Opens a news website for the latest updates.
- **Integration with Gemini AI**: Uses Gemini AI to provide explanations, summaries, and task execution.
- **Data Persistence**: Saves notes, tasks, and reminders in a JSON file for later retrieval.

---

## **Installation**

### **Prerequisites**
- Python 3.7 or later
- The following Python libraries (install via `pip`):
  ```bash
  pip install speechrecognition pyttsx3 requests wikipedia pygame pyautogui apscheduler
  ```

### **Setup**
1. Clone the repository:
   ```bash
   git clone https://github.com/SamirYMeshram/Joe-AI-Assistant.git
   cd Joe-AI-Assistant
   ```
2. Create a `assistant_data.json` file in the root directory for storing notes and reminders:
   ```json
   {}
   ```
3. Add your **OpenWeatherMap API key** and **Gemini API key** in the script:
   - Replace `"30816f4fea5fd2bd505c7c6b5562e6cd"` with your OpenWeatherMap API key.
   - Replace `"AIzaSyCQZzOBPLIffz2kjD_aGInNPJRHYjk5bNw"` with your Gemini API key.

4. Run the assistant:
   ```bash
   python main.py
   ```

---

## **Usage**

### **Basic Commands**
| Command Example           | Description                                      |
|---------------------------|--------------------------------------------------|
| **"hello"**               | Greets the user.                                 |
| **"how are you"**         | Joe responds with a friendly message.            |
| **"what is your name"**   | Joe introduces itself.                           |
| **"time"**                | Tells the current time.                          |
| **"weather in [city]"**   | Provides the current weather of the specified city. |
| **"search [term]"**       | Searches for the term on Google.                 |
| **"open [app]"**          | Opens applications like Chrome or Notepad.       |
| **"take a note [content]"** | Saves a note to the JSON file.                  |
| **"schedule [task]"**     | Schedules a task.                                |
| **"play music [song]"**   | Plays local music or searches for it on YouTube. |
| **"wikipedia [topic]"**   | Fetches a Wikipedia summary for the topic.       |
| **"news"**                | Opens the BBC News website.                      |
| **"goodbye" / "exit"**    | Closes the assistant.                            |

### **Advanced Features**
- **Gemini AI Integration**: Ask Joe to explain or summarize topics using Gemini AI. Example:  
  - *"Explain quantum physics."*
- **Reminders**: Set a reminder with commands like:  
  - *"Set a reminder at 3 PM to call John."*
- **Take Screenshots**: Simply say:  
  - *"Take a screenshot."*

---

## **Architecture**

1. **Speech Recognition**:
   - Listens to user commands using `speech_recognition`.
   - Converts speech to text.
   
2. **Query Handling**:
   - Processes the text and matches it with pre-defined commands.
   
3. **Task Execution**:
   - Performs corresponding actions like fetching weather data, playing music, or opening applications.

4. **Text-to-Speech**:
   - Converts responses into audio using `pyttsx3`.

5. **Data Persistence**:
   - Notes, tasks, and reminders are saved in `assistant_data.json`.

---

## **File Structure**
```plaintext
Joe-AI-Assistant/
│
├── main.py                  # Main script for the assistant
├── assistant_data.json      # JSON file for storing notes and tasks
├── assistant_log.log        # Log file for tracking activities and errors
└── README.md                # Documentation for the project
```

---

## **APIs and Libraries**
### **1. OpenWeatherMap API**
- Provides weather data.
- [Sign up for an API key](https://openweathermap.org/api) to use it.

### **2. Gemini AI**
- Used for explanations, summaries, and task handling.
- Add your API key in the script to enable this feature.

### **3. Wikipedia API**
- Fetches brief summaries of topics.

---

## **Known Issues**
- Limited support for applications outside Chrome, Notepad, and Calculator.
- API keys are hardcoded; it's recommended to use environment variables for better security.
- The Gemini AI feature may not work if the API key is invalid or if there's a network issue.

---

## **Future Improvements**
- Add support for more applications (e.g., Word, Excel).
- Use OpenAI's ChatGPT API for dynamic, conversational responses.
- Integrate with Google Calendar API for task scheduling.
- Expand music playback capabilities with Spotify or YouTube Music APIs.
- Enhance error handling and user query understanding using NLP tools like `spaCy`.

---

## **Author**
- **Name**: Samir Yogendra Meshram  
- **Email**: [sameerymeshram](mailto:sameerymeshram)  
- **GitHub**: [SamirYMeshram](https://github.com/SamirYMeshram)

---

## **License**
This project is open-source. You are free to use, modify, and distribute it under the terms of the [MIT License](https://opensource.org/licenses/MIT).  

Feel free to contribute to this project by submitting pull requests or reporting issues!

--- 

Let me know if you'd like any adjustments to this README file!