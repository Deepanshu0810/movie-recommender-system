# Movie Recommender System

This movie recommender system is a <b>content-based recommender</b> system i.e. this system recommend movies based on the similarities of the query of the user and the movies.<br>
Checkout the web app <a href="">here</a>

## Requirements
> ipykernal<br>
> pandas<br>
> numpy<br>
> scikit-learn<br>
> pickle5<br>
> streamlit<br>
> requests<br>

## Run the app in your Local Environemnt
1. Create a new environment in your working directory
```
conda create -p venv python==3.7 -y
```

2. Get the required files
```
git clone https://github.com/Deepanshu0810/movie-recommender-system.git
```

3. Install all the libraries and modules
```
pip install -r requirements.txt
```

4. Activate the environment 
```
activate venv/
```

5. Start the web-server in your local host
```
streamlit run app.py
```
