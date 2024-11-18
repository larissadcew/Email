# 📧 Email - Web-Based Email Client  

The **Email** project is a web application that replicates the core functionality of an email client. Built using **Django** and **JavaScript**, it enables users to send, receive, and manage emails through an interactive and responsive interface.  

---

## 🔍 What Does This Project Do?  

This application provides the following key features:  
- **Inbox Management**: View all received emails, including read/unread statuses. 📨  
- **Sent Mail Tracking**: Access emails sent by the user. ✉️  
- **Archive Functionality**: Archive and unarchive emails to manage clutter. 📂  
- **Email Composition**: Create and send emails with ease. ✍️  
- **Dynamic Updates**: Seamless interaction powered by JavaScript. ⚡  

---

## 🛠️ Technologies Used  

### 1. **Django Framework**  
- **Back-End**: Implements the logic for email storage, sending, and user authentication.  
- **Django REST Framework**: Provides APIs for email management.  

### 2. **JavaScript**  
- **Fetch API**: Handles asynchronous requests for seamless updates.  
- **Dynamic Rendering**: Renders emails and updates UI without full-page reloads.  

### 3. **HTML and CSS**  
- **HTML**: Structures the pages for inbox, sent mail, archives, and composition.  
- **CSS**: Styles the interface for a clean and user-friendly experience.  

### 4. **SQLite**  
- Database for storing user accounts, email data, and archive states.  

---

## 🔧 How It Works  

### 1. User Interface  
- Users interact with four primary views:  
  - **Inbox**: Displays received emails, showing sender, subject, and read status.  
  - **Sent**: Lists all emails sent by the user.  
  - **Archive**: Allows users to retrieve archived emails.  
  - **Compose**: Provides a form for creating and sending new emails.  

### 2. Email Composition  
- Users specify recipients, subject, and body content.  
- Emails are sent and saved to the database for later retrieval.  

### 3. Inbox Functionality  
- Emails are fetched dynamically using the **Fetch API**.  
- Read/unread status is toggled directly in the interface.  

### 4. Archiving  
- Emails can be archived or unarchived with a single click.  
- Archive status is updated in real-time via API calls.  

### 5. API Endpoints  
The application uses Django APIs to handle:  
- **Fetching Emails**: Retrieve email data for inbox, sent, or archive views.  
- **Sending Emails**: Save new emails to the database and send them to recipients.  
- **Updating Status**: Mark emails as read/unread or archived/unarchived.  

---

## 📊 Database Models  

### 1. **User**  
- Utilizes Django's built-in authentication system.  

### 2. **Email**  
- **Fields**: `sender`, `recipients`, `subject`, `body`, `timestamp`, `read`, `archived`.  
- **Relationships**: Links to users for sender and recipient information.  

---

## 🎯 Applications  

This project is an excellent example of:  
- **Web Application Development**: Combining Django and JavaScript for dynamic, feature-rich applications.  
- **API Integration**: Utilizing RESTful APIs for seamless data interactions.  
- **Email Management**: Understanding how email systems are structured and function.  

---

## 🌟 Why Use This Project?  

- **Educational**: Learn how to build a responsive, full-stack web application.  
- **Practical**: Adapt the project to create a personalized email client or integrate it into larger systems.  
- **Scalable**: Add advanced features like search functionality, email threading, or integration with real SMTP servers.  

---  

Feel free to explore and expand this project. Happy coding! 🚀  
