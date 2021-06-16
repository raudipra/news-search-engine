# News Search Engine (news-search-engine)

Web app to search news from all news sources using news API

## Install the dependencies
```bash
pip install -r requirements.txt
```

## Setup the Configuration File
- Create a new file named .flaskenv following the format of .flaskenv.example


## Start the app in development mode
```bash
python app.py
```

## Build the app for production (For Ubuntu 18.04)
- `cd ../deployments/services`
- Modify the path in the `news.service` file
- Copy the `news.service` to `/etc/systemd/system/`
- Run `sudo systemctl start news`
