import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "https://github.com/Ro-han12/GOOGLE-Solution-Challenge-2024.git"
AUTHOR_USER_NAME = "Ro-han12","shreyas1455","rohith4088"
SRC_REPO = "GoogleSolutionChallenge"
AUTHOR_EMAIL = "rohannair2939@gmail.com","rohithjaya2939@gmail.com","shreyas.rajesh14@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Solution Challenge 2024-India Regional Bootcamp:The Sustainable Consumer Assistant App",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)