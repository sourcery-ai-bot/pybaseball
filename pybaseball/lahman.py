import requests
import zipfile
import os
import pandas as pd
from io import BytesIO, StringIO
from bs4 import BeautifulSoup

url = "https://github.com/chadwickbureau/baseballdatabank/archive/master.zip"
base_string = os.path.join("baseballdatabank-master","core")

_handle = None
def get_lahman_zip():
    # Retrieve the Lahman database zip file, returns None if file already exists in cwd.
    # If we already have the zip file, keep re-using that.
    # Making this a function since everything else will be re-using these lines
    global _handle
    if os.path.exists(base_string):
        _handle = None
    elif not _handle:
        s = requests.get(url, stream=True)
        _handle = zipfile.ZipFile(BytesIO(s.content))
    return _handle

def download_lahman():
	# download entire lahman db to present working directory
	z = get_lahman_zip()
	if z is not None:
		z.extractall()
		z = get_lahman_zip()
		# this way we'll now start using the extracted zip directory
		# instead of the session ZipFile object

def parks():
    # do this for every table in the lahman db so they can exist as separate functions
    z = get_lahman_zip()
    f = os.path.join(base_string, "Parks.csv")
    return pd.read_csv(
        f if z is None else z.open(f), header=0, sep=',', quotechar="'"
    )

def all_star_full():
    z = get_lahman_zip()
    f = os.path.join(base_string, "AllstarFull.csv")
    return pd.read_csv(
        f if z is None else z.open(f), header=0, sep=',', quotechar="'"
    )

def appearances():
    z = get_lahman_zip()
    f = os.path.join(base_string, "Appearances.csv")
    return pd.read_csv(
        f if z is None else z.open(f), header=0, sep=',', quotechar="'"
    )

def awards_managers():
    z = get_lahman_zip()
    f = os.path.join(base_string, "AwardsManagers.csv")
    return pd.read_csv(
        f if z is None else z.open(f), header=0, sep=',', quotechar="'"
    )

def awards_players():
    z = get_lahman_zip()
    f = os.path.join(base_string, "AwardsPlayers.csv")
    return pd.read_csv(
        f if z is None else z.open(f), header=0, sep=',', quotechar="'"
    )

def awards_share_managers():
    z = get_lahman_zip()
    f = os.path.join(base_string, "AwardsShareManagers.csv")
    return pd.read_csv(
        f if z is None else z.open(f), header=0, sep=',', quotechar="'"
    )

def awards_share_players():
    z = get_lahman_zip()
    f = os.path.join(base_string, "AwardsSharePlayers.csv")
    return pd.read_csv(
        f if z is None else z.open(f), header=0, sep=',', quotechar="'"
    )

def batting():
    z = get_lahman_zip()
    f = os.path.join(base_string, "Batting.csv")
    return pd.read_csv(
        f if z is None else z.open(f), header=0, sep=',', quotechar="'"
    )

def batting_post():
    z = get_lahman_zip()
    f = os.path.join(base_string, "BattingPost.csv")
    return pd.read_csv(
        f if z is None else z.open(f), header=0, sep=',', quotechar="'"
    )

def college_playing():
    z = get_lahman_zip()
    f = os.path.join(base_string, "CollegePlaying.csv")
    return pd.read_csv(
        f if z is None else z.open(f), header=0, sep=',', quotechar="'"
    )

def fielding():
    z = get_lahman_zip()
    f = os.path.join(base_string, "Fielding.csv")
    return pd.read_csv(
        f if z is None else z.open(f), header=0, sep=',', quotechar="'"
    )

def fielding_of():
    z = get_lahman_zip()
    f = os.path.join(base_string, "FieldingOF.csv")
    return pd.read_csv(
        f if z is None else z.open(f), header=0, sep=',', quotechar="'"
    )

def fielding_of_split():
    z = get_lahman_zip()
    f = os.path.join(base_string, "FieldingOFsplit.csv")
    return pd.read_csv(
        f if z is None else z.open(f), header=0, sep=',', quotechar="'"
    )

def fielding_post():
    z = get_lahman_zip()
    f = os.path.join(base_string, "FieldingPost.csv")
    return pd.read_csv(
        f if z is None else z.open(f), header=0, sep=',', quotechar="'"
    )

def hall_of_fame():
    z = get_lahman_zip()
    f = os.path.join(base_string, "HallOfFame.csv")
    return pd.read_csv(
        f if z is None else z.open(f), header=0, sep=',', quotechar="'"
    )

def home_games():
    z = get_lahman_zip()
    f = os.path.join(base_string, "HomeGames.csv")
    return pd.read_csv(
        f if z is None else z.open(f), header=0, sep=',', quotechar="'"
    )

def managers():
    z = get_lahman_zip()
    f = os.path.join(base_string, "Managers.csv")
    return pd.read_csv(
        f if z is None else z.open(f), header=0, sep=',', quotechar="'"
    )

def managers_half():
    z = get_lahman_zip()
    f = os.path.join(base_string, "ManagersHalf.csv")
    return pd.read_csv(
        f if z is None else z.open(f), header=0, sep=',', quotechar="'"
    )

# Alias for people -- the new name for master
def master():
	return people()

def people():
    z = get_lahman_zip()
    f = os.path.join(base_string, "People.csv")
    return pd.read_csv(
        f if z is None else z.open(f), header=0, sep=',', quotechar="'"
    )

def pitching():
    z = get_lahman_zip()
    f = os.path.join(base_string, "Pitching.csv")
    return pd.read_csv(
        f if z is None else z.open(f), header=0, sep=',', quotechar="'"
    )

def pitching_post():
    z = get_lahman_zip()
    f = os.path.join(base_string, "PitchingPost.csv")
    return pd.read_csv(
        f if z is None else z.open(f), header=0, sep=',', quotechar="'"
    )

def salaries():
    z = get_lahman_zip()
    f = os.path.join(base_string, "Salaries.csv")
    return pd.read_csv(
        f if z is None else z.open(f), header=0, sep=',', quotechar="'"
    )

def schools():
	z = get_lahman_zip()
	f = os.path.join(base_string, "Schools.csv")
	data = pd.read_csv(f if z is None else z.open(f), header=0, sep=',', quotechar='"') # different here bc of doublequotes used in some school names
	return data

def series_post():
    z = get_lahman_zip()
    f = os.path.join(base_string, "SeriesPost.csv")
    return pd.read_csv(
        f if z is None else z.open(f), header=0, sep=',', quotechar="'"
    ) 

def teams():
    z = get_lahman_zip()
    f = os.path.join(base_string, "Teams.csv")
    return pd.read_csv(
        f if z is None else z.open(f), header=0, sep=',', quotechar="'"
    )

def teams_franchises():
    z = get_lahman_zip()
    f = os.path.join(base_string, "TeamsFranchises.csv")
    return pd.read_csv(
        f if z is None else z.open(f), header=0, sep=',', quotechar="'"
    )

def teams_half():
    z = get_lahman_zip()
    f = os.path.join(base_string, "TeamsHalf.csv")
    return pd.read_csv(
        f if z is None else z.open(f), header=0, sep=',', quotechar="'"
    )

