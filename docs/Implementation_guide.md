# AI Ethics Poll Game - Implementation Guide

This guide provides detailed instructions for setting up, testing, and deploying the AI Ethics Poll Game for your company event.

## 1. Development Setup

### 1.1 Environment Setup

1. **Ensure Python is installed:**
   ```bash
   python --version  # Should be 3.8 or higher
   ```

2. **Create a project directory:**
   ```bash
   mkdir ai-ethics-poll
   cd ai-ethics-poll
   ```

3. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Create the file structure:**
   ```
   ai-ethics-poll/
   ├── app.py
   ├── config.py
   ├── models.py
   ├── utils.py
   ├── requirements.txt
   ├── static/
   │   └── css/
   │       └── main.css
   └── templates/
       ├── base.html
       ├── index.html
       ├── display.html
       └── vote.html
   ```

5. **Install required packages:**
   ```bash
   pip install Flask qrcode pillow
   ```

### 1.2 Adding the Code

1. Copy each provided code file into its respective location in your project structure.
2. Create the necessary directories:
   ```bash
   mkdir -p static/css static/qrcodes static/exports
   mkdir -p templates
   ```

### 1.3 Customizing Content

1. **Customize scenarios in `config.py`:**
   - Modify existing scenarios to fit your audience
   - Add company-specific examples if relevant
   - Ensure frameworks represent diverse ethical viewpoints

2. **Customize styling (optional):**
   - Modify `static/css/main.css` to match your company branding
   - Update colors, fonts, and styles as needed

## 2. Testing

### 2.1 Local Testing

1. **Start the application:**
   ```bash
   python app.py
   ```

2. **Access admin panel:**
   Open `http://localhost:5000` in your browser

3. **Test the following flows:**
   - Create a scenario and view the QR code
   - Open the voting page in a different browser/device
   - Submit votes and check if they appear in real-time
   - Test multiple simultaneous connections
   - Verify results visualization works correctly

### 2.2 Network Testing

1. **Determine your local IP address:**
   The application will show this when starting, or you can find it with:
   ```bash
   ipconfig  # Windows
   ifconfig  # Mac/Linux
   ```

2. **Connect multiple devices to the same network:**
   - Ensure all test devices are on the same Wi-Fi network
   - Try with at least 5-10 different devices

3. **Access the application using the IP address:**
   `http://<your-ip-address>:5000`

4. **Test performance with multiple simultaneous votes:**
   - Have everyone vote at the same time
   - Monitor server response and browser performance

### 2.3 Stress Testing

For events with large audiences (100+ participants), simulation testing is recommended:

1. **Install load testing tools:**
   ```bash
   pip install locust
   ```

2. **Create a simple load test script:**
   ```python
   # locustfile.py
   from locust import HttpUser, task, between

   class VotingUser(HttpUser):
       wait_time = between(1, 5)
       
       @task
       def vote(self):
           scenario_id = "scenario1"
           voter_id = f"test_voter_{self.user_id}"
           choice = "A"  # Randomly choose in a real test
           
           self.client.post("/submit_vote", json={
               "scenario_id": scenario_id,
               "voter_id": voter_id,
               "choice": choice
           })
   ```

3. **Run the load test:**
   ```bash
   locust --host=http://localhost:5000
   ```

4. **Gradually increase users to simulate event attendance**

## 3. Deployment

### 3.1 Pre-Event Setup

1. **Prepare the host machine:**
   - Use a laptop with good battery life
   - Ensure Python and all dependencies are installed
   - Pre-generate QR codes if possible
   - Test the application again on the actual event network

2. **Network considerations:**
   - Coordinate with IT to ensure the local network can handle 100+ simultaneous connections
   - Get a dedicated IP address if possible
   - Verify that firewalls won't block the application

3. **Display setup:**
   - Test the display view on the actual presentation screen
   - Ensure QR codes are large enough to be scanned from a distance
   - Adjust font sizes for visibility in the venue

### 3.2 Event Day Deployment

1. **Start the application early:**
   ```bash
   python app.py
   ```

2. **Connect to the venue network:**
   - Verify IP address is accessible
   - Test with a few devices before the audience arrives

3. **Display the admin panel on your screen and the display view on the presentation screen**

4. **Have a backup plan:**
   - Keep the repository on a USB drive
   - Have installation instructions ready if you need to switch computers
   - Create screenshots of scenarios in case the application fails

### 3.3 Running the Game

1. **Introduce the game concept to the audience**
2. **Display the QR code and instruct everyone to scan it**
3. **Allow 1-2 minutes for voting on each scenario**
4. **Discuss results and framework positions**
5. **Move to the next scenario**
6. **Export results at the end for later analysis**

## 4. Troubleshooting Common Issues

### 4.1 Connection Issues

- **Problem**: Participants cannot connect to the application
  - **Solution**: Verify network connectivity and firewall settings
  - **Workaround**: Create a mobile hotspot from the presenter's computer

- **Problem**: QR codes not scanning
  - **Solution**: Increase QR code size or brightness
  - **Workaround**: Display the direct URL for manual entry

### 4.2 Performance Issues

- **Problem**: Slow response with many participants
  - **Solution**: Reduce polling frequency in JavaScript
  - **Workaround**: Refresh results manually instead of auto-updating

- **Problem**: Application crashes
  - **Solution**: Restart the application
  - **Workaround**: Split audience into groups

### 4.3 Display Issues

- **Problem**: Charts not displaying correctly
  - **Solution**: Check browser compatibility
  - **Workaround**: Use simpler visualization or text-based results

## 5. Post-Event

1. **Export all results for analysis**
2. **Gather feedback from participants**
3. **Review technical performance for future improvements**
4. **Share insights learned from the ethical positions chosen**

## 6. Additional Resources

- Flask Documentation: https://flask.palletsprojects.com/
- Chart.js Documentation: https://www.chartjs.org/docs/
- QR Code Library: https://pypi.org/project/qrcode/