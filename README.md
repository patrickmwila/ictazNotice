# ICTAZ Notice Page

A simple, responsive web application built with Flask and Bootstrap to display an important notice for ICT Association of Zambia (ICTAZ) members regarding the registration system.

## Features

- Clean, professional design matching ICTAZ branding
- Responsive layout for all devices
- Clear notice display with important information
- Contact information section
- Footer with copyright information

## Tech Stack

- Python 3.x
- Flask 3.0.0
- Bootstrap 5.3.2
- Google Fonts (Poppins and Open Sans)

## Project Structure

```
ictazNotice/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── static/
│   ├── css/
│   │   └── style.css  # Custom styles
│   └── images/
│       └── ictaz_logo.png
├── templates/
│   └── notice.html    # Main notice template
└── guide.md           # Deployment guide
```

## Local Development Setup

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
- Windows:
```bash
venv\Scripts\activate
```
- Linux/Mac:
```bash
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the development server:
```bash
python app.py
```

5. Visit `http://localhost:5000` in your web browser

## Deployment

For detailed deployment instructions on Ubuntu 18.04, please refer to the `guide.md` file.

## Browser Support

The application is tested and works on:
- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Copyright © ICT Association of Zambia | All Rights Reserved
