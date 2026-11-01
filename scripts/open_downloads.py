import subprocess

def open_downloads():
	"""
	Открывает оффициальные сайты с приложениями
	"""

	sites = {
		"Firefox": "https://www.firefox.com/en-US/thanks/",
		"Visual Studio Code": "https://code.visualstudio.com/thank-you?dv=darwinarm64&build=stable",
		"Insomnia": "https://insomnia.rest/download/",
		"DBeaver": "https://dbeaver.io/download/",
		"Docker": "https://docs.docker.com/desktop/setup/install/mac-install/",
		"Better Display": "https://betterdisplay.pro/",
		"Linear Mouse": "https://github.com/linearmouse/linearmouse",
		"Garage Band": "https://apps.apple.com/ge/app/garageband/id682658836?mt=12",
		"Red Shield VPN": "https://redshieldvpn.com/ru/help/apps/macos/install?dl=mac",
		"Telegram": "https://desktop.telegram.org/",
		"NVM": "https://github.com/nvm-sh/nvm",
		"Rectangle": "https://github.com/rxhanson/Rectangle/releases",
		"Starship": "https://github.com/starship/starship"
	}

	for name, url in sites.items():
		print(f"open: {name}")
		subprocess.run(["open", url], check=True)


if (__name__ == "__main__"):
	open_downloads()