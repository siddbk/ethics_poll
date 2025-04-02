# AI Ethics Poll Game

An interactive digital game to engage audiences with AI ethical dilemmas. This application enables participants to vote on ethical scenarios using their smartphones and see real-time results compared with established AI ethics frameworks.

## Features

- Present ethical AI dilemmas to your audience
- Participants vote via smartphones by scanning QR codes
- Real-time results visualization
- Comparison with AI ethics framework positions
- No external dependencies or hosting required
- Works for 100+ simultaneous participants
- Easy setup with minimal technical requirements

## Requirements

- Python 3.8 or higher
- Local network where all participants can connect
- Computer with ability to run Python and display presentation
- Participants' smartphones with QR code scanning capability

## Quick Start

1. **Clone or download this repository:**

```bash
git clone https://github.com/yourusername/ai-ethics-poll-game.git
cd ai-ethics-poll-game
```

2. **Create a virtual environment (recommended):**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Run the application:**

```bash
python app.py
```

5. **Access the admin panel:**

Open a web browser and navigate to `http://localhost:5000` (or the IP address shown in the console)

6. **Set up the display view:**

Click "Open Display View" in the admin panel, then display this window on the main screen visible to participants

7. **Start the game:**

Select a scenario from the sidebar to begin

## How to Play

1. **Presenter** selects an ethical scenario from the admin panel
2. **Participants** scan the displayed QR code using their smartphones
3. **Participants** read the scenario and select their ethical position
4. **Results** update in real-time on the main display
5. **Presenter** can reveal how different AI ethics frameworks would approach the scenario
6. **Repeat** with different scenarios

## Customizing Scenarios

You can customize the ethical scenarios by editing the `config.py` file. Each scenario includes:

- Title and description
- Multiple ethical positions
- Framework positions with explanations

## Technical Architecture

- **Backend**: Python Flask
- **Data Storage**: In-memory (no external database required)
- **Frontend**: HTML/CSS/JavaScript with Bootstrap
- **Visualization**: Chart.js
- **QR Generation**: qrcode library

## Development

### Project Structure

```
ai-ethics-poll-game/
├── app.py              # Main Flask application
├── config.py           # Configuration and scenarios
├── models.py           # Data models
├── utils.py            # Utility functions
├── requirements.txt    # Package dependencies
├── static/             # Static assets
│   ├── css/            # Stylesheets
│   ├── js/             # JavaScript
│   ├── qrcodes/        # Generated QR codes
│   └── exports/        # Exported results
└── templates/          # HTML templates
    ├── base.html       # Base template
    ├── index.html      # Admin panel
    ├── display.html    # Public display
    └── vote.html       # Voting page
```

### Adding New Scenarios

1. Open `config.py`
2. Add a new scenario to the `SCENARIOS` list following the existing format
3. Include framework positions for consistent comparison

### Extending the Application

- **Custom Styling**: Edit the CSS in `static/css/main.css`
- **Additional Features**: Modify `app.py` to add new routes or functionality
- **Export Results**: Use the "Export Results" button to save data for later analysis

## Troubleshooting

- **QR Codes not working**: Ensure devices are on the same network as the server
- **Cannot connect to server**: Check firewall settings and network connectivity
- **Slow response times**: Reduce polling frequency in JavaScript files

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- Flask - Web framework
- Chart.js - Visualization library
- Bootstrap - CSS framework
- qrcode - QR code generation library