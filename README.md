# Traffic Management System

This repository contains a Traffic Management System that integrates Google Maps, an AI-powered traffic prediction model, and real-time data to simulate traffic congestion and predict traffic levels based on various factors such as time, weather, and holidays. The system also includes user authentication via Google OAuth.

## Features

- **AI Traffic Predictor**: Utilizes an AI model to predict traffic levels based on user inputs like location, date, time, day of the week, weather conditions, and holiday status.
- **Google Maps Integration**: Displays a map where users can select a location for traffic prediction and routing.
- **User Authentication**: Supports Google OAuth for login functionality, allowing users to securely access the platform.
- **Simulations**: Interactive traffic signal simulator for managing traffic flow in real time.
- **Shortest Route Calculator**: Provides the shortest route suggestion considering traffic congestion.
- **Congestion Levels**: Displays predicted traffic congestion levels based on inputs from the user.

## Pages

1. **Signal Simulator**: Simulate traffic signal timings based on vehicle flow and manage congestion.
2. **Congestion Levels**: Displays predicted traffic congestion levels using AI.
3. **Shortest Route**: Suggests the shortest and most optimal route based on current and predicted traffic conditions.
4. **Login Page**: Users can log in via Google OAuth to access the system.

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Backend**: (To be added)
- **Google Maps API**: For location selection, map visualization, and route suggestions.
- **AI Traffic Prediction Model**: Machine learning model trained on historical traffic, weather, and time data.
- **Google OAuth**: For user authentication and login functionality.

## How to Run

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/traffic-management-system.git
    cd traffic-management-system
    ```

2. Install the necessary dependencies and libraries (e.g., if using Node.js for the backend).

3. Replace the Google Maps API key and Google OAuth credentials with your own in the script tag and backend configuration:

    ```html
    <script async defer
        src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=places&callback=initMap">
    </script>
    ```

4. Run the application locally or deploy it to a server.

5. Access the different features via the navigation bar:
    - **Signal Simulator**
    - **Congestion Levels**
    - **Shortest Route**
    - **Login (Google OAuth)**

## AI Traffic Prediction Model

The AI model predicts traffic congestion based on the following factors:
- **Location**: Selected by the user using the Google Maps search.
- **Date & Time**: Users provide date and time for which they want to predict traffic.
- **Day of the Week**: Automatically calculated based on the selected date.
- **Weather Conditions**: Users choose between Clear, Rainy, Foggy, and Snowy conditions.
- **Holiday**: Users specify whether it’s a holiday or not, affecting traffic patterns.

The prediction is displayed in the form of expected traffic levels (e.g., Light, Moderate, Heavy).

## User Authentication

- **Google OAuth**: Users can log in using their Google accounts to access the platform securely.
- After logging in, users can access the traffic prediction and simulation features.
- The logout option is available, redirecting users to the welcome page.

## Future Enhancements

- **Backend Integration**: Implement backend services for managing predictions and traffic data.
- **Real-time Traffic Data**: Incorporate live traffic data for more accurate predictions.
- **User Dashboard**: Allow users to save and view their past traffic predictions.
- **Mobile Responsiveness**: Ensure full compatibility and responsiveness on mobile devices.

## License

This project is licensed under the MIT License.

## Contributing

Feel free to contribute to this project by forking the repository, creating an issue, or submitting a pull request.

---

If you encounter any issues or have suggestions for improvements, please open an issue in the repository or contact us directly.
