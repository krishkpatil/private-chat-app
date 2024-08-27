# Preventing Confidential Data Leaks through Nudging

This project introduces a communication platform designed to prevent unauthorized sharing of confidential information using advanced Natural Language Processing (NLP) techniques and behavioral nudges.

## Key Features

- **NLP-Based Message Classification**: Utilizes a BERT-based model trained on the Reuters-21578 dataset to classify messages as Public, Sensitive, or Confidential. This classification is crucial for identifying messages that require user intervention.

- **"Are You Sure?" Nudging Mechanism**: Designed to prompt users before sending potentially sensitive or confidential information. The system employs color-coded nudges:
  - **Red Nudge**: Triggered for confidential information.
    ![Red Nudge](https://i.ibb.co/syDGHRz/conf-ss.jpg)
  - **Yellow Nudge**: Triggered for sensitive information.
    ![Yellow Nudge](https://i.ibb.co/fr24JvT/sens-ss.jpg)

- **Real-Time Interaction**: Implemented using Streamlit, allowing for real-time communication with immediate feedback from the NLP model.
  ![Chat Image](https://i.ibb.co/km4TM58/chat-img.jpg)

- **User Interaction Flow**:
  ![Flow Chart](https://i.ibb.co/H7sdzZP/Flow-chart.png)

## Results

- **Nudge Effectiveness**: 76.9% of users opted to refrain from sending messages after receiving a nudge.
  ![Nudge Effectiveness](https://i.ibb.co/gJgT7PF/Screenshot-2024-08-14-at-1-02-46-AM.jpg)

- **User Misclassification**: Users struggled to differentiate between Sensitive and Confidential information, highlighting the need for improved contextual understanding.
  ![Misclassification Chart](https://i.ibb.co/K5bzbH9/miss.jpg)

## Conclusion

This project demonstrates the effectiveness of digital nudges in preventing data leaks by influencing user behavior. The BERT model’s ability to understand context and the strategic implementation of nudges make this platform a promising tool for enhancing data security.
